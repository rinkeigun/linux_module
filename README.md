# linux_module
このファイルの内容を新しい順で先頭に追加するようにします
2016/07/04
WEB システム
	APACHE
	MYSQL
	PHP
	HTML
	CSS
DB　システム
SERVER
UNIT　SERVER
SENSOR

2016/07/03
vim + screen + gdb?
vim + screen + global?
比較 -d
nmap, imap
exモードって何？
vimの拡張、連携
keyの割り当て　:help index.txt, :verbose nmap

認知
聞いた、見たことがある（知っている）
機能（％）知っている
　　　　　理解している
　　　　　使ったことがある
自由に扱える
人に教えられる
拡張できる
不足点が分かっている

configureとmakeの関連、その仕組み



2016/06/28
使っているライブラリをどう調べるか
ldd

2016/06/26
コーディングルールを追加（変数名）
メモリ領域
　プログラム領域
　静的領域
　スタック領域
　ヒップ領域
　上記の領域はそれぞれどのような位置関係？
　システムが立ち上がったらもう決まったのか？それとも状況によって変化するか？

2016/06/23
IoT
user <-> web server <-> DB <-> Server(Center) <-> Concentrator(集約器) <-> sensor
web ( linux + Apache + PHP ) : 閲覧、指示 
DB ( MySql, DBアクセス ) : データ管理
Center( server, c ) : データアクセス、制御伝達
concentrator( c言語、開発要) : センサー情報収集、制御伝達
sensor( driver開発, 接続方法)

Center
機能：複数プロセス、データベース制御、ログ設計、関数登録

2016/06/09 
----- 2016/06/20 この内容は下に纏める -----------------
どんな技術が必要
１．割り込み
２．タイマー
３．スレッド
４．排他制御
５．セマフォ

スレッド関連関数は？どう使うか？

POSIX, MUTEXってなに？
MULTI THREAD
-----  2016/06/20 --------------------------------------

2016/06/12
bit 8, 16, 32, 64
各bit（CPU？）に対してレジスタ
レジスタの種類、役割
アセンブラの種類
アセンブラのコンパイラ
開発システム
ターゲットの種類

2016/06/16
linuxで起動imageをどう作るか。
libソースを入手、解読
初期化
実行速度、構造体の参照

2016/06/17
オブジェクトファイルの種類、フォーマット
種類：a.out, COFF -> PE, ELF 
ELF : 再配置可能なオブジェクト, 実行ファイル, 共有オブジェクトファイル
フォーマット:

2016/06/20
どのようなセンサーがあるか？
電子部品、パーツ(秋葉原ラジオセンター、サトー電気)
linux上ではどう扱うか
IoT
user <-> web server <-> DB <-> Concentrator(集約器) <-> senson
web ( linux + Apache + PHP ) 
DB ( MySql, DBアクセス )
concentrator( c言語、開発要)
sensor( driver開発, 接続方法)

日本統計API
http://www.e-stat.go.jp/SG1/estat/eStatTopPortal.do

linux 通信用語
セマフォ プロセス　キュー　通信　FIFO　メッセージ　ソケット
シグナル パイプ 共有メモリ 
どんな技術が必要
１．割り込み
２．タイマー
３．スレッド
４．排他制御
５．セマフォ
スレッド関連関数は？どう使うか？
POSIX, MUTEXってなに？
MULTI THREAD

