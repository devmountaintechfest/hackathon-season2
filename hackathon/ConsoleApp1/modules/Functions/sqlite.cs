using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Data.SQLite;
using System.Linq;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace ConsoleApp1.modules.Functions
{
    public static class sqlite
    {
        public static List<Employees> getData(string cmd)
        {
            List<Employees> list = new List<Employees>();
            SQLiteConnection conn = new SQLiteConnection("Data Source=../../database/dataDevMoutrain.db;Version=3;New=True;");
            conn.Open();
            SQLiteDataReader sqlite_datareader;
            SQLiteCommand sqlite_cmd;
            sqlite_cmd = conn.CreateCommand();
            sqlite_cmd.CommandText = cmd;
            sqlite_datareader = sqlite_cmd.ExecuteReader();
            while (sqlite_datareader.Read())
            {
                Employees emp = new Employees();
                emp.empId = sqlite_datareader["emp_id"].ToString();
                emp.passPort = sqlite_datareader["passport"].ToString();
                emp.empFirstName = sqlite_datareader["fname"].ToString();
                emp.empLastName = sqlite_datareader["lname"].ToString();
                emp.empGender = sqlite_datareader["gender"].ToString();
                emp.empBirthday = sqlite_datareader["birthdate"].ToString();
                emp.empLastName = sqlite_datareader["nationality"].ToString();
                emp.empHired = sqlite_datareader["hired"].ToString();
                emp.empDept = sqlite_datareader["dept"].ToString();
                emp.empPosition = sqlite_datareader["position"].ToString();
                emp.empStatus = sqlite_datareader["status"].ToString();
                emp.empRegion = sqlite_datareader["region"].ToString();
                list.Add(emp);
            }
            conn.Close();
            return list;
        }
        public static bool romoveData(List<Employees> listDel)
        {
            SQLiteConnection conn = new SQLiteConnection("Data Source=../../database/dataDevMoutrain.db; Version=3;New=True;Compress=True;");
            conn.Open();
            foreach (var item in listDel)
            {
                Console.WriteLine("delete id :"+ item.empId);
                SQLiteCommand cmd = new SQLiteCommand("DELETE FROM dev_club where dev_club.emp_Id =\""+Convert.ToInt32(item.empId)+"\"", conn);
                cmd.ExecuteNonQuery();
            }
            conn.Close();
            return true;
        }
        public static bool insertData(List<Employees> addlist)
        {

            SQLiteConnection conn = new SQLiteConnection("Data Source=../../database/dataDevMoutrain.db; Version=3;New=True;Compress=True;");
            conn.Open();
            foreach (var item in addlist)
            {
                Console.WriteLine("insert new id :"+ item.empId);
                SQLiteCommand sql_cmd = conn.CreateCommand();
                string cmd = 
                    $"insert into dev_club (emp_id,passport,fname,lname,gender," +
                    $"birthdate,nationality,hired,dept,position,status,region) " +
                    $"values (\"{item.empId}\",\"{item.passPort}\",\"{item.empFirstName}\",\"{item.empLastName}\",\"{item.empGender}\"," +
                    $"\"{item.empBirthday}\",\"{item.empNationality}\",\"{item.empHired}\",\"{item.empDept}\",\"{item.empPosition}\",\"{item.empStatus}\",\"{item.empRegion}\");";
                Console.WriteLine("insert  :" + cmd);

                sql_cmd.CommandText = cmd;
                sql_cmd.ExecuteNonQuery();
            }
            conn.Close();
            return true;

        }

    }
}
