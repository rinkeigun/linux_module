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
        ComboBox combo;
         
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
            combo = new ComboBox();
            combo.Items.Add("Windows");
            combo.Items.Add("Mac OS X");
            combo.Items.Add("Linux");
            combo.Width = 100;
            combo.Height = 25;
            combo.Left = 50;
            combo.Top = 50;
            combo.SelectedValueChanged += combo_changed;
            combo.TextChanged += combo_changed;
            this.Controls.Add(combo);
        }
         
        private void combo_changed(object sender, System.EventArgs e)
        {
            int n = combo.SelectedIndex;
            string str = combo.Text;
            label.Text = "selected: " + n + " (" + str + ")";
        }




        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());

		}
    }
}
