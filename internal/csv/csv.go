package csv

import (
	"fmt"
	"os"
	"strings"
)

type CsvData struct {
	Columns []string
	Records []string
}

func (c *CsvData) BuildCsvFile() error {
	csvFile, err := os.Create("DevMountain.csv")
	if err != nil {
		return err
	}
	defer csvFile.Close()

	_, err = csvFile.WriteString(prepareColunm(c.Columns))
	if err != nil {
		return err
	}
	// fmt.Printf("wrote %v bytes\n", c)
	err = prepareRow(c.Records, csvFile)
	// fmt.Println(c.Records)
	if err != nil {
		return err
	}
	return err
}

func prepareRow(rows []string, file *os.File) error {

	fmt.Println(rows)
	for i, s := range rows {
		var sb strings.Builder
		sb.WriteString(s)
		// if is last data of rows no need to add "\n"
		if i != len(rows)-1 {
			sb.WriteString("\n")
		}
		_, err := file.Write([]byte(sb.String()))
		if err != nil {
			return err
		}
	}
	return nil
}

func prepareColunm(columns []string) string {
	var sb strings.Builder
	for i, s := range columns {
		sb.WriteString(s)
		// if is last data of column no need to add ";"
		if i != len(columns)-1 {
			sb.WriteString(";")
		}
	}
	//add newline for end of colunm
	sb.WriteString("\n")
	return sb.String()
}

func (c *CsvData) SetColumn(columns []string) {
	c.Columns = columns
}

func (c *CsvData) AddRecord(data []string) {
	var sb strings.Builder
	for i, s := range data {
		sb.WriteString(s)
		// if is last data of column no need to add ";"
		if i != len(data)-1 {
			sb.WriteString(";")
		}
	}
	c.Records = append(c.Records, sb.String())
}
