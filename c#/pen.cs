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
            Pen p = new Pen(Color.Red);
            Brush b = new SolidBrush(Color.Blue);
            g.FillRectangle(b,50,50,50,50);
            g.DrawEllipse(p,75,75,50,50);
        }

        
		[STAThread]
		public static void Main()
		{
		  Application.EnableVisualStyles();
		  Application.Run(new MyForm());
		}
	}
}
