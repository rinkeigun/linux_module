using System;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            string s1 = "Hello! Welcome to C# World!";
            Console.WriteLine("s:" + s1);
            string[] arr = s1.Split(' ');
            Console.WriteLine(arr);
            string s2 = String.Join("-",arr);
            Console.WriteLine(s2);
            string s3 = s2.Remove(10);
            Console.WriteLine(s3);
            Console.ReadKey(true);
        }
    }
}


