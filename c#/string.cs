using System;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
             
            string s1 = "Hello! Welcome to C# World!";
            Console.WriteLine("s1:" + s1);
            Console.Write("s2:");
            string s2 = Console.ReadLine();
            // s1��s2�Ŏn�܂邩�H
            Console.WriteLine(s1.StartsWith(s2));
            // s1�̂ق���s2���傫�����H
            Console.WriteLine(s1.CompareTo(s2));
            // s1�̉������ڂ�s2�����邩�H
            Console.WriteLine(s1.IndexOf(s2));
            Console.ReadKey(true);
        }
    }
}

