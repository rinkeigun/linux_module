using System;

public class Server
{
    public static void Main()
    {
        //Listen����IP�A�h���X
        string ipString = "127.0.0.1";
        System.Net.IPAddress ipAdd = System.Net.IPAddress.Parse(ipString);

        //�z�X�g������IP�A�h���X���擾���鎞�́A���̂悤�ɂ���
        //string host = "localhost";
        //System.Net.IPAddress ipAdd =
        //    System.Net.Dns.GetHostEntry(host).AddressList[0];
        //.NET Framework 1.1�ȑO�ł́A�ȉ��̂悤�ɂ���
        //System.Net.IPAddress ipAdd =
        //    System.Net.Dns.Resolve(host).AddressList[0];

        //Listen����|�[�g�ԍ�
        int port = 2001;

        //TcpListener�I�u�W�F�N�g���쐬����
        System.Net.Sockets.TcpListener listener =
            new System.Net.Sockets.TcpListener(ipAdd, port);

        //Listen���J�n����
        listener.Start();
        Console.WriteLine("Listen���J�n���܂���({0}:{1})�B",
            ((System.Net.IPEndPoint)listener.LocalEndpoint).Address,
            ((System.Net.IPEndPoint)listener.LocalEndpoint).Port);

while(true)
{
        //�ڑ��v������������󂯓����
        System.Net.Sockets.TcpClient client = listener.AcceptTcpClient();
        Console.WriteLine("�N���C�A���g({0}:{1})�Ɛڑ����܂����B",
            ((System.Net.IPEndPoint)client.Client.RemoteEndPoint).Address,
            ((System.Net.IPEndPoint)client.Client.RemoteEndPoint).Port);

        //NetworkStream���擾
        System.Net.Sockets.NetworkStream ns = client.GetStream();

        //�ǂݎ��A�������݂̃^�C���A�E�g��10�b�ɂ���
        //�f�t�H���g��Infinite�ŁA�^�C���A�E�g���Ȃ�
        //(.NET Framework 2.0�ȏオ�K�v)
        ns.ReadTimeout = 10000;
        ns.WriteTimeout = 10000;

        //�N���C�A���g���瑗��ꂽ�f�[�^����M����
        System.Text.Encoding enc = System.Text.Encoding.UTF8;
        bool disconnected = false;
        System.IO.MemoryStream ms = new System.IO.MemoryStream();
        byte[] resBytes = new byte[256];
        int resSize = 0;
        do
        {
            //�f�[�^�̈ꕔ����M����
            resSize = ns.Read(resBytes, 0, resBytes.Length);
            //Read��0��Ԃ������̓N���C�A���g���ؒf�����Ɣ��f
            if (resSize == 0)
            {
                disconnected = true;
                Console.WriteLine("�N���C�A���g���ؒf���܂����B");
                break;
            }
            //��M�����f�[�^��~�ς���
            ms.Write(resBytes, 0, resSize);
            //�܂��ǂݎ���f�[�^�����邩�A�f�[�^�̍Ōオ\n�łȂ����́A
            // ��M�𑱂���
        } while (ns.DataAvailable || resBytes[resSize - 1] != '\n');
        //��M�����f�[�^�𕶎���ɕϊ�
        string resMsg = enc.GetString(ms.GetBuffer(), 0, (int)ms.Length);
        ms.Close();
        //������\n���폜
        resMsg = resMsg.TrimEnd('\n');
        Console.WriteLine(resMsg);

        if (!disconnected)
        {
            //�N���C�A���g�Ƀf�[�^�𑗐M����
            //�N���C�A���g�ɑ��M���镶������쐬
            string sendMsg = resMsg.Length.ToString();
            //�������Byte�^�z��ɕϊ�
            byte[] sendBytes = enc.GetBytes(sendMsg + '\n');
            //�f�[�^�𑗐M����
            ns.Write(sendBytes, 0, sendBytes.Length);
            Console.WriteLine(sendMsg);
        }

        //����
        ns.Close();
        client.Close();
        Console.WriteLine("�N���C�A���g�Ƃ̐ڑ�����܂����B");
}
// ���̃R�[�h�͎��s����Ȃ��H

        //���X�i�����
        listener.Stop();
        Console.WriteLine("Listener����܂����B");

        Console.ReadLine();
    }
}
