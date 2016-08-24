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
                /*
 �EEnvironment.SpecialFolder�̃t�H���_
ApplicationData�\�\�z�[���f�B���N�g�����́uAppData�v�t�H���_
MyComputer�\�\�u�}�C�R���s���[�^�v
MyDocuments�\�\�u�}�C�h�L�������g�v
MyPictures�\�\�u�}�C�s�N�`���[�v
MyVideos�\�\�u�}�C�r�f�I�v
MyMusic�\�\�u�}�C�~���[�W�b�N�v
Desktop�\�\�f�X�N�g�b�v
ProgramFiles�\�\�uProgram Files�v�t�H���_
Windows�\�\Windows�̃C���X�g�[���t�H���_               
                */
                string[] files = Directory.GetFiles(doc);
                string result = "";
                foreach(string file in files)
                {
                    string fname = Path.GetFileName(file);
                    result += fname + Environment.NewLine;
                }
                box.Text = result;
        }




        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());
		}
	}
}
