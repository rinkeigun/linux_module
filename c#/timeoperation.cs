using System;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            DateTime d1 = DateTime.Parse("1543�N12��6�� 01:23:45 AM");
            DateTime d2 = DateTime.Now;
            TimeSpan s = d2 - d1;
            DateTime d = d2 + s;
            Console.WriteLine("��������" + d1 + "�܂ł́A" + s.Days + "���B");
            Console.WriteLine("��������" + s.Days + "����́A" + 
                              d.ToString("yyyy�NMM��dd���B"));
            Console.ReadKey(true);
        }
    }
}


