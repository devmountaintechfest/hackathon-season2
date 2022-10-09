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
                "stop program"
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
                for (int idx = 0; idx < cmd.Length; idx++)
                {
                    if (menu == (idx + 1).ToString())
                    {
                        if (cmd[idx] == "stop program")
                        {
                            stop = true;
                            Console.WriteLine("Good bye");
                        }
                        // else if anther menu
                    }
                    else
                    {
                        Console.WriteLine("don't match please try again\n");
                    }  
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
