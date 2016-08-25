using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.IO;

namespace TcpFileExchange
{
	/// <summary>
	/// Summary description for Form1.
	/// </summary>
	public class FormMain : System.Windows.Forms.Form
	{
		private System.Windows.Forms.TextBox textBoxIPAddress;
		private System.Windows.Forms.Button buttonConnect;
		private System.Windows.Forms.TextBox textBoxReceivedMessage;
		private System.Windows.Forms.Button buttonSend;

		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.Container components = null;

		//ユーザ定義メンバ変数
		private TcpListener listener = null;

		//クライアント側のストリーム
		private StreamWriter clientWriter = null;
		private StreamReader clientReader = null;

		//サーバ側のストリーム
		private StreamWriter serverWriter = null;
		private StreamReader serverReader = null;

		//サーバスレッド
		Thread threadServer = null;

		//クライアントスレッド
		Thread threadClient = null;

		private System.Windows.Forms.OpenFileDialog openFileDialog1;
		private System.Windows.Forms.TextBox textBoxFileName;
		private System.Windows.Forms.Button buttonOpen;

		//ポート番号は9999に設定
		private Int32 port = 9991;

		public FormMain()
		{
			//
			// Required for Windows Form Designer support
			//
			InitializeComponent();
		}

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.textBoxIPAddress = new System.Windows.Forms.TextBox();
			this.buttonConnect = new System.Windows.Forms.Button();
			this.textBoxReceivedMessage = new System.Windows.Forms.TextBox();
			this.textBoxFileName = new System.Windows.Forms.TextBox();
			this.buttonSend = new System.Windows.Forms.Button();
			this.buttonOpen = new System.Windows.Forms.Button();
			this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
			this.SuspendLayout();
			// 
			// textBoxIPAddress
			// 
			this.textBoxIPAddress.Location = new System.Drawing.Point(16, 16);
			this.textBoxIPAddress.Name = "textBoxIPAddress";
			this.textBoxIPAddress.Size = new System.Drawing.Size(184, 20);
			this.textBoxIPAddress.TabIndex = 0;
			this.textBoxIPAddress.Text = "localhost";
			// 
			// buttonConnect
			// 
			this.buttonConnect.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonConnect.Location = new System.Drawing.Point(204, 16);
			this.buttonConnect.Name = "buttonConnect";
			this.buttonConnect.Size = new System.Drawing.Size(72, 23);
			this.buttonConnect.TabIndex = 1;
			this.buttonConnect.Text = "Connect";
			this.buttonConnect.Click += new System.EventHandler(this.buttonConnect_Click);
			// 
			// textBoxReceivedMessage
			// 
			this.textBoxReceivedMessage.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
				| System.Windows.Forms.AnchorStyles.Left) 
				| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxReceivedMessage.Location = new System.Drawing.Point(16, 164);
			this.textBoxReceivedMessage.Multiline = true;
			this.textBoxReceivedMessage.Name = "textBoxReceivedMessage";
			this.textBoxReceivedMessage.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
			this.textBoxReceivedMessage.Size = new System.Drawing.Size(260, 88);
			this.textBoxReceivedMessage.TabIndex = 2;
			this.textBoxReceivedMessage.Text = "";
			// 
			// textBoxFileName
			// 
			this.textBoxFileName.Location = new System.Drawing.Point(16, 112);
			this.textBoxFileName.Name = "textBoxFileName";
			this.textBoxFileName.Size = new System.Drawing.Size(184, 20);
			this.textBoxFileName.TabIndex = 3;
			this.textBoxFileName.Text = "";
			// 
			// buttonSend
			// 
			this.buttonSend.Enabled = false;
			this.buttonSend.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonSend.Location = new System.Drawing.Point(16, 136);
			this.buttonSend.Name = "buttonSend";
			this.buttonSend.Size = new System.Drawing.Size(260, 23);
			this.buttonSend.TabIndex = 4;
			this.buttonSend.Text = "Send";
			this.buttonSend.Click += new System.EventHandler(this.buttonSend_Click);
			// 
			// buttonOpen
			// 
			this.buttonOpen.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonOpen.Location = new System.Drawing.Point(204, 112);
			this.buttonOpen.Name = "buttonOpen";
			this.buttonOpen.Size = new System.Drawing.Size(72, 23);
			this.buttonOpen.TabIndex = 5;
			this.buttonOpen.Text = "Open";
			this.buttonOpen.Click += new System.EventHandler(this.buttonOpen_Click);
			// 
			// FormMain
			// 
			this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
			this.ClientSize = new System.Drawing.Size(292, 266);
			this.Controls.Add(this.buttonOpen);
			this.Controls.Add(this.buttonSend);
			this.Controls.Add(this.textBoxFileName);
			this.Controls.Add(this.textBoxReceivedMessage);
			this.Controls.Add(this.buttonConnect);
			this.Controls.Add(this.textBoxIPAddress);
			this.Name = "FormMain";
			this.Text = "TcpFileExchange";
			this.Load += new System.EventHandler(this.FormMain_Load);
			this.Closed += new System.EventHandler(this.FormMain_Closed);
			this.ResumeLayout(false);

		}
		#endregion

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main() 
		{
			Application.Run(new FormMain());
		}

		private void FormMain_Load(object sender, System.EventArgs e)
		{
			//サーバとしては自動的にスタート
			ServerStart();
		}

		//サーバをスタート
		private void ServerStart()
		{
			try
			{
				//TcpListenerを使用してサーバーを指定のポートで確立
				listener = new TcpListener(IPAddress.Any, port);
				listener.Start();

				WriteLineMessage("サーバを開始しました。");

				//スレッドとしてクライアントからの通信を処理する部分を実行
				threadServer = new Thread(new ThreadStart(ServerListen));
				threadServer.Start();
			}
			catch (Exception exception)
			{
				WriteLineMessage(exception.Message + "\r\n" + exception.StackTrace);
			}
		}

		//UIとは別スレッドで実行されるサーバ側の処理
		private void ServerListen()
		{
			try
			{
				//クライアントの要求があったら、接続を確立する
				TcpClient server = listener.AcceptTcpClient();

				this.textBoxReceivedMessage.BeginInvoke(new WriteLineMessageHandler(WriteLineMessage), new object[] {"クライアントが接続しました。"});

				this.buttonConnect.Enabled = false;
				this.buttonSend.Enabled = true;

				//クライアントとの間の通信につかうストリームを取得
				NetworkStream ns = server.GetStream();

				serverReader = new StreamReader(ns, Encoding.UTF8);
				serverWriter = new StreamWriter(ns, Encoding.UTF8);

				//クライアントからのデータ送信をループで待機
				//いつデータ送信がきても受信するように
				while (true)
				{
					ProcessMessage(serverReader);
				}
			}
			catch (Exception exception)
			{
				this.textBoxReceivedMessage.BeginInvoke(new WriteLineMessageHandler(WriteLineMessage), new object[] { exception.Message  + "\r\n" + exception.StackTrace});
			}
		}

		//クライアント側で、サーバからのデータ送信を待機する
		private void ClientListen()
		{
			try
			{
				while (true)
				{
					ProcessMessage(clientReader);
				}
			}
			catch (Exception exception)
			{
				this.textBoxReceivedMessage.BeginInvoke(new WriteLineMessageHandler(WriteLineMessage), new object[] { exception.Message  + "\r\n" + exception.StackTrace});
			}
		}

		//受け取ったメッセージを処理する
		//メッセージはProtocolEncodedで決められたプロトコルによってやり取りされる
		private void ProcessMessage(StreamReader reader)
		{
			lock(this)
			{
				string message = reader.ReadLine();

				string fileName = ProtocolEncoder.GetFileNameFromStreamText(message);

				Byte[] data = ProtocolEncoder.GetDataFromStreamText(message);

				FileIO.WriteFile(Application.StartupPath + "\\" + fileName, data);

				this.textBoxReceivedMessage.BeginInvoke(new WriteLineMessageHandler(WriteLineMessage), new object[] {fileName + "を受信しました。"});
			}
		}

		//delegateを宣言して、マルチスレッドでもUIにアクセスできるように。
		delegate void WriteLineMessageHandler(string message);

		//ユーザインターフェイスにメッセージを書き込む
		private void WriteLineMessage(string message)
		{
			this.textBoxReceivedMessage.AppendText(message + "\r\n");
		}

		//クライアントがサーバに接続
		private void buttonConnect_Click(object sender, EventArgs e)
		{
			try
			{
				//クライアントのソケットを用意
				TcpClient client = new TcpClient(this.textBoxIPAddress.Text, port);

				//クライアントがサーバとのデータのやり取りに使うストリームを取得
				NetworkStream ns = client.GetStream();

				clientReader = new StreamReader(ns, Encoding.UTF8);
				clientWriter = new StreamWriter(ns, Encoding.UTF8);

				WriteLineMessage("サーバに接続しました。");

				this.buttonConnect.Enabled = false;
				this.buttonSend.Enabled = true;

				//サーバからのデータを受信するループをスレッドで処理
				threadClient = new Thread(new ThreadStart(this.ClientListen));
				threadClient.Start();
			}
			catch (Exception exception)
			{
				WriteLineMessage(exception.Message + "\r\n" + exception.StackTrace);
			}
		}

		//ファイルを送信する
		//データにはファイル名とBASE64でエンコーディングされたファイルの中身が送信される
		private void buttonSend_Click(object sender, EventArgs e)
		{
			string path = this.textBoxFileName.Text;
			string fileName = Path.GetFileName(path);

			//ファイルの読み込み
			Byte[] data = FileIO.ReadFile(path);

			WriteLineMessage(fileName + "を送信中。");

			try
			{
				//クライアント側なら
				if(clientWriter != null)
				{
					SendMessage(clientWriter, fileName, data);

					WriteLineMessage(fileName + "を送信終了。");
				}

				//サーバーなら
				else if(serverWriter != null)
				{
					SendMessage(serverWriter, fileName, data);

					WriteLineMessage(fileName + "を送信終了。");
				}

				else
				{
					this.WriteLineMessage("サーバもクライアントも立ち上がっていません。");
				}
			}
			catch (Exception exception)
			{
				WriteLineMessage(exception.Message + "\r\n" + exception.StackTrace);
			}
		}

		//データを送るメソッド
		private void SendMessage(StreamWriter writer, string fileName, Byte[] data)
		{
			//設計したプロトコルにしたがってファイル名とファイルのデータをエンコードして送信
			writer.WriteLine(ProtocolEncoder.ToBase64EncodedData(fileName, data));

			//確実にネットワークに流れるようにFlush
			writer.Flush();
		}

		//アプリケーションの終了
		//すべての接続を破棄し、スレッドを終了させる
		private void FormMain_Closed(object sender, System.EventArgs e)
		{
			if(listener != null)
			{
				listener.Stop();
			}

			if(serverReader != null)
			{
				serverReader.BaseStream.Close();
				serverReader.Close();
			}

			if(clientReader != null)
			{
				clientReader.BaseStream.Close();
				clientReader.Close();
			}

			if(serverWriter != null)
			{
				serverWriter.Close();
			}

			if(clientWriter != null)
			{
				clientWriter.Close();
			}

			if (threadClient != null)
			{
				threadClient.Abort();
			}

			if(threadServer != null)
			{
				threadServer.Abort();
			}
		}

		//OPENボタンが押されたときに、ファイルをオープンする
		private void buttonOpen_Click(object sender, System.EventArgs e)
		{
			if(openFileDialog1.ShowDialog() == DialogResult.OK)
			{
				this.textBoxFileName.Text = openFileDialog1.FileName;
			}
		}
	}
}
