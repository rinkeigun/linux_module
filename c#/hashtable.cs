using System;
using System.Collections;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            Hashtable table = new Hashtable();
            table.Add("taro","taro@yamada.com");
            table.Add("hanako","hanako@flower.com");
            table.Add("tuyano","tuyano@syoda.com");
            table["tuyano"] = "syoda@tuyao.com";
            Console.WriteLine(table["tuyano"]);
            Console.WriteLine(table["hanako"]);
            Console.ReadKey(true);
        }
    }
}
