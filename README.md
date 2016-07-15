# linux_module
このファイルの内容を新しい順で先頭に追加するようにします
2016/07/15
C#
c:\Windows\Microsoft.NET\Framework\バージョン番号\
コンパイラ:csc
ソースの拡張子:cs
netbeans
visual studio
IDE

統合開発環境
プロジェクト管理
バージョン管理
GUIの作成
チーム開発
作成補助
ビルド、デバッグ補助

scp -r rin-k@172.30.10.33:filename ~/local
scp filename rin-k172.30.10.33:


2016/07/14
Qtデザインのパーツ
layout
line, textarea, label, button, list, check, radio, select, pulldown

実行時間とswitch、メモリ配置、構造体参照位置

2016/07/13
Qt インストール
PostgreSQL インストール
MinGWインストール

2016/07/09
bit
二進数 (２の倍数、奇数倍）
ビット演算（論理和、論理積、排他、反転）
シフト
bitcheck, bitset, bitunset
奇数ビット、偶数ビット

時間計測
ライブラリを作りたい
配列はメモリ上どのように配置するか
キャッシュサイズはどのぐらいありますか？

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

