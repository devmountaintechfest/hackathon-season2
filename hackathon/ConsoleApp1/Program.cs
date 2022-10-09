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
            string pathFile = "";
            /* string pathFile = @"D:/DevClubData.xml";*/
            Console.Write("enter url xml file");
            pathFile = Console.ReadLine();
            List<Employees> employee = GlobalFunction.XmlToCsv(pathFile);
            foreach (var emp in employee)
            {
                Console.WriteLine(emp.ToString());
            }
            //List<Employees> employeeXml = GlobalFunction.csvToXml("../../DefaultDevMountainData.csv");
            Console.ReadLine();
        }
        
    }
}
