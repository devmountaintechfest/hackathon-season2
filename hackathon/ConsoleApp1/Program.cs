using System;
using System.Collections.Generic;
using System.IO;
using ConsoleApp1.modules.Functions;
using ConsoleApp1.modules.module;
namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool stop = false;
            string[] cmd =
            {
                "Stop program",
                "Convert Xml To CSV",
                "Convert Csv To Xml",
                "tranfer data DevMountain to DevClub (csv to db)",
                "split csv with nationallity",
                "get json file"
            };
            string menu = "";
            while (!stop)
            {
                for (int idx = 0; idx< cmd.Length;idx++)
                {
                    Console.WriteLine((idx+1) + " : "+ cmd[idx]);
                }
                Console.WriteLine("please select manu:");
                menu = Console.ReadLine();
                try
                {
                    int menuSelect = Convert.ToInt32(menu);
                    if (menuSelect <= cmd.Length)
                    {
                       
                        if (menuSelect == 1)
                        {
                             stop = true;
                             Console.WriteLine("Good bye");
                        }
                        else if (menuSelect == 2)
                        {
                            string path = "",output="";
                            Console.WriteLine("please enter your xml file path");
                            path = Console.ReadLine();
                            //for test : ../../../../data-devclub-1.xml
                            Console.WriteLine("please enter your output file path");
                            output = Console.ReadLine();
                            //for test : ../../../../data-devclub-1
                            List<Employees> employee = GlobalFunction.XmlToCsv(path,output);
                            Console.WriteLine("success");
                        }
                        else if (menuSelect == 3)
                        {
                            string pathFile = "", output = "";
                            Console.Write("please enter your csv file path");
                            // ../../../../data-devclub-1
                            pathFile = Console.ReadLine();
                            Console.WriteLine("please enter your output file path");
                            output = Console.ReadLine();
                            // ../../../../data-devclub-1
                            List<Employees> employee = GlobalFunction.XmlToCsv(pathFile,output);
                            Console.WriteLine("success");
                        }
                        else if (menuSelect == 4)
                        {
                            string path = "", output = "";
                            Console.WriteLine("we need DevMountain csv file please enter path csv file");
                            path = Console.ReadLine();
                            // ../../../../data-devclub-1.csv
                            List<Employees> employee = GlobalFunction.csvToXml(path, output);
                            List<Employees> devMoutrain = new List<Employees>();
                            foreach (var emp in employee)
                            {
                                // filter data 
                                if (emp.empStatus == "1" && (emp.empPosition == "Pilot"|| emp.empPosition == "Steward" || emp.empPosition == "Airhostess"))
                                {
                                    string[] year = emp.empHired.Split('-');
                                    if (2022 - Convert.ToInt32(year[2]) >= 3)
                                    {
                                        devMoutrain.Add(emp);
                                    }
                                }
                            }
                            //dev club getdata 
                            List<Employees> devClub =  sqlite.getData("select * from dev_club;");
                            List<Employees> delDevClub = new List<Employees>();
                            List<Employees> devClubFilter = new List<Employees>();
                            foreach (var emp in devClub)
                            {
                                // filter data 
                                if (emp.empStatus == "1")
                                {
                                    devClubFilter.Add(emp);
                                }
                                else
                                {
                                    Console.WriteLine("dwed");
                                    delDevClub.Add(emp);
                                }
                            }
                           
                            List<Employees> dataSender = new List<Employees>();
                            foreach (var moutrain in devMoutrain)
                            {
                                foreach (var club in devClubFilter)
                                {
                                    if ((moutrain.empId != club.empId) && (moutrain.passPort != club.passPort))
                                    {

                                        dataSender.Add(moutrain);
                                    }
                                    else
                                    {
                                        Console.WriteLine("dwed");
                                        delDevClub.Add(moutrain);
                                    }
                                }
                            }

                            sqlite.romoveData(delDevClub);

                            foreach (var item in delDevClub)
                            {
                                Console.WriteLine(item.empId);
                            }
                            // migration data 2 data base 
                            // GlobalFunction.genarateCsvFormat(dataSender,"../../../../dataDevclub");
                            // send to db
                            Console.WriteLine("success");
                        }
                        else if (menuSelect == 5)
                        {
                            string path = "", output = "";
                            Console.WriteLine("we need csv file for split please enter file path");

                            // ../../../../data-devclub-1.csv

                            path = Console.ReadLine();
                            List<Employees> employee = GlobalFunction.csvToXml(path, output);
                            string nations = "";
                            nations += employee[0].empNationality.ToString().Trim();
                            foreach (var emp in employee)
                            {
                                bool add = true;
                                string[] nation = nations.Split('-');
                                for (int idx = 0;idx < nation.Length;idx++)
                                {
                                    if (emp.empNationality.Trim() == nation[idx].Trim())
                                    { 
                                        add = false;
                                    }
                                }
                                if (add)
                                {
                                    nations += "-"+emp.empNationality.ToString().Trim();
                                }
                            }
                            string[] nationality = nations.Split('-');
                            foreach (var nation in nationality)
                            {
                                List<Employees> nationCsv = new List<Employees>();
                                foreach (var emp in employee)
                                {
                                    if(emp.empNationality == nation)
                                    {
                                        nationCsv.Add(emp);
                                        /*employee.Remove(emp);*/
                                    }
                                    GlobalFunction.genarateCsvFormat(nationCsv,"../../../../employees_"+ nation);
                                }
                            }
                            Console.WriteLine("success");
                        }
                    }
                    
                    else
                    {
                        Console.WriteLine("don't match please try again\n");
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                    Console.WriteLine("something what wrong error!!\n");
                }  
                
            }
            Console.ReadLine();
        }
        
    }
}
