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
        private TextBox box;
        private Button btn;
         
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
            box = new TextBox();
            box.Width = 225;
            box.Top = 50;
            box.Left = 25;
            this.Controls.Add(box);
            btn = new Button();
            btn.Text = "click";
            btn.Height = 30;
            btn.Width = 100;
            btn.Top = 100;
            btn.Left = 100;
            btn.Click += btn_Click;
            this.Controls.Add(btn);
        }
         
        private void btn_Click(object sender, System.EventArgs e)
        {
            string str = box.Text;
            label.Text = "you write'" + str + "'.";
        }

        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());

		}
    }
}
