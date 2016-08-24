using System;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            DateTime d1 = DateTime.Parse("1543”N12ŒŽ6“ú 01:23:45 AM");
            DateTime d2 = new DateTime(2001,1,1);
            Console.WriteLine(d1.Year + "”N" + d1.Month + "ŒŽ" + d1.Day + "“ú");
            Console.WriteLine(d2.ToString("yyyy-MM-dd(ddd)"));
            Console.ReadKey(true);
        }
    }
}



