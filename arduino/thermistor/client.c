#include "client.h"

int
client(char *data)
{
	struct sockaddr_in server;
	int sock;
	char buf[32];
	int con, n;
	WSADATA wsaData;


	WSAStartup(2 , &wsaData);
 /* �\�P�b�g�̍쐬 */
	sock = socket(AF_INET, SOCK_STREAM, 0);
	printf("sock = %d\n", sock ) ;

 /* �ڑ���w��p�\���̂̏��� */
	server.sin_family = AF_INET;
	server.sin_port = htons(12345);
	server.sin_addr.s_addr = inet_addr("192.168.2.11");

 /* �T�[�o�ɐڑ� */
	con = connect(sock, (struct sockaddr *)&server, sizeof(server));
	if ( con == -1 )
	{
		printf( "�ڑ����s\n" ) ;
	}
	sleep( 3 ) ;
	/* �T�[�o����f�[�^����M */
	//memset(buf, 0, sizeof(buf));
	n = send(sock, data, strlen(data), 0);
	//n = write(sock, buf, sizeof(buf));
	//n = write(sock, data, strlen(data));
	//n = write(sock, 'a', 1);
	if( n == -1 )
	{
		printf( "���M���s\n" ) ;
		printf( "errno:%d\n", errno ) ;
	}
	
	printf("%d, %s\n", n, data);

 /* socket�̏I�� */
	close(sock);
	printf("WSAGetLastError=%d\n", WSAGetLastError());
	printf("WSACleanup = %d\n", WSACleanup());
 return 0;
}

