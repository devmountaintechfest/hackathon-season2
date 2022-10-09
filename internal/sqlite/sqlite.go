package sqlite

import (
	"database/sql"
	"fmt"
	"os"
	"strings"

	"github.com/markkj/hackathon-season2/internal/csv"
	_ "github.com/mattn/go-sqlite3"
)

/*
SqlField type builder
*/

type SqlField struct {
	schema  []string
	colName string
}

func (f *SqlField) addSchema(s string) {
	f.schema = append(f.schema, s)
}

func (f *SqlField) Name(name string) *SqlField {
	f.colName = name
	return f
}

func (f *SqlField) PrimaryKey() *SqlField {
	f.addSchema("primary key")
	return f
}

func (f *SqlField) Text() *SqlField {
	f.addSchema("text")
	return f
}

func (f *SqlField) Int() *SqlField {
	f.addSchema("integer")
	return f
}

func (f *SqlField) Date() *SqlField {
	f.addSchema("date")
	return f
}

func (f *SqlField) Schema() string {
	schem := strings.Join(f.schema, " ")
	col := fmt.Sprintf("%s ", f.colName)
	// return strings.Join(f.schema, " ")
	return col + schem
}

// SqlField builder ...
func Field(name string) *SqlField {
	f := &SqlField{}
	f.Name(name)
	return f
}

type SqlData struct {
	Conn      *sql.DB
	tableName string
	tableCols []string
}

func (c *SqlData) UseTable(tableName string) {
	c.tableName = tableName
}

func (c *SqlData) UseSchema(columns []*SqlField) error {
	cols := ""
	for _, v := range columns {
		c.tableCols = append(c.tableCols, v.colName)
		cols = cols + v.Schema() + ","
	}

	cols = strings.TrimSuffix(cols, ",")

	cmd := fmt.Sprintf("create table if not exists %s (%s)", c.tableName, cols)
	stmt, err := c.Conn.Prepare(cmd)
	if err != nil {
		return err
	}

	_, err = stmt.Exec()
	if err != nil {
		return err
	}

	return nil
}

func (c *SqlData) AddRow(data []string) error {
	cols := strings.Join(c.tableCols, ",")

	vals := []interface{}{}
	for _, v := range data {
		vals = append(vals, v)
	}

	cmd := fmt.Sprintf("insert into %s(%s) values(?,?,?,?,?,?,?,?,?,?,?,?)", c.tableName, cols)

	stmt, err := c.Conn.Prepare(cmd)
	if err != nil {
		fmt.Println(err)
	}

	_, err = stmt.Exec(vals...)
	if err != nil {
		fmt.Println(err)
	}

	return nil
}

// type

func (c *SqlData) Query(cmd string) error {
	// data := c.Conn.QueryRow("select *  from 'devMountain2' A where A.HIRED >= '2010-04-01'")
	nationsT := make([]string, 0)
	nations, _ := c.Conn.Query(cmd)

	// v.Scan(&nation)

	// fmt.Println("nation", len(nation))
	for nations.Next() {
		var nation string
		if err := nations.Scan(&nation); err != nil {
		}
		nationsT = append(nationsT, nation)
	}

	fmt.Println(nationsT)

	return nil
}

func (c *SqlData) QueryVis5() map[string]interface{} {
	query := "select count(EMPID) as num,NATIONALITY from 'devMountain2' A group by A.NATIONALITY"

	result := map[string]interface{}{}

	// fmt.Println(query)
	conutrysCountQuery, _ := c.Conn.Query(query)

	fmt.Println(conutrysCountQuery)

	for conutrysCountQuery.Next() {
		var countNum int64
		var country string
		if err := conutrysCountQuery.Scan(&countNum, &country); err != nil {

		} else {
			fmt.Println(countNum, country)
			result[country] = countNum
		}

	}

	return result

}

/*
alway return db connection
*/
func OpenDB(filePath string) SqlData {
	_, err := os.Stat(filePath)

	if err != nil {
		file, createErr := os.Create(filePath)

		if createErr != nil {
			return SqlData{}
		}

		file.Close()
	}

	database, err := sql.Open("sqlite3", filePath)

	if err != nil {
		return SqlData{}
	}

	return SqlData{Conn: database}

}

