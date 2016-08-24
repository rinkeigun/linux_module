/*
	2016/08/24 Huiqun.Lin
	c:\Windows\Microsoft.NET\Framework\v4.0.30319\csc MyFrmApp.cs
*/

using System;
//using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
 
namespace MyFrmApp
{



    public class MyForm : Form
    {
        public MyForm()
        {
            Label label = new Label();
            label.Text = "Welcome to C#!";
            label.Font = new Font("Geneva",18,FontStyle.Regular);
            label.Height = 30;
            label.Width = 300;
            this.Controls.Add(label);
            this.Width = 300;
            this.Height = 200;
        }
        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());

		}
    }
}
