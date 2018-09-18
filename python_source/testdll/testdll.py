from ctypes import cdll
import ctypes

# 作成したdllの読み込み
dll = cdll.LoadLibrary('./dll1.dll')
# dllの関数をセット
initializeClass = dll.initializeClass
exitClass = dll.exitClass
constructor = dll.constructor
destructor = dll.destructor
calcA = dll.calcA
getB = dll.getB
#関数を呼び出す
initializeClass(5)
constructor(0, 100)
print (calcA(0, 10))
print (getB(0))
destructor(0)
exitClass()