# -*- coding: utf-8 -*-
# File name : mtype.py
# Date      : 2017/11/03
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、型を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['ブール',''],
			['整数',''],
			['浮動小数点型',''],
			['複素数',''],
			['文字列',''],
			['イテレータ',''],
			['シーケンス',''],
		]
		mBase.__init__(self, com_list)
		

	def __str__(self):
		print('str')

	def __del__(self):
		print( 'クラスが終了するときに呼び出される' )
# mBaseの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	mMain()
	
#types.NoneType¶(原文)
#None の型です。

#types.TypeType(原文)
#typeオブジェクトの型です (type() などによって返されます)。組み込みの type のエイリアスになります。

#types.BooleanType(原文)
#bool の True と False の型です。これは組み込みの bool のエイリアスです。


#types.IntType(原文)
#整数の型です (e.g. 1)。組み込みの int のエイリアスになります。

#types.LongType(原文)
#長整数の型です (e.g. 1L)。組み込みの long のエイリアスになります。

#types.FloatType(原文)
#浮動小数点数の型です (e.g. 1.0)。組み込みの float のエイリアスになります。

#types.ComplexType(原文)
#複素数の型です (e.g. 1.0j)。 Python が複素数のサポートなしでコンパイルされていた場合には定義されません。

#types.StringType(原文)
#文字列の型です (e.g. 'Spam')。組み込みの str のエイリアスになります。

#types.UnicodeType(原文)
#Unicode 文字列の型です (e.g. u'Spam')。 Python が Unicode のサポートなしでコンパイルされていた場合には定義されません。組み込みの Unicode のエイリアスになります。

#types.TupleType(原文)
#タプルの型です (e.g. (1, 2, 3, 'Spam'))。組み込みの tuple のエイリアスになります。

#types.ListType(原文)
#リストの型です (e.g. [0, 1, 2, 3])。組み込みの list のエイリアスになります。

#types.DictType(原文)
#辞書の型です (e.g. {'Bacon': 1, 'Ham': 0})。組み込みの dict のエイリアスになります。

#types.DictionaryType(原文)
#DictType の別名です。

#types.FunctionType(原文)
#types.LambdaType(原文)
#ユーザー定義の関数または lambda 式によって作成された関数の型です。

#types.GeneratorType(原文)
#ジェネレータ (generator) 関数の呼び出しによって生成されたイテレータオブジェクトの型です。


#types.CodeType(原文)
#compile() 関数などによって返されるコードオブジェクトの型です。

#types.ClassType(原文)
#ユーザー定義の、旧形式クラスの型です。

#types.InstanceType(原文)
#ユーザー定義の旧形式クラスのインスタンスの型です。

#types.MethodType(原文)
#ユーザー定義のクラスのインスタンスのメソッドの型です。

#types.UnboundMethodType(原文)
#MethodType の別名です。

#types.BuiltinFunctionType(原文)
#types.BuiltinMethodType(原文)
#len() や sys.exit() のような組み込み関数や、組み込み型のメソッドの型です。 (ここでは、"組み込み"という単語を、"C で書かれた" という意味で使っています)

#types.ModuleType(原文)
#モジュールの型です。

#types.FileType(原文)
#sys.stdout のような open されたファイルオブジェクトの型です。組み込みの file のエイリアスになります。

#types.XRangeType(原文)
#xrange() 関数によって返される range オブジェクトの型です。組み込みの xrange のエイリアスになります。

#types.SliceType(原文)
#slice() 関数によって返されるオブジェクトの型です。組み込みの slice のエイリアスになります。

#types.EllipsisType(原文)
#Ellipsis の型です。

#types.TracebackType(原文)
#sys.exc_traceback に含まれるようなトレースバックオブジェクトの型です。

#types.FrameType(原文)
#フレームオブジェクトの型です。トレースバックオブジェクト tb の tb.tb_frame などです。

#types.BufferType(原文)
#buffer() 関数によって作られるバッファオブジェクトの型です。

#types.DictProxyType(原文)
#TypeType.__dict__ のような dict へのプロキシ型です。

#types.NotImplementedType(原文)
#NotImplemented の型です。

#types.GetSetDescriptorType(原文)
#FrameType.f_locals や array.array.typecode のような、拡張モジュールにおいて PyGetSetDef によって定義されたオブジェクトの型です。この型はオブジェクト属性のディスクリプタとして利用されます。 property 型と同じ目的を持った型ですが、こちらは拡張モジュールで定義された型のためのものです。


#types.MemberDescriptorType(原文)
#datetime.timedelta.days のような、拡張モジュールにおいて PyMemberDef によって定義されたオブジェクトの型です。この型は、標準の変換関数を利用するような、Cのシンプルなデータメンバで利用されます。 property 型と同じ目的を持った型ですが、こちらは拡張モジュールで定義された型のためのものです。

#CPython 実装の詳細: Pythonの他の実装では、この型は GetSetDescriptorType と同じかもしれません。

#types.StringTypes(原文)	
