package xml

import (
	"fmt"
	"os"
	"strings"
)

const (
	startIndexFrom = 3
	jumpLenght     = 14
	recordLenght   = 12
)

// ReaderXMLHackathon is an object responisble for reader xml and validate data to other file
type ReaderXMLHackathon struct {
	recordStrings []string
}

// ReadXMLFromHackathon is a function read xml file to struct
func ReadXMLFromHackathon(filePath string) ([]map[string]string, error) {
	dataBytes, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Println(err)
	}

	reader := ReaderXMLHackathon{
		recordStrings: strings.Split(string(dataBytes), "\n"),
	}
	return reader.getAttribute()
}

// getAttribute is helper function to get string postion from records of xml file
func (r *ReaderXMLHackathon) getAttribute() ([]map[string]string, error) {
	data := make([]map[string]string, 0)
	for i := startIndexFrom; i < len(r.recordStrings); i += jumpLenght {
		mapData := make(map[string]string)

		key, _ := r.readTag(r.recordStrings[i])
		if key != "EMPID" {
			return nil, fmt.Errorf("error invalid format xml")
		}

		for _, line := range r.recordStrings[i : i+recordLenght] { // loop start from first column of that record to last
			key, value := r.readTag(line)
			mapData[key] = value
		}
		data = append(data, mapData)
	}
	return data, nil
}

// readTag is a function for read xml tag an return key and value
func (r *ReaderXMLHackathon) readTag(line string) (string, string) {
	var (
		key   string
		value string
	)

	var (
		readKey   bool
		readValue bool
	)
	for _, c := range line {
		if readValue && string(c) == "<" {
			// end
			break
		} else if string(c) == ">" {
			// end key
			readKey = false
			// start value
			readValue = true
			continue
		} else if string(c) == "<" {
			readKey = true
			continue
		}
		if readKey {
			key += string(c)
		} else if readValue {
			value += string(c)
		}
	}
	return key, value
}
