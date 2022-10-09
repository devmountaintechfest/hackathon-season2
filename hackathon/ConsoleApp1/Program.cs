using System;
using System.Collections.Generic;
using System.IO;
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
                "tranfer data DevMountain to DevClub",
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
                            
                            List<Employees> dataSender = new List<Employees>();
                            foreach (var emp in employee)
                            {
                                // filter data 
                                if (emp.empStatus == "1" && (emp.empPosition == "Pilot"|| emp.empPosition == "Steward" || emp.empPosition == "Airhostess"))
                                {
                                    string[] year = emp.empHired.Split('-');
                                    if (2022 - Convert.ToInt32(year[2]) >= 3)
                                    {
                                        dataSender.Add(emp);
                                    }
                                }
                            }
                            GlobalFunction.genarateCsvFormat(dataSender,"../../../../dataDevclub");
                        }
                    }
                    else if (menuSelect == 5)
                    {
                        string path = "", output = "";
                        Console.WriteLine("we need csv file for split please enter file path");
                        // ../../../../data-devclub-1.csv
                        path = Console.ReadLine();
                        List<Employees> employee = GlobalFunction.XmlToCsv(path, output);
                        GlobalFunction.csvToXml(path, "../../../../dataDevclub.csv");

                    }
                    else
                    {
                        Console.WriteLine("don't match please try again\n");
                    }
                }
                catch (Exception)
                {
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
