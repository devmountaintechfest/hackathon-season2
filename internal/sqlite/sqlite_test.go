package sqlite

import (
	"fmt"
	"testing"
)

func TestToSqlite(t *testing.T) {
	err := ToSqlite("../../", "./target.csv")

	if err != nil {
		// t.Errorf("error")
		fmt.Println(err)
	}
}

func TestToSqliteInvalidPath(t *testing.T) {
	err := ToSqlite("nowhere", "./target.csv")

	if err == nil {
		t.Errorf("error")
	}
}

func TestWriteSql(t *testing.T) {
	err := WriteSql("../../output/clean.csv", "./target.sqlite")

	if err != nil {
		// t.Errorf("error")
	}
}

func TestSqlField(t *testing.T) {
	field1 := new(SqlField).PrimaryKey().Text()
	fmt.Println(field1.Schema())

}

func TestSqliteManager(t *testing.T) {
	// sql := SqlManager{}
	// sql.OpenDB("./target.sqlite")

	// err := sql.DB.Query("")

	// if err != nil {
	// 	fmt.Println(err)
	// }
	sql := OpenDB("./target.sqlite")
	// sql.Query("SELECT NATIONALITY FROM 'devMountain2' group by NATIONALITY")
	sql.QueryVis5()
}
