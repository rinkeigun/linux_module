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
 /* ソケットの作成 */
	sock = socket(AF_INET, SOCK_STREAM, 0);
	printf("sock = %d\n", sock ) ;

 /* 接続先指定用構造体の準備 */
	server.sin_family = AF_INET;
	server.sin_port = htons(12345);
	server.sin_addr.s_addr = inet_addr("192.168.2.11");

 /* サーバに接続 */
	con = connect(sock, (struct sockaddr *)&server, sizeof(server));
	if ( con == -1 )
	{
		printf( "接続失敗\n" ) ;
	}
	sleep( 3 ) ;
	/* サーバからデータを受信 */
	//memset(buf, 0, sizeof(buf));
	n = send(sock, data, strlen(data), 0);
	//n = write(sock, buf, sizeof(buf));
	//n = write(sock, data, strlen(data));
	//n = write(sock, 'a', 1);
	if( n == -1 )
	{
		printf( "送信失敗\n" ) ;
		printf( "errno:%d\n", errno ) ;
	}
	
	printf("%d, %s\n", n, data);

 /* socketの終了 */
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

引き数リストが長過ぎる (POSIX.1) 

	case EACCES:

許可がない (POSIX.1) 

	case EADDRINUSE:

アドレスがすでに使用されている (POSIX.1) 

	case EADDRNOTAVAIL:

アドレスが使用できない (POSIX.1) 

	case EAFNOSUPPORT:

アドレスファミリーがサポートされていない (POSIX.1) 

	case EAGAIN:

リソースが一時的に利用不可 (EWOULDBLOCK と同じ値でもよい) (POSIX.1) 

	case EALREADY:

接続が既に処理中である (POSIX.1) 

EBADE:

不正なやり取り (exchange) である 

EBADF:

ファイルディスクリプターが不正である (POSIX.1) 

EBADFD:

ファイルディスクリプターが不正な状態である 

EBADMSG:

メッセージが不正である (POSIX.1) 

EBADR:

不正なリクエストディスクリプター 

EBADRQC:

不正なリクエストコード 

EBADSLT:

不正なスロット 

EBUSY:

リソースが使用中である (POSIX.1) 

ECANCELED:

操作がキャンセルされた (POSIX.1) 

ECHILD:

子プロセスが無い (POSIX.1) 

ECHRNG:

チャンネル番号が範囲外である 

ECOMM:

送信時に通信エラーが発生した 

ECONNABORTED:

接続が中止された (POSIX.1) 

ECONNREFUSED:

接続が拒否された (POSIX.1) 

ECONNRESET:

接続がリセットされた (POSIX.1) 

EDEADLK:

リソースのデッドロックを回避した (POSIX.1) 

EDEADLOCK:

EDEADLK の同義語 

EDESTADDRREQ:

宛先アドレスが必要である (POSIX.1) 

EDOM:

数学関数で引き数が領域外である (out of domain) 

EDQUOT:

ディスククォータ (quota) を超過した (POSIX.1) 

EEXIST:

ファイルが存在する (POSIX.1) 

EFAULT:

アドレスが不正である (POSIX.1) 

EFBIG:

ファイルが大き過ぎる (POSIX.1) 

EHOSTDOWN:

ホストがダウンしている 

EHOSTUNREACH:

ホストに到達不能である (POSIX.1) 

EIDRM:

識別子が削除された (POSIX.1) 

EILSEQ:

不正なバイト列 (POSIX.1, C99) 

EINPROGRESS:

操作が実行中である (POSIX.1) 

EINTR:

関数呼び出しが割り込まれた (POSIX.1); signal(7) 参照。 

EINVAL:

引数が無効である (POSIX.1) 

EIO:

入出力エラー (POSIX.1) 

EISCONN:

ソケットが接続されている (POSIX.1) 

EISDIR:

ディレクトリである (POSIX.1) 

EISNAM:

名前付きのファイルである 

EKEYEXPIRED:

鍵が期限切れとなった 

EKEYREJECTED:

鍵がサーバにより拒否された 

EKEYREVOKED:

鍵が無効となった 

EL2HLT:

停止 (レベル 2) 

EL2NSYNC:

同期できていない (レベル 2) 

EL3HLT:

停止 (レベル 3) 

EL3RST:

停止 (レベル 3) 

ELIBACC:

必要な共有ライブラリにアクセスできなかった 

ELIBBAD:

壊れた共有ライブラリにアクセスしようとした 

ELIBMAX:

リンクしようとした共有ライブラリが多過ぎる 

ELIBSCN:

a.out のライブラリセクションが壊れている (corrupted) 

ELIBEXEC:

共有ライブラリを直接実行できなかった 

ELOOP:

シンボリックリンクの回数が多過ぎる (POSIX.1) 

EMEDIUMTYPE:

間違ったメディア種別である 

EMFILE:

オープンしているファイルが多過ぎる (POSIX.1)。 通常は getrlimit(2) に説明があるリソース上限 RLIMIT_NOFILE を超過した場合に発生する。 

EMLINK:

