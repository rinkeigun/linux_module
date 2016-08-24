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
        ListBox list;
         
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
            list = new ListBox();
            list.Width = 100;
            list.Height = 100;
            list.Left = 50;
            list.Top = 50;
            list.SelectionMode = SelectionMode.MultiExtended;
            list.Items.Add("Hello");
            list.Items.Add("Welcome");
            list.Items.Add("Bye!");
            list.SelectedValueChanged += list_changed;
            this.Controls.Add(list);
        }
         
        private void list_changed(object sender, System.EventArgs e)
        {
            string res = "selected: ";
            foreach(string obj in list.SelectedItems)
            {
                res += obj + " ";
            }
            label.Text = res;
        }



        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());

		}
    }
}
