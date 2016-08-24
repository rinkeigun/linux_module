using System;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            DateTime d1 = DateTime.Parse("1543年12月6日 01:23:45 AM");
            DateTime d2 = DateTime.Now;
            TimeSpan s = d2 - d1;
            DateTime d = d2 + s;
            Console.WriteLine("今日から" + d1 + "までは、" + s.Days + "日。");
            Console.WriteLine("今日から" + s.Days + "日後は、" + 
                              d.ToString("yyyy年MM月dd日。"));
            Console.ReadKey(true);
        }
    }
}


