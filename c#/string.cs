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
            // s1がs2で始まるか？
            Console.WriteLine(s1.StartsWith(s2));
            // s1のほうがs2より大きいか？
            Console.WriteLine(s1.CompareTo(s2));
            // s1の何文字目にs2があるか？
            Console.WriteLine(s1.IndexOf(s2));
            Console.ReadKey(true);
        }
    }
}

