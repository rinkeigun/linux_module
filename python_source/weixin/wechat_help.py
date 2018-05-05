# _*_coding: utf-8 _*_

import wxpy
import inspect
import pprint

def info_obj( obj ):
    # builtin関数を除外したい
    p = eval(obj)
    #オブジェクトがモジュールの場合真を返します。
    #if inspect.ismodule(obj) or inspect.isclass(obj) or inspect.ismethod(obj) or inspect.isfunction(obj):
    if inspect.ismodule(p) or inspect.isclass(p) or inspect.ismethod(p) or inspect.isfunction(p):
        if '__class__' in obj:
            pass
        else:
            help(p)
    else:
        print(obj + " : "+ p )
    cnt = 0
    for i in dir(p):
        #print(i)
        #オブジェクトがモジュールの場合真を返します。
        if inspect.ismodule(p):
            try:
                modname = str(p).split(' ')[1]
                modname = modname.replace("'",'')
                s = modname+'.'+i
                info_obj(s)
            except:
                pass

        #オブジェクトが組み込みか Python が生成したクラスの場合に真を返します。
        if inspect.isclass(p):
            classname = str(p).split(' ')[1]
            classname = classname.replace("'",'')
            classname = classname.replace(">",'')
            s = classname+'.'+i
            info_obj(s)

        #オブジェクトがメソッドの場合真を返します。
        if inspect.ismethod(p):
            print(p)
            methodname = str(p)
            print('methodname')

        #オブジェクトが Python 関数(lambda 式で生成されたものを含む) の場合に真を返します。
        if inspect.isfunction(p):
            print(p)
            functionname = str(p).split(' ')[1]
            s = functionname+'.'+i
            print(s)
            info_obj(s)

        #object が Python のジェネレータ関数の場合真を返します。
        if inspect.isgeneratorfunction(p):
            print(p)
            generatorname = str(p)
            print('generatorname')
        cnt += 1

if __name__ == '__main__':
    w = 'wxpy'
    info_obj(w)

