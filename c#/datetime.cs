using System;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            DateTime d1 = DateTime.Parse("1543�N12��6�� 01:23:45 AM");
            DateTime d2 = new DateTime(2001,1,1);
            Console.WriteLine(d1.Year + "�N" + d1.Month + "��" + d1.Day + "��");
            Console.WriteLine(d2.ToString("yyyy-MM-dd(ddd)"));
            Console.ReadKey(true);
        }
    }
}



