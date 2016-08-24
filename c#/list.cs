using System;
using System.Collections.Generic;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            List<string> list = new List<string>();
            list.Add("One");
            list.Add("Two");
            list.Add("Three");
            list[0] = "Zero";
            foreach(String str in list){
                Console.WriteLine(str);
            }
            Console.ReadKey(true);
        }
    }
}
