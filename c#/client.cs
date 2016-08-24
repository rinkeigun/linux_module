using System;

public class Client
{
    public static void Main()
    {
        //�T�[�o�[�ɑ��M����f�[�^����͂��Ă��炤
        Console.WriteLine("���������͂��AEnter�L�[�������Ă��������B");
        string sendMsg = Console.ReadLine();
        //�������͂���Ȃ��������͏I��
        if (sendMsg == null || sendMsg.Length == 0)
        {
            return;
        }

        //�T�[�o�[��IP�A�h���X�i�܂��́A�z�X�g���j�ƃ|�[�g�ԍ�
        string ipOrHost = "127.0.0.1";
        //string ipOrHost = "localhost";
        int port = 2001;

        //TcpClient���쐬���A�T�[�o�[�Ɛڑ�����
        System.Net.Sockets.TcpClient tcp =
            new System.Net.Sockets.TcpClient(ipOrHost, port);
        Console.WriteLine("�T�[�o�[({0}:{1})�Ɛڑ����܂���({2}:{3})�B",
            ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Address,
            ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Port,
            ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Address,
            ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Port);

        //NetworkStream���擾����
        System.Net.Sockets.NetworkStream ns = tcp.GetStream();

        //�ǂݎ��A�������݂̃^�C���A�E�g��10�b�ɂ���
        //�f�t�H���g��Infinite�ŁA�^�C���A�E�g���Ȃ�
        //(.NET Framework 2.0�ȏオ�K�v)
        ns.ReadTimeout = 10000;
        ns.WriteTimeout = 10000;

        //�T�[�o�[�Ƀf�[�^�𑗐M����
        //�������Byte�^�z��ɕϊ�
        System.Text.Encoding enc = System.Text.Encoding.UTF8;
        byte[] sendBytes = enc.GetBytes(sendMsg + '\n');
        //�f�[�^�𑗐M����
        ns.Write(sendBytes, 0, sendBytes.Length);
        Console.WriteLine(sendMsg);

        //�T�[�o�[���瑗��ꂽ�f�[�^����M����
        System.IO.MemoryStream ms = new System.IO.MemoryStream();
        byte[] resBytes = new byte[256];
        int resSize = 0;
        do
        {
            //�f�[�^�̈ꕔ����M����
            resSize = ns.Read(resBytes, 0, resBytes.Length);
            //Read��0��Ԃ������̓T�[�o�[���ؒf�����Ɣ��f
            if (resSize == 0)
            {
                Console.WriteLine("�T�[�o�[���ؒf���܂����B");
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

        //����
        ns.Close();
        tcp.Close();
        Console.WriteLine("�ؒf���܂����B");

        Console.ReadLine();
    }
}
