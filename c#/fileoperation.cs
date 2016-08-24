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
            this.Width = 500;
            this.Height = 500;
            setupControls();
        }
        public void setupControls()
        {
            label = new Label();
            label.Text = "type text:";
            label.Font = new Font("Geneva",12,FontStyle.Regular);
            label.Height = 30;
            label.Width = 500;
            this.Controls.Add(label);
            box = new TextBox();
            box.Multiline = true;
            box.Width = 425;
            box.Height = 300;
            box.Top = 50;
            box.Left = 25;
            this.Controls.Add(box);
            btn = new Button();
            btn.Text = "click";
            btn.Height = 30;
            btn.Width = 100;
            btn.Top = 360;
            btn.Left = 100;
            btn.Click += btn_Click;
            this.Controls.Add(btn);
        }
          
        private void btn_Click(object sender, System.EventArgs e)
        {
                string doc = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
                string dtop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
                string[] files = Directory.GetFiles(doc);
                string bk = dtop + Path.DirectorySeparatorChar + "Backup!";
                Directory.CreateDirectory(bk);
                foreach(string file in files)
                {
                    string fname = Path.GetFileName(file);
                    File.Copy(file, bk + Path.DirectorySeparatorChar + fname);
                    box.Text += fname + Environment.NewLine;
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
