package csv

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

type CsvData struct {
	Columns []string
	Records []string
}

func (c *CsvData) BuildCsvFile(outPath string) error {
	csvFile, err := os.Create(outPath)
	if err != nil {
		return err
	}
	defer csvFile.Close()

	_, err = csvFile.WriteString(prepareColunm(c.Columns))
	if err != nil {
		return err
	}

	err = prepareRow(c.Records, csvFile)
	if err != nil {
		return err
	}
	return err
}

func prepareRow(rows []string, file *os.File) error {
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

// CSVFileToMap reads csv file into slice of map
func CSVFileToMap(filePath string) (returnMap []map[string]interface{}, err error) {

	// read csv file
	csvfile, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf(err.Error())
	}

	defer csvfile.Close()

	reader := bufio.NewReader(csvfile)
	if err != nil {
		return nil, err
	}
	header := []string{} // holds first row (header)
	isFirstRow := true
	for {
		row, _, err := reader.ReadLine()
		if err != nil {
			// if EOF error we just jump out of loop
			if err == io.EOF {
				break
			}
			return nil, err
		}
		rowStr := string(row)
		if isFirstRow {
			str := strings.Split(rowStr, ";")
			header = append(header, str...)
			isFirstRow = false
		} else {
			// for each cell, map[string]string k=header v=value
			line := make(map[string]interface{})
			str := strings.Split(rowStr, ";")
			for i := 0; i < len(str); i++ {
				line[header[i]] = str[i]
			}
			returnMap = append(returnMap, line)
		}
	}
	return
}

func CSVFileToList(filePath string) (returnMap [][]string, err error) {

	// read csv file
	csvfile, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf(err.Error())
	}

	defer csvfile.Close()

	reader := bufio.NewReader(csvfile)
	if err != nil {
		return nil, err
	}

	isFirstRow := true
	for {
		row, _, err := reader.ReadLine()
		if err != nil {
			// if EOF error we just jump out of loop
			if err == io.EOF {
				break
			}
			return nil, err
		}
		rowStr := string(row)
		if isFirstRow {
			isFirstRow = false
		} else {
			str := strings.Split(rowStr, ";")
			returnMap = append(returnMap, str)
		}
	}
	return
}
