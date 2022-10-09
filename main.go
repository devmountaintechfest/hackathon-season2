package main

import (
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/markkj/hackathon-season2/internal/csv"
	"github.com/markkj/hackathon-season2/internal/json"
	"github.com/markkj/hackathon-season2/internal/models"
	"github.com/markkj/hackathon-season2/internal/sqlite"
	"github.com/markkj/hackathon-season2/internal/xml"
)

const (
	moveStatus = "1"
)

var (
	columnStrings = []string{
		"EMPID",
		"PASSPORT",
		"FIRSTNAME",
		"LASTNAME",
		"GENDER",
		"BIRTHDAY",
		"NATIONALITY",
		"HIRED",
		"DEPT",
		"POSITION",
		"STATUS",
		"REGION",
	}
)

func main() {
	outputFolder := "output"

	os.Mkdir(outputFolder, os.ModePerm)
	data, err := xml.ReadXMLFromHackathon("./data-devclub-1.xml")
	if err != nil {
		log.Fatal(err)
	}
	employees, err := models.MapToEmployees(data)
	if err != nil {
		log.Fatal(err)
	}

	// ** Start clean anomalies information challenge
	employees = employees.FilterBy(models.IsValidStatus, models.IsValidGender, models.IsActiveStatus)
	fmt.Printf("clean result row = %d\n", len(employees))
	err = exportToCSV(fmt.Sprintf("%s/clean", outputFolder), employees)
	if err != nil {
		log.Fatal(err)
	}
	// ** End clean anomalies information challenge

	// ** Start migration Challenge
	// Step 1 ย้ายพนักงานจากสายการบิน DevMountain ไป DevClub เฉพาะตำแหน่ง Air Hostess, Pilot และ Steward ที่มีสถานะ Active
	// Note "Active is already filter from clean data above"
	// check role
	employees = employees.FilterBy(models.IsOnlyPosition)
	fmt.Printf("check only positon steward,airhostess,pilot result row = %d\n", len(employees))
	err = exportToCSV(outputFolder+"/only_steward_airhostess_pilot_and_active", employees)
	if err != nil {
		log.Fatal(err)
	}
	//TODO: store CSV data to SQLite from step 1 here

	// Step 2 สำหรับตำแหน่งอายุการทำงาน เกิน 3 ปี
	// check exp more than three compare with current date
	employees = employees.FilterBy(models.IsExpMoreThanThree)
	fmt.Printf("check only exp more than three result row = %d\n", len(employees))
	err = exportToCSV(outputFolder+"/only_exp_more_than_three", employees)
	if err != nil {
		log.Fatal(err)
	}

	err = exportToCSV(outputFolder+"/DevMountain", employees)
	if err != nil {
		log.Fatal(err)
	}
	//TODO: store CSV data to SQLite from step 2 here

	// Step 3 สร้างไฟล์ CSV แยกตามสัญชาติของพนักงาน
	groupByNation := employees.GroupByNation()
	for key, group := range groupByNation {
		err = exportToCSV(fmt.Sprintf(outputFolder+"/DevMountain-%s", key), group)
		if err != nil {
			log.Fatal(err)
		}
	}

	//TODO: here
	sqlitePath := outputFolder + "/DevMountain.sqlite"
	sqlite.WriteSql(outputFolder+"/clean.csv", sqlitePath)
	// Step 4 สร้าง SQLite view ที่สามารถ query ตามประเทศที่ทำงาน
	sqlite.ViewRegionSql(sqlitePath)
	// Step 5 สร้าง SQLite view สำหรับแบ่งตาม department
	sqlite.ViewDepartmentSql(sqlitePath)
	// Step 6 สร้าง SQLite view ที่สามารถ query ตามสัญชาติของพนักงาน
	sqlite.ViewNationSql(sqlitePath)
	// ** End migration Challenge
}

func exportToCSV(fileName string, employees models.Employees) error {
	csvFile := &csv.CsvData{
		Columns: columnStrings,
		Records: []string{},
	}
	for _, emp := range employees {
		record := make([]string, len(columnStrings))
		record[0] = strconv.Itoa(emp.EMPID)
		record[1] = emp.PASSPORT
		record[2] = emp.FIRSTNAME
		record[3] = emp.LASTNAME
		record[4] = strconv.Itoa(emp.GENDER)
		record[5] = emp.BIRTHDAY.Format("02-01-2006")
		record[6] = emp.NATIONALITY
		record[7] = emp.HIRED.Format("02-01-2006")
		record[8] = emp.DEPT
		record[9] = emp.POSITION
		record[10] = strconv.Itoa(emp.STATUS)
		record[11] = emp.REGION

		csvFile.AddRecord(record)
	}
	path, _ := os.Getwd()
	path += fmt.Sprintf("/%s.csv", fileName)
	err := csvFile.BuildCsvFile(path)
	if err != nil {
		log.Fatal(err)
	}
	records, err := csv.CSVFileToMap(path)
	if err != nil {
		log.Fatal(err)
	}
	json.ExportToJsonFile(records, fileName)
	return nil
}
