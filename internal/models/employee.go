package models

import (
	"fmt"
	"reflect"
	"strconv"
	"time"
)

// Employee is ..
type Employee struct {
	EMPID       int
	PASSPORT    string
	FIRSTNAME   string
	LASTNAME    string
	GENDER      int
	BIRTHDAY    time.Time
	NATIONALITY string
	HIRED       time.Time
	DEPT        string
	POSITION    string
	STATUS      int
	REGION      string
}

// MapToEmployees is ...
func MapToEmployees(data []map[string]string) (Employees, error) {
	employees := make([]*Employee, 0)
	for _, row := range data {
		emp, err := NewEmployeeFromMap(row)
		if err != nil {
			return nil, err
		}
		employees = append(employees, emp)
	}
	return employees, nil
}

// NewEmployeeFromMap is a factory for new employee struct
func NewEmployeeFromMap(data map[string]string) (*Employee, error) {
	var emp Employee
	for key, value := range data {
		err := setField(&emp, key, value)
		if err != nil {
			return nil, err
		}
	}
	return &emp, nil
}

func setField(obj *Employee, name string, value interface{}) error {
	structValue := reflect.ValueOf(obj).Elem()
	structFieldValue := structValue.FieldByName(name)

	if !structFieldValue.IsValid() {
		return fmt.Errorf("No such field: %s in obj", name)
	}

	if !structFieldValue.CanSet() {
		return fmt.Errorf("Cannot set %s field value", name)
	}

	structFieldType := structFieldValue.Type()
	var err error
	switch structFieldType {
	case reflect.TypeOf(0):
		value, err = strconv.Atoi(value.(string))
		if err != nil {
			return err
		}
	case reflect.TypeOf(time.Now()):
		value, err = time.Parse("02-01-2006", value.(string))
		if err != nil {
			return err
		}
	}
	val := reflect.ValueOf(value)
	if structFieldType != val.Type() {
		return fmt.Errorf("cannot assigne %v to %v", val.Type(), structFieldType)
	}

	structFieldValue.Set(val)
	return nil
}

// Employees is ...
type Employees []*Employee

// EmplyeesFilterOptions is ...
type EmplyeesFilterOptions func(employee *Employee) bool

// FilterBy is ...
func (emps Employees) FilterBy(filterOption ...EmplyeesFilterOptions) Employees {
	for i := 0; i < len(emps); i++ {
		emp := emps[i]
		isValid := true

		for _, filter := range filterOption {
			if !filter(emp) {
				isValid = false
				break
			}
		}

		if !isValid {
			emps = append(emps[:i], emps[i+1:]...)
			i = i - 1
		}
	}
	return emps
}

// GroupByNation is a function responsible for group employee by nation
func (emps Employees) GroupByNation() map[string]Employees {
	groupByNation := make(map[string]Employees)
	for i := 0; i < len(emps); i++ {
		emp := emps[i]
		if _, exist := groupByNation[emp.NATIONALITY]; !exist {
			groupByNation[emp.NATIONALITY] = make([]*Employee, 0)
		}
		groupByNation[emp.NATIONALITY] = append(groupByNation[emp.NATIONALITY], emp)
	}
	return groupByNation
}

func IsOnlyPosition(emp *Employee) bool {
	positions := []string{"Airhostess", "Pilot", "Steward"}
	for _, position := range positions {
		if position == emp.POSITION {
			return true
		}
	}
	return false
}

func IsActiveStatus(emp *Employee) bool {
	if emp.STATUS != 1 {
		return false
	}
	return true
}

func IsValidStatus(emp *Employee) bool {
	if emp.STATUS != 1 && emp.STATUS != 2 && emp.STATUS != 3 {
		return false
	}
	return true
}

func IsValidGender(emp *Employee) bool {
	if emp.GENDER != 0 && emp.GENDER != 1 {
		return false
	}
	return true
}

func IsExpMoreThanThree(emp *Employee) bool {
	date := emp.HIRED
	date = time.Time{}.Add(time.Now().Sub(date))
	if date.Year() < 3 {
		return false
	}
	return true
}
