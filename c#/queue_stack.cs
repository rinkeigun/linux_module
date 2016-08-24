using System;
using System.Collections.Generic;
 
namespace MyCLIApp
{
    class Program
    {
        public static void Main(string[] args)
        {
            Queue<string> queue = new Queue<string>();
            Stack<string> stack = new Stack<string>();
            queue.Enqueue("One");
            stack.Push("One");
            queue.Enqueue("Two");
            stack.Push("Two");
            queue.Enqueue("Three");
            stack.Push("Thre");
            Console.WriteLine("Queue:");
            foreach(string str in queue){
                Console.Write(str + " ");
            }
            Console.WriteLine();
            Console.WriteLine("Stack:");
            foreach(string str in stack){
                Console.Write(str + " ");
            }
            Console.ReadKey(true);
        }
    }
}