func WriteSql(sourcePath string, filePath string) error {
	db := OpenDB(filePath)
	defer db.Conn.Close()

	if db.Conn == nil {
		fmt.Println("erro")
	}

	db.UseTable("devMountain2")

	err := db.UseSchema([]*SqlField{
		Field("EMPID").Int().PrimaryKey(),
		Field("PASSPORT").Text(),
		Field("FIRSTNAME").Text(),
		Field("LASTNAME").Text(),
		Field("GENDER").Int(),
		Field("BIRTHDAY").Date(),
		Field("NATIONALITY").Text(),
		Field("HIRED").Date(),
		Field("DEPT").Text(),
		Field("POSITION").Text(),
		Field("STATUS").Int(),
		Field("REGION").Text(),
	})

	if err != nil {
		fmt.Println(err)
	}

	employees, err := csv.CSVFileToList(sourcePath)
	// employees, err := csv.CSVFileToList("../../output/clean.csv")

	if err != nil {
		fmt.Println(err)
	}

	for _, employee := range employees {
		db.AddRow(employee)
	}

	ViewNationSql(filePath)
	ViewDepartmentSql(filePath)
	ViewRegionSql(filePath)

	return nil
}

func ToSqlite(filePath string, fileTarget string) error {
	print(filePath)

	_, err := os.ReadFile(filePath)

	if err != nil {
		return err
	}

	csvFile, err := os.Create(fileTarget)

	if err != nil {
		return err
	}

	defer csvFile.Close()

	return nil
}

func ViewNationSql(filePath string) error {
	db := OpenDB(filePath)
	defer db.Conn.Close()

	if db.Conn == nil {
		fmt.Println("erro")
	}

	nationArr := make([]string, 0)
	nations, _ := db.Conn.Query("SELECT NATIONALITY FROM 'devMountain2' group by NATIONALITY")

	for nations.Next() {
		var nation string
		if err := nations.Scan(&nation); err != nil {
		}

		nationArr = append(nationArr, nation)
	}

	for i := range nationArr {
		cmd := fmt.Sprintf("CREATE VIEW nation%s as SELECT * FROM 'devMountain2' WHERE NATIONALITY = '%s'", nationArr[i], nationArr[i])
		_, err := db.Conn.Exec(cmd)
		if err != nil {
			return err
		}
		// db.Conn.Exec("SELECT * FROM nation%s", nationArr[i])
	}
	return nil
}

func ViewDepartmentSql(filePath string) error {
	db := OpenDB(filePath)
	defer db.Conn.Close()

	if db.Conn == nil {
		fmt.Println("erro")
	}

	deptArr := make([]string, 0)
	depts, _ := db.Conn.Query("SELECT DEPT FROM 'devMountain2' group by DEPT")

	for depts.Next() {
		var dept string
		if err := depts.Scan(&dept); err != nil {
		}

		deptArr = append(deptArr, dept)
	}

	for i := range deptArr {
		query := fmt.Sprintf("CREATE VIEW department%s as SELECT * FROM 'devMountain2' WHERE DEPT = '%s'", strings.ReplaceAll(deptArr[i], " ", ""), deptArr[i])
		_, err := db.Conn.Exec(query)
		if err != nil {
			return err
		}
		db.Conn.Exec("SELECT * FROM department%s", deptArr[i])
	}
	return nil
}

func ViewRegionSql(filePath string) error {
	db := OpenDB(filePath)
	defer db.Conn.Close()

	if db.Conn == nil {
		fmt.Println("erro")
	}

	regionArr := make([]string, 0)
	regions, _ := db.Conn.Query("SELECT REGION FROM 'devMountain2' group by REGION")

	for regions.Next() {
		var region string
		if err := regions.Scan(&region); err != nil {
		}
		regionArr = append(regionArr, region)
	}

	for i := range regionArr {
		query := fmt.Sprintf("CREATE VIEW region%s as SELECT * FROM 'devMountain2' WHERE REGION = '%s'", regionArr[i], regionArr[i])
		_, err := db.Conn.Exec(query)
		if err != nil {
			return err
		}
		db.Conn.Exec("SELECT * FROM region%s", regionArr[i])
	}
	return nil
}