リンクが多過ぎる (POSIX.1) 

EMSGSIZE:

メッセージが長過ぎる (POSIX.1) 

EMULTIHOP:

マルチホップ (multihop) を試みた (POSIX.1) 

ENAMETOOLONG:

ファイル名が長過ぎる (POSIX.1) 

ENETDOWN:

ネットワークが不通である (POSIX.1) 

ENETRESET:

接続がネットワーク側から中止された (POSIX.1) 

ENETUNREACH:

ネットワークが到達不能である (POSIX.1) 

ENFILE:

システム全体でオープンされているファイルが多過ぎる (POSIX.1) 

ENOBUFS:

使用可能なバッファー空間がない (POSIX.1 (XSI STREAMS option)) 

ENODATA:

ストリームの読み出しキューの先頭に読み出し可能なメッセージがない (POSIX.1) 

ENODEV:

そのようなデバイスは無い (POSIX.1) 

ENOENT:

そのようなファイルやディレクトリは無い (POSIX.1) 

ENOEXEC:

実行ファイル形式のエラー (POSIX.1) 

ENOKEY:

要求された鍵が利用できない 

ENOLCK:

利用できるロックが無い (POSIX.1) 

ENOLINK:

リンクが切れている (POSIX.1) 

ENOMEDIUM:

メディアが見つからない 

ENOMEM:

十分な空きメモリー領域が無い (POSIX.1) 

ENOMSG:

要求された型のメッセージが存在しない (POSIX.1) 

ENONET:

マシンがネットワーク上にない 

ENOPKG:

パッケージがインストールされていない 

ENOPROTOOPT:

指定されたプロトコルが利用できない (POSIX.1) 

ENOSPC:

デバイスに空き領域が無い (POSIX.1) 

ENOSR:

指定されたストリームリソースが存在しない (POSIX.1 (XSI STREAMS option)) 

ENOSTR:

ストリームではない (POSIX.1 (XSI STREAMS option)) 

ENOSYS:

関数が実装されていない (POSIX.1) 

ENOTBLK:

ブロックデバイスが必要である 

ENOTCONN:

ソケットが接続されていない (POSIX.1) 

ENOTDIR:

ディレクトリではない (POSIX.1) 

ENOTEMPTY:

ディレクトリが空ではない (POSIX.1) 

ENOTSOCK:

ソケットではない (POSIX.1) 

ENOTSUP:

操作がサポートされていない (POSIX.1) 

ENOTTY:

I/O 制御操作が適切でない (POSIX.1) 

ENOTUNIQ:

名前がネットワークで一意ではない 

ENXIO:

そのようなデバイスやアドレスはない (POSIX.1) 

EOPNOTSUPP:

ソケットでサポートしていない操作である (POSIX.1) 
(Linux では ENOTSUP と EOPNOTSUPP は同じ値を持つが、 POSIX.1 に従えば両者のエラー値は区別されるべきである。) 

EOVERFLOW:

指定されたデータ型に格納するには値が大き過ぎる (POSIX.1) 

EPERM:

操作が許可されていない (POSIX.1) 

EPFNOSUPPORT:

サポートされていないプロトコルファミリーである 

EPIPE:

パイプが壊れている (POSIX.1) 

EPROTO:

プロトコルエラー (POSIX.1) 

EPROTONOSUPPORT:

プロトコルがサポートされていない (POSIX.1) 

EPROTOTYPE:

ソケットに指定できないプロトコルタイプである (POSIX.1) 

ERANGE:

結果が大き過ぎる (POSIX.1, C99) 

EREMCHG:

リモートアドレスが変わった 

EREMOTE:

オブジェクトがリモートにある 

EREMOTEIO:

リモート I/O エラー 

ERESTART:

システムコールが中断され再スタートが必要である 

EROFS:

読み出し専用のファイルシステムである (POSIX.1) 

ESHUTDOWN:

通信相手がシャットダウンされて送信できない 

ESPIPE:

無効なシーク (POSIX.1) 

ESOCKTNOSUPPORT:

サポートされていないソケット種別である 

ESRCH:

そのようなプロセスは無い (POSIX.1) 

ESTALE:

ファイルハンドルが古い状態になっている (POSIX.1) 
NFS や他のファイルシステムで起こりうる。 

ESTRPIPE:

ストリームパイプエラー 

ETIME:

時間が経過した (POSIX.1 (XSI STREAMS option)) 
(POSIX.1 では "STREAM ioctl(2) timeout" と書かれている) 

ETIMEDOUT:

操作がタイムアウトした (POSIX.1) 

ETXTBSY:

テキストファイルが使用中である (POSIX.1) 

EUCLEAN:

Structure needs cleaning 

EUNATCH:

プロトコルのドライバが付与 (attach) されていない 

EUSERS:

ユーザー数が多過ぎる 

EWOULDBLOCK:

操作がブロックされる見込みである (EAGAIN と同じ値でもよい) (POSIX.1) 

EXDEV:

不適切なリンク (POSIX.1) 

EXFULL:

変換テーブルが一杯である 		
		*/
