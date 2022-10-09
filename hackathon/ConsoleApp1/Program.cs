using System;
using System.Collections.Generic;
using System.IO;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string pathFile = "";
            /* string pathFile = @"D:/DevClubData.xml";*/
            Console.Write("enter url xml file");
            pathFile = Console.ReadLine();
            List<Employees> employee = XmlToCsv(pathFile);


            foreach (var emp in employee)
            {
                Console.WriteLine(emp.ToString());
            }
            // List<Employees> employeeXml = csvToXml("../../DefaultDevMountainData.csv");

            Console.ReadLine();
        }
        public static List<Employees> csvToXml(string pathFile)
        {
            List<Employees> employees = new List<Employees>();
            List<string> dataReader = new List<string>();
            using (var reader = new StreamReader(pathFile))
            {
                while (!reader.EndOfStream)
                {
                    dataReader.Add(reader.ReadLine());
                }
            }
            foreach (var items in dataReader)
            {
                Employees employee = new Employees();
                string[] dataCsvSplit = items.Split(',');
                employee.empId = dataCsvSplit[0];
                employee.passPort = dataCsvSplit[1];
                employee.empFirstName = dataCsvSplit[2];
                employee.empLastName = dataCsvSplit[3];
                employee.empGender = dataCsvSplit[4];
                employee.empBirthday = dataCsvSplit[5];
                employee.empNationality = dataCsvSplit[6];
                employee.empHired = dataCsvSplit[7];
                employee.empDept = dataCsvSplit[8];
                employee.empPosition = dataCsvSplit[9];
                employee.empStatus = dataCsvSplit[10];
                employee.empRegion = dataCsvSplit[11];
                employees.Add(employee);
            }
            string herder = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n";
            string item = "records>\n";
            string itemrecord = "record>\n";
            string id = "EMPID>";
            string passport = "PASSPORT>";
            string firstname = "FIRSTNAME>";
            string lastname = "LASTNAME>";
            string gender = "GENDER>";
            string birthday = "BIRTHDAY>";
            string nation = "NATIONALITY>";
            string hired = "HIRED>";
            string dept = "DEPT>";
            string position = "POSITION>";
            string status = "STATUS>";
            string region = "REGION>";
            string textXml = herder + "\t<" + item;
            foreach (var data in employees)
            {
                textXml += "\t\t<" + itemrecord;
                textXml += "\t\t\t<" + id + data.empId + "</" + id + "\n";
                textXml += "\t\t\t<" + passport + data.passPort + "</" + passport + "\n";
                textXml += "\t\t\t<" + firstname + data.empFirstName + "atippa" + "</" + firstname + "\n";
                textXml += "\t\t\t<" + lastname + data.empLastName + "</" + lastname + "\n";
                textXml += "\t\t\t<" + gender + data.empGender + "</" + gender + "\n";
                textXml += "\t\t\t<" + birthday + data.empBirthday + "</" + birthday + "\n";
                textXml += "\t\t\t<" + nation + data.empNationality + "</" + nation + "\n";
                textXml += "\t\t\t<" + hired + data.empHired + "</" + hired + "\n";
                textXml += "\t\t\t<" + dept + data.empDept + "</" + dept + "\n";
                textXml += "\t\t\t<" + position + data.empPosition + "</" + position + "\n";
                textXml += "\t\t\t<" + status + data.empStatus + "</" + status + "\n";
                textXml += "\t\t\t<" + region + data.empRegion + "</" + region + "\n";
                textXml += "\t\t</" + itemrecord;
            }
            textXml += "\t</" + item;
            string[] xmldata = textXml.Split('\n');
            File.WriteAllLines("../../xmltest" + ".xml", xmldata);
            Console.WriteLine(textXml);

            return employees;
            /* return dataReader;*/
        }
        public static string genarateCsvFormat(List<Employees> data)
        {
            string[] csvText = new string[100];
            for (int idx = 0; idx < 100; idx++)
            {
                csvText[idx] = data[idx].empId + "," + data[idx].passPort + "," + data[idx].empFirstName + "," + data[idx].empLastName + "," +
                    data[idx].empGender + "," + data[idx].empBirthday + "," + data[idx].empNationality + "," + data[idx].empHired + "," +
                    data[idx].empDept + "," + data[idx].empPosition + "," + data[idx].empStatus + "," + data[idx].empRegion;
            }
            string text = "";
            for (int idx = 0; idx < 100; idx++)
            {
                text += csvText[idx] + "\n";
            }
            writeCsv(csvText, "../../DefaultDevMountainData");
            return text;
        }
        public static void writeCsv(string[] csvData, string fileName)
        {
            File.WriteAllLines(fileName + ".csv", csvData);
        }
        public static List<string> ReadXmlToList(string pathFile)
        {
            List<string> dataReader = new List<string>();
            using (var reader = new StreamReader(pathFile))
            {
                while (!reader.EndOfStream)
                {
                    string text = reader.ReadLine().ToString().Trim();
                    if (text != "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>"
                        && (text != "<records>") && (text != "</records>")
                        && (text != "<record>") &&  (text != "</record>"))
                    {
                        dataReader.Add(text);
                    }
                }
            }
            return dataReader;
        }
        public static List<string[]> FormatList(List<string> ReadData)
        {

            List<string[]> dataSet = new List<string[]>();
            string[] attributeData = new string[12];

            int idx = 1;
            foreach (var item in ReadData)
            {
                // new record
                attributeData[idx - 1] = item;
                if (idx == 12)
                {
                    idx = 1;
                    dataSet.Add(attributeData);
                    attributeData = new string[12];
                }
                else
                {
                    idx++;
                }
            }
            return dataSet;
        }
        public static List<Employees> XmlToCsv(string pathFile)
        {
            List<string> ReadData = ReadXmlToList(pathFile);
            List<string[]> dataSet = FormatList(ReadData);
            List<Employees> employees = formatDataToEmployeeObj(dataSet);
            genarateCsvFormat(employees);
            return employees;
        }
        public static List<Employees> formatDataToEmployeeObj(List<string[]> dataSet)
        {
            List<Employees> employee = new List<Employees>();
            int idx = 0;
            foreach (var item in dataSet)
            {
                idx = 1;
                Employees temp = new Employees();
                foreach (var att in item)
                {
                    string[] dataExtract = att.Split('>');
                    string[] dataValue = dataExtract[1].Split('<');
                    // idx เเทน attribute ของ data ทั้ง 12 ตัว
                    if (idx == 0)
                    {
                        temp.empId = dataValue[0];
                    }
                    else if (idx == 1)
                    {
                        temp.empId = dataValue[0];
                    }
                    else if (idx == 2)
                    {
                        temp.passPort = dataValue[0];
                    }
                    else if (idx == 3)
                    {
                        temp.empFirstName = dataValue[0];
                    }
                    else if (idx == 4)
                    {
                        temp.empLastName = dataValue[0];
                    }
                    else if (idx == 5)
                    {
                        temp.empGender = dataValue[0];
                    }
                    else if (idx == 6)
                    {
                        temp.empBirthday = dataValue[0];
                    }
                    else if (idx == 7)
                    {
                        temp.empNationality = dataValue[0];
                    }
                    else if (idx == 8)
                    {
                        temp.empHired = dataValue[0];
                    }
                    else if (idx == 9)
                    {
                        temp.empDept = dataValue[0];
                    }
                    else if (idx == 10)
                    {
                        temp.empPosition = dataValue[0];
                    }
                    else if (idx == 11)
                    {
                        temp.empStatus = dataValue[0];
                    }
                    else if (idx == 12)
                    {
                        temp.empRegion = dataValue[0];
                    }
                    idx++;
                }
                employee.Add(temp);
            }
            return employee;
        }
    }
}
