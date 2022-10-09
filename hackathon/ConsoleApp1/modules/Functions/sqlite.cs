using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Data.SQLite;
using System.Linq;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
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
        public static void romoveData(string cmd)
        {
            SQLiteConnection conn = new SQLiteConnection("Data Source=database.db; Version=3;New=True;Compress=True;");
            conn.Open();
            SQLiteDataReader sqlite_datareader;
            SQLiteCommand sqlite_cmd;
            sqlite_cmd = conn.CreateCommand();
            sqlite_cmd.CommandText = cmd;
            sqlite_datareader = sqlite_cmd.ExecuteReader();
            while (sqlite_datareader.Read())
            {
                string myreader = sqlite_datareader.GetString(0);
                Console.WriteLine(myreader);
            }
            conn.Close();
        }
        public static void insertData(string cmd)
        {
            SQLiteConnection conn = new SQLiteConnection("Data Source=database.db; Version=3;New=True;Compress=True;");
            conn.Open();
            SQLiteCommand sqlite_cmd;
            sqlite_cmd = conn.CreateCommand();
            sqlite_cmd.CommandText = "INSERT INTO SampleTable (Col1, Col2) VALUES('Test Text ', 1); ";
            sqlite_cmd.ExecuteNonQuery();
            conn.Close();
        }
        public static void updateData(string cmd)
        {
            SQLiteConnection conn = new SQLiteConnection("Data Source=database.db; Version=3;New=True;Compress=True;");
            conn.Open();
            SQLiteDataReader sqlite_datareader;
            SQLiteCommand sqlite_cmd;
            sqlite_cmd = conn.CreateCommand();
            sqlite_cmd.CommandText = cmd;
            sqlite_datareader = sqlite_cmd.ExecuteReader();
            while (sqlite_datareader.Read())
            {
                string myreader = sqlite_datareader.GetString(0);
                Console.WriteLine(myreader);
            }
            conn.Close();
        }

    }
}
