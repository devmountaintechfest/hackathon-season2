package json

import (
	"encoding/json"
	"os"
)

func ExportToJsonFile(records []map[string]interface{}, fileName string) error {
	jsonFile, err := os.Create(fileName + ".json")
	if err != nil {
		return err
	}
	// adjust format of output
	jsonFile.WriteString("[\n")
	defer jsonFile.Close()
	for i, row := range records {
		jsonStr, err := json.MarshalIndent(row, "", " ")
		if err != nil {
			return err
		}
		//only add "," if not the last row
		str := string(jsonStr)
		if i != len(records)-1 {
			str = str + ","
		}
		_, err = jsonFile.WriteString(str)
		if err != nil {
			return err
		}
	}
	// adjust format of output
	jsonFile.WriteString("\n]")
	return nil
}
