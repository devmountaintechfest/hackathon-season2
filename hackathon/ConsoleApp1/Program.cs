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
                "split csv with nationallity"
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
                            Console.WriteLine("please enter your file path");
                            path = Console.ReadLine();
                            //for test : ../../../../data-devclub-1.xml
                            Console.WriteLine("please enter your output file path");
                            output = Console.ReadLine();
                            //for test : ../../../../data-devclub-1
                            List<Employees> employee = GlobalFunction.XmlToCsv(path,output);
                            Console.ReadLine();
                        }
                        else if (menuSelect == 3)
                        {
                            Console.WriteLine("Convert Csv To Xml");
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
                                if (emp.empStatus != "3" )
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
                                foreach (var club in devClubFilter)
                                {
                                    if ((moutrain.empId != club.empId) || (moutrain.passPort != club.passPort))
                                    {

                                        dataSender.Add(moutrain);
                                    }
                                    else
                                    {
                                        delDevClub.Add(moutrain);
                                    }
                                }
                            }
                            foreach (var item in delDevClub)
                            {
                                Console.WriteLine(devClubFilter);
                            }
                            // migration data 2 data base 
                            // GlobalFunction.genarateCsvFormat(dataSender,"../../../../dataDevclub");
                            // send to db
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
                                    if (emp.empNationality.Trim() != nation[idx].Trim())
                                    { 
                                        add = true;
                                    }
                                    else
                                    {
                                        add = false;
                                    }
                                }
                                if (add)
                                {
                                    Console.WriteLine(nations);
                                    Console.WriteLine(emp.empNationality);
                                    nations += "-"+emp.empNationality.ToString().Trim();
                                }
                            }
                          /*  Console.WriteLine(nations);*/
                            Console.WriteLine(nations.Split('-').Length);
                            /* GlobalFunction.csvToXml(path, "../../../../dataDevclub.csv");*/

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
            /* string pathFile = "";
             *//* string pathFile = @"D:/DevClubData.xml";*//*
             Console.Write("enter url xml file");
             pathFile = Console.ReadLine();
             List<Employees> employee = GlobalFunction.XmlToCsv(pathFile);
             foreach (var emp in employee)
             {
                 Console.WriteLine(emp.ToString());
             }
             //List<Employees> employeeXml = GlobalFunction.csvToXml("../../DefaultDevMountainData.csv");
             Console.ReadLine();*/
            Console.ReadLine();
        }
        
    }
}
