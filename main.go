package main

import (
	"fmt"

	"github.com/markkj/hackathon-season2/internal/csv"
	"github.com/markkj/hackathon-season2/internal/xml"
)

func main() {
	data, err := xml.ReadXMLFromHackathon("./data-devclub-1.xml")
	if err != nil {
		fmt.Println(err)
	}
	dataArr := data.([]interface{})
	csvFile := &csv.CsvData{
		Columns: []string{},
		Records: []string{},
	}
	columnStrings := []string{
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
	csvFile.SetColumn(columnStrings)
	for _, row := range dataArr {
		fmt.Println(row)
		record := make([]string, len(columnStrings))
		for key, value := range row.(map[string]interface{}) {
			for i, c := range columnStrings {
				if key == c {
					record[i] = value.(string)
					break
				}
			}
		}
		csvFile.AddRecord(record)
	}
	err = csvFile.BuildCsvFile()
	if err != nil {
		fmt.Println(err)
	}
}