/*
void show_error( int no )
{
	switch( no )
	{
	case E2BIG:

���������X�g�����߂��� (POSIX.1) 

	case EACCES:

�����Ȃ� (POSIX.1) 

	case EADDRINUSE:

�A�h���X�����łɎg�p����Ă��� (POSIX.1) 

	case EADDRNOTAVAIL:

�A�h���X���g�p�ł��Ȃ� (POSIX.1) 

	case EAFNOSUPPORT:

�A�h���X�t�@�~���[���T�|�[�g����Ă��Ȃ� (POSIX.1) 

	case EAGAIN:

���\�[�X���ꎞ�I�ɗ��p�s�� (EWOULDBLOCK �Ɠ����l�ł��悢) (POSIX.1) 

	case EALREADY:

�ڑ������ɏ������ł��� (POSIX.1) 

EBADE:

�s���Ȃ���� (exchange) �ł��� 

EBADF:

�t�@�C���f�B�X�N���v�^�[���s���ł��� (POSIX.1) 

EBADFD:

�t�@�C���f�B�X�N���v�^�[���s���ȏ�Ԃł��� 

EBADMSG:

���b�Z�[�W���s���ł��� (POSIX.1) 

EBADR:

�s���ȃ��N�G�X�g�f�B�X�N���v�^�[ 

EBADRQC:

�s���ȃ��N�G�X�g�R�[�h 

EBADSLT:

�s���ȃX���b�g 

EBUSY:

���\�[�X���g�p���ł��� (POSIX.1) 

ECANCELED:

���삪�L�����Z�����ꂽ (POSIX.1) 

ECHILD:

�q�v���Z�X������ (POSIX.1) 

ECHRNG:

�`�����l���ԍ����͈͊O�ł��� 

ECOMM:

���M���ɒʐM�G���[���������� 

ECONNABORTED:

�ڑ������~���ꂽ (POSIX.1) 

ECONNREFUSED:

�ڑ������ۂ��ꂽ (POSIX.1) 

ECONNRESET:

�ڑ������Z�b�g���ꂽ (POSIX.1) 

EDEADLK:

���\�[�X�̃f�b�h���b�N��������� (POSIX.1) 

EDEADLOCK:

EDEADLK �̓��`�� 

EDESTADDRREQ:

����A�h���X���K�v�ł��� (POSIX.1) 

EDOM:

���w�֐��ň��������̈�O�ł��� (out of domain) 

EDQUOT:

�f�B�X�N�N�H�[�^ (quota) �𒴉߂��� (POSIX.1) 

EEXIST:

�t�@�C�������݂��� (POSIX.1) 

EFAULT:

�A�h���X���s���ł��� (POSIX.1) 

EFBIG:

�t�@�C�����傫�߂��� (POSIX.1) 

EHOSTDOWN:

�z�X�g���_�E�����Ă��� 

EHOSTUNREACH:

�z�X�g�ɓ��B�s�\�ł��� (POSIX.1) 

EIDRM:

���ʎq���폜���ꂽ (POSIX.1) 

EILSEQ:

�s���ȃo�C�g�� (POSIX.1, C99) 

EINPROGRESS:

���삪���s���ł��� (POSIX.1) 

EINTR:

�֐��Ăяo�������荞�܂ꂽ (POSIX.1); signal(7) �Q�ƁB 

EINVAL:

�����������ł��� (POSIX.1) 

EIO:

���o�̓G���[ (POSIX.1) 

EISCONN:

�\�P�b�g���ڑ�����Ă��� (POSIX.1) 

EISDIR:

�f�B���N�g���ł��� (POSIX.1) 

EISNAM:

���O�t���̃t�@�C���ł��� 

EKEYEXPIRED:

���������؂�ƂȂ��� 

EKEYREJECTED:

�����T�[�o�ɂ�苑�ۂ��ꂽ 

EKEYREVOKED:

���������ƂȂ��� 

EL2HLT:

��~ (���x�� 2) 

EL2NSYNC:

�����ł��Ă��Ȃ� (���x�� 2) 

EL3HLT:

��~ (���x�� 3) 

EL3RST:

��~ (���x�� 3) 

ELIBACC:

�K�v�ȋ��L���C�u�����ɃA�N�Z�X�ł��Ȃ����� 

ELIBBAD:

��ꂽ���L���C�u�����ɃA�N�Z�X���悤�Ƃ��� 

ELIBMAX:

�����N���悤�Ƃ������L���C�u���������߂��� 

ELIBSCN:

a.out �̃��C�u�����Z�N�V���������Ă��� (corrupted) 

ELIBEXEC:

���L���C�u�����𒼐ڎ��s�ł��Ȃ����� 

ELOOP:

�V���{���b�N�����N�̉񐔂����߂��� (POSIX.1) 

EMEDIUMTYPE:

�Ԉ�������f�B�A��ʂł��� 

EMFILE:

�I�[�v�����Ă���t�@�C�������߂��� (POSIX.1)�B �ʏ�� getrlimit(2) �ɐ��������郊�\�[�X��� RLIMIT_NOFILE �𒴉߂����ꍇ�ɔ�������B 

EMLINK:

�����N�����߂��� (POSIX.1) 

EMSGSIZE:

���b�Z�[�W�����߂��� (POSIX.1) 

EMULTIHOP:

�}���`�z�b�v (multihop) �����݂� (POSIX.1) 

ENAMETOOLONG:

�t�@�C���������߂��� (POSIX.1) 

ENETDOWN:

�l�b�g���[�N���s�ʂł��� (POSIX.1) 

ENETRESET:

�ڑ����l�b�g���[�N�����璆�~���ꂽ (POSIX.1) 

ENETUNREACH:

�l�b�g���[�N�����B�s�\�ł��� (POSIX.1) 

ENFILE:

�V�X�e���S�̂ŃI�[�v������Ă���t�@�C�������߂��� (POSIX.1) 

ENOBUFS:

�g�p�\�ȃo�b�t�@�[��Ԃ��Ȃ� (POSIX.1 (XSI STREAMS option)) 

ENODATA:

�X�g���[���̓ǂݏo���L���[�̐擪�ɓǂݏo���\�ȃ��b�Z�[�W���Ȃ� (POSIX.1) 

ENODEV:

���̂悤�ȃf�o�C�X�͖��� (POSIX.1) 

ENOENT:

���̂悤�ȃt�@�C����f�B���N�g���͖��� (POSIX.1) 

ENOEXEC:

���s�t�@�C���`���̃G���[ (POSIX.1) 

ENOKEY:

�v�����ꂽ�������p�ł��Ȃ� 

ENOLCK:

���p�ł��郍�b�N������ (POSIX.1) 

ENOLINK:

�����N���؂�Ă��� (POSIX.1) 

ENOMEDIUM:

���f�B�A��������Ȃ� 

ENOMEM:

�\���ȋ󂫃������[�̈悪���� (POSIX.1) 

ENOMSG:

�v�����ꂽ�^�̃��b�Z�[�W�����݂��Ȃ� (POSIX.1) 

ENONET:

�}�V�����l�b�g���[�N��ɂȂ� 

ENOPKG:

�p�b�P�[�W���C���X�g�[������Ă��Ȃ� 

ENOPROTOOPT:

�w�肳�ꂽ�v���g�R�������p�ł��Ȃ� (POSIX.1) 

ENOSPC:

�f�o�C�X�ɋ󂫗̈悪���� (POSIX.1) 

ENOSR:

�w�肳�ꂽ�X�g���[�����\�[�X�����݂��Ȃ� (POSIX.1 (XSI STREAMS option)) 

ENOSTR:

�X�g���[���ł͂Ȃ� (POSIX.1 (XSI STREAMS option)) 

ENOSYS:

�֐�����������Ă��Ȃ� (POSIX.1) 

ENOTBLK:

�u���b�N�f�o�C�X���K�v�ł��� 

ENOTCONN:

�\�P�b�g���ڑ�����Ă��Ȃ� (POSIX.1) 

ENOTDIR:

�f�B���N�g���ł͂Ȃ� (POSIX.1) 

ENOTEMPTY:

�f�B���N�g������ł͂Ȃ� (POSIX.1) 

ENOTSOCK:

�\�P�b�g�ł͂Ȃ� (POSIX.1) 

ENOTSUP:

���삪�T�|�[�g����Ă��Ȃ� (POSIX.1) 

ENOTTY:

I/O ���䑀�삪�K�؂łȂ� (POSIX.1) 

ENOTUNIQ:

���O���l�b�g���[�N�ň�ӂł͂Ȃ� 

ENXIO:

���̂悤�ȃf�o�C�X��A�h���X�͂Ȃ� (POSIX.1) 

EOPNOTSUPP:

�\�P�b�g�ŃT�|�[�g���Ă��Ȃ�����ł��� (POSIX.1) 
(Linux �ł� ENOTSUP �� EOPNOTSUPP �͓����l�������A POSIX.1 �ɏ]���Η��҂̃G���[�l�͋�ʂ����ׂ��ł���B) 

EOVERFLOW:

�w�肳�ꂽ�f�[�^�^�Ɋi�[����ɂ͒l���傫�߂��� (POSIX.1) 

EPERM:

���삪������Ă��Ȃ� (POSIX.1) 

EPFNOSUPPORT:

�T�|�[�g����Ă��Ȃ��v���g�R���t�@�~���[�ł��� 

EPIPE:

�p�C�v�����Ă��� (POSIX.1) 

EPROTO:

�v���g�R���G���[ (POSIX.1) 

EPROTONOSUPPORT:

�v���g�R�����T�|�[�g����Ă��Ȃ� (POSIX.1) 

EPROTOTYPE:

�\�P�b�g�Ɏw��ł��Ȃ��v���g�R���^�C�v�ł��� (POSIX.1) 

ERANGE:

���ʂ��傫�߂��� (POSIX.1, C99) 

EREMCHG:

�����[�g�A�h���X���ς���� 

EREMOTE:

�I�u�W�F�N�g�������[�g�ɂ��� 

EREMOTEIO:

�����[�g I/O �G���[ 

ERESTART:

�V�X�e���R�[�������f����ăX�^�[�g���K�v�ł��� 

EROFS:

�ǂݏo����p�̃t�@�C���V�X�e���ł��� (POSIX.1) 

ESHUTDOWN:

�ʐM���肪�V���b�g�_�E������đ��M�ł��Ȃ� 

ESPIPE:

�����ȃV�[�N (POSIX.1) 

ESOCKTNOSUPPORT:

�T�|�[�g����Ă��Ȃ��\�P�b�g��ʂł��� 

ESRCH:

���̂悤�ȃv���Z�X�͖��� (POSIX.1) 

ESTALE:

�t�@�C���n���h�����Â���ԂɂȂ��Ă��� (POSIX.1) 
NFS �⑼�̃t�@�C���V�X�e���ŋN���肤��B 

ESTRPIPE:

�X�g���[���p�C�v�G���[ 

ETIME:

���Ԃ��o�߂��� (POSIX.1 (XSI STREAMS option)) 
(POSIX.1 �ł� "STREAM ioctl(2) timeout" �Ə�����Ă���) 

ETIMEDOUT:

���삪�^�C���A�E�g���� (POSIX.1) 

ETXTBSY:

�e�L�X�g�t�@�C�����g�p���ł��� (POSIX.1) 

EUCLEAN:

Structure needs cleaning 

EUNATCH:

�v���g�R���̃h���C�o���t�^ (attach) ����Ă��Ȃ� 

EUSERS:

���[�U�[�������߂��� 

EWOULDBLOCK:

���삪�u���b�N����錩���݂ł��� (EAGAIN �Ɠ����l�ł��悢) (POSIX.1) 

EXDEV:

�s�K�؂ȃ����N (POSIX.1) 

EXFULL:

�ϊ��e�[�u������t�ł��� 		
		*/
