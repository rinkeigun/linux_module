using System;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            DateTime d1 = DateTime.Parse("1543年12月6日 01:23:45 AM");
            DateTime d2 = new DateTime(2001,1,1);
            Console.WriteLine(d1.Year + "年" + d1.Month + "月" + d1.Day + "日");
            Console.WriteLine(d2.ToString("yyyy-MM-dd(ddd)"));
            Console.ReadKey(true);
        }
    }
}



