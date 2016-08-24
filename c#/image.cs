using System;
using System.Drawing;
using System.Windows.Forms;
 
namespace MyFrmApp
{
    public class MyForm : Form
    {
             
        public MyForm()
        {
            this.Width = 300;
            this.Height = 200;
            this.Paint += myframe_paint;
        }
             
        private void myframe_paint(object sender, PaintEventArgs e)
        {
			Graphics g = e.Graphics;
			Image img = Image.FromFile("sample.jpg");
		    g.DrawImage(img,25,25,100,100);
		    g.DrawImage(img,125,125,100,100);

        }

        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());
		}
	}
}
