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
        RadioButton radio1, radio2;
         
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
            GroupBox group = new GroupBox();
            group.Width = 200;
            group.Height = 100;
            group.Top = 50;
            group.Left = 50;
            group.Text = "radio group";
            this.Controls.Add(group);
            radio1 = new RadioButton();
            radio1.Text = "male";
            radio1.Top = 25;
            radio1.Left = 25;
            radio1.Checked = true;
            radio1.CheckedChanged += check_changed;
            group.Controls.Add(radio1);
            radio2 = new RadioButton();
            radio2.Text = "fimale";
            radio2.Top = 50;
            radio2.Left = 25;
            radio2.CheckedChanged += check_changed;
            group.Controls.Add(radio2);
        }
         
        private void check_changed(object sender, System.EventArgs e)
        {
            RadioButton btn = (RadioButton)sender;
            label.Text = "selected: " + btn.Text;
        }



        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());

		}
    }
}
