using System;
using System.Text;

namespace TcpFileExchange
{
	/// <summary>
	/// ファイル転送のために定義したプロトコルに基づいてデータをエンコード/デコードするクラス
	/// データの形式は
	/// [filename]?[BASE64でエンコードされたファイルの中身]
	/// のように?で区切られた２つの文字列
	/// </summary>
	public class ProtocolEncoder
	{
		//セパレータを?と定義
		//?はBASE64に使われないため
		private const char Separator = '?';

		//受け取ったデータからファイル名を取り出す
		public static string GetFileNameFromStreamText(string data)
		{
			string[] partString = data.Split(new char[]{Separator});

			return partString[0];
		}

		//受け取ったデータからファイルの中身のデータを取り出す
		public static Byte[] GetDataFromStreamText(string data)
		{
			string[] partString = data.Split(new char[]{Separator});

			return Convert.FromBase64String(partString[1]);
		}

		//ファイル名とファイルの中身からデータ文字列を作成する
		public static string ToBase64EncodedData(string filename, Byte[] data)
		{
			return filename + "?" + Convert.ToBase64String(data); 
		}
	}
}
