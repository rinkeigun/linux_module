# linux_module

2016/06/09 どんな技術が必要
１．割り込み
２．タイマー
３．スレッド
４．排他制御
５．セマフォ

スレッド関連関数は？どう使うか？

POSIX, MUTEXってなに？
MULTI THREAD

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
linux上ではどう扱うか
user <-> web server <-> DB <-> Concentrator(集約器) <-> senson
web ( linux + Apache + PHP ) 
DB ( MySql, DBアクセス )
concentrator( c言語、開発要)
sensor( driver開発, 接続方法)

日本統計API
http://www.e-stat.go.jp/SG1/estat/eStatTopPortal.do

linux 通信用語
セマフォ プロセス　キュー　通信　FIFO　メッセージ　ソケット
シグナル パイプ 共有メモリ thread(スレッド) タイマー 割り込み

