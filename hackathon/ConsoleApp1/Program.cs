using System;
using System.Collections.Generic;
using System.Data.Entity.Infrastructure;
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
                            string path = "", output = "";
                            Console.WriteLine("please enter your xml file path");
                            path = Console.ReadLine();
                            //for test : ../../../../data-devclub-1.xml
                            Console.WriteLine("please enter your output file path");
                            output = Console.ReadLine();
                            //for test : ../../../../resultFile/data-devclub-1
                            List<Employees> employee = GlobalFunction.XmlToCsv(path, output);
                            Console.WriteLine("success");
                        }
                        else if (menuSelect == 3)
                        {
                            string pathFile = "", output = "";
                            Console.Write("please enter your csv file path");
                            // ../../../../resultFile/data-devclub-1.csv
                            pathFile = Console.ReadLine();
                            Console.WriteLine("please enter your output file path");
                            output = Console.ReadLine();
                            // ../../../../resultFile/data-devclub-1
                            List<Employees> employee = GlobalFunction.XmlToCsv(pathFile, output);
                            Console.WriteLine("success");
                        }
                        else if (menuSelect == 4)
                        {
                            string path = "", output = "";
                            Console.WriteLine("we need DevMountain csv file please enter path csv file");
                            path = Console.ReadLine();
                            // ../../../../resultFile/data-devclub-1.csv
                            List<Employees> employee = GlobalFunction.csvToXml(path, output);
                            List<Employees> devMoutrain = new List<Employees>();
                            foreach (var emp in employee)
                            {
                                // filter data 
                                if (emp.empStatus == "1" && (emp.empPosition == "Pilot" || emp.empPosition == "Steward" || emp.empPosition == "Airhostess"))
                                {
                                    string[] year = emp.empHired.Split('-');
                                    if (2022 - Convert.ToInt32(year[2]) >= 3)
                                    {
                                        devMoutrain.Add(emp);
                                    }
                                }
                            }
                            //dev club getdata 
                            List<Employees> devClub = sqlite.getData("select * from dev_club;");
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
                                    delDevClub.Add(emp);
                                }
                            }

                            List<Employees> dataSender = new List<Employees>();
                            foreach (var moutrain in devMoutrain)
                            {
                                bool add = true;
                                foreach (var club in devClubFilter)
                                {
                                    if ((moutrain.empId == club.empId) || (moutrain.passPort == club.passPort))
                                    {
                                        add = false;
                                    }
                                }
                                if (add)
                                {
                                    dataSender.Add(moutrain);
                                }
                                else
                                {
                                    delDevClub.Add(moutrain);
                                }
                            }
                            // migration data 2 data base
                            sqlite.romoveData(delDevClub);
                            sqlite.insertData(dataSender);
                            Console.WriteLine("success");
                        }
                        else if (menuSelect == 5)
                        {
                            string path = "", output = "";
                            Console.WriteLine("we need csv file for split please enter file path");

                            // ../../../../resultFile/data-devclub-1.csv

                            path = Console.ReadLine();
                            List<Employees> employee = GlobalFunction.csvToXml(path, output);
                            string nations = "";
                            nations += employee[0].empNationality.ToString().Trim();
                            foreach (var emp in employee)
                            {
                                bool add = true;
                                string[] nation = nations.Split('-');
                                for (int idx = 0; idx < nation.Length; idx++)
                                {
                                    if (emp.empNationality.Trim() == nation[idx].Trim())
                                    {
                                        add = false;
                                    }
                                }
                                if (add)
                                {
                                    nations += "-" + emp.empNationality.ToString().Trim();
                                }
                            }
                            string[] nationality = nations.Split('-');
                            foreach (var nation in nationality)
                            {
                                List<Employees> nationCsv = new List<Employees>();
                                foreach (var emp in employee)
                                {
                                    if (emp.empNationality == nation)
                                    {
                                        nationCsv.Add(emp);
                                    }
                                    GlobalFunction.genarateCsvFormat(nationCsv, "../../../../resultFile/nationality/employees_" + nation);
                                }
                            }
                            Console.WriteLine("success");
                        }
                        else if (menuSelect == 6)
                        {
                            Console.WriteLine("what database your want to create jsonfile");
                            Console.WriteLine("1. dev Club 2.dev Mountrain");
                            string choice = Console.ReadLine();
                            if (choice == "1" || choice == "2")
                            {
                                string selectCmd = "";
                                if(choice == "1")
                                {
                                    selectCmd += "select * from dev_club";
                                }
                                else
                                {
                                    selectCmd += "select * from dev_mountain";
                                }

                                List<Employees> employee = sqlite.getData(selectCmd);
                                Console.WriteLine("output path and filename: ");
                                // ../../../../resultFile/resultJson
                                string output = Console.ReadLine();
                                GlobalFunction.getJsonFile(employee, output);
                            }
                            else
                            {
                                Console.WriteLine("wrong choice");
                            }
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
