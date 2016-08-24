using System;
using System.Drawing;
using System.IO;
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
            this.Height = 250;
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
            box.Multiline = true;
            box.Width = 225;
            box.Height = 100;
            box.Top = 50;
            box.Left = 25;
            this.Controls.Add(box);
            btn = new Button();
            btn.Text = "click";
            btn.Height = 30;
            btn.Width = 100;
            btn.Top = 160;
            btn.Left = 100;
            btn.Click += btn_Click;
            this.Controls.Add(btn);
        }
          
        private void btn_Click(object sender, System.EventArgs e)
        {
            using (StreamReader reader = new StreamReader("data.txt"))
            {
                box.Text = reader.ReadToEnd();
            }
        }



        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());
		}
	}
}
