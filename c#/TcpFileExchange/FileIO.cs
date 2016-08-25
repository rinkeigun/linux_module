using System;
using System.IO;

namespace TcpFileExchange
{
	/// <summary>
	/// �t�@�C�����o�C�i���œǂݏ������邽�߂̃N���X
	/// </summary>
	public class FileIO
	{
		//�t�@�C�����o�C�i���`���œǂݍ���
		public static Byte[] ReadFile(string filename)
		{
			FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
			Byte[] data = new Byte[fs.Length];

			int offset=0;
			int remaining = data.Length;

			while (remaining > 0)
			{
				int read = fs.Read(data, offset, remaining);
				remaining -= read;
				offset += read;
			}

			fs.Close();

			return data;
		}

		//�t�@�C�����o�C�i���`���ŏ�������
		public static void WriteFile(string filename, Byte[] data)
		{
			FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
			fs.Write(data, 0, data.Length);
			fs.Flush();
			fs.Close();
		}
	}
}
