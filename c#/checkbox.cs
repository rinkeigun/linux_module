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
        private Label label;
        CheckBox check;
         
        public MyForm()
        {
            this.Width = 300;
            this.Height = 200;
            setupControls();
        }
         
        public void setupControls()
        {
            label = new Label();
            label.Text = "type text:";
            label.Font = new Font("Geneva",12,FontStyle.Regular);
            label.Height = 30;
            label.Width = 300;
            this.Controls.Add(label);
            check = new CheckBox();
            check.Text = "check box";
            check.Top = 50;
            check.Left = 50;
            check.CheckedChanged += check_changed;
            this.Controls.Add(check);
        }
         
        private void check_changed(object sender, System.EventArgs e)
        {
             label.Text = "checked: " + check.CheckState + "(" + check.Checked + ")";
        }


        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());

		}
    }
}
