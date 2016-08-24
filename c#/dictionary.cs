using System;
using System.Collections.Generic;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            Dictionary<string,string> dict = new Dictionary<string,string>();
            dict.Add("taro","taro@yamada.com");
            dict.Add("hanako","hanako@flower.com");
            dict.Add("tuyano","tuyano@syoda.com");
            dict["tuyano"] = "syoda@tuyao.com";
            Console.WriteLine(dict["tuyano"]);
            Console.WriteLine(dict["hanako"]);
            Console.ReadKey(true);
        }
    }
}
