using System;
using System.Collections;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            ArrayList list = new ArrayList();
            list.Add("One");
            list.Add("Two");
            list.Add("Three");
            list[0] = "Zero";
            foreach(Object obj in list){
                Console.WriteLine(obj);
            }
            Console.ReadKey(true);
        }
    }
}
