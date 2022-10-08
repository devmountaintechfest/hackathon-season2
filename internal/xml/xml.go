package xml

import (
	"fmt"
	"os"
	"strings"
)

const (
	startIndexFrom               = 13
	jumpLenght                   = 14
	positionAtFirstIndexOfRecode = -10 // we will using this one to jump back to first data of that record
	moveStatus                   = "1"
)

// ReaderXMLHackathon is an object responisble for reader xml and validate data to other file
type ReaderXMLHackathon struct {
	recordStrings []string
}

// ReadXMLFromHackathon is a function read xml file to struct
func ReadXMLFromHackathon(filePath string) (interface{}, error) {
	dataBytes, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Println(err)
	}

	reader := ReaderXMLHackathon{
		recordStrings: strings.Split(string(dataBytes), "\n"),
	}
	return reader.getAttribute()
}

// func (r *ReaderXMLHackathon) checkIsValidToMove(index int) bool {
// 	_, status := r.readTag(r.recordStrings[index])
// 	// check status
// 	if status != moveStatus {
// 		return false
// 	}

// 	//Steward Pilot Airhostess
// 	_, role := r.readTag(r.recordStrings[index-1])
// 	if !strings.Contains("Steward Pilot Airhostess", role) {
// 		return false
// 	}

// 	return true
// }

// getAttribute is ...
func (r *ReaderXMLHackathon) getAttribute() ([]interface{}, error) {
	data := make([]interface{}, 0)
	for i := startIndexFrom; i <= len(r.recordStrings); i += jumpLenght {
		mapData := make(map[string]interface{})
		for _, line := range r.recordStrings[i+positionAtFirstIndexOfRecode : i+2] { // loop start from first column of that record to last
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
