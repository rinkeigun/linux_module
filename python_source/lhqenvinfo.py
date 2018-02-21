#  -*- coding: utf-8 -*-
# File name : lhqenvinfo.py
# Date      : 2018/02/20
# Author    : Huiqun Lin
# Ver       : 0.1
# Explain   : show infomation
#-----------------------------------------------

import os
import sys

class lhqenvinfo:
    # function list

    def __init__(self):
        pass

    def strformat(self, title, content):
        return '{0:<10}'.format(title) + ':' + content

    def strexec(self, s1, strcommand):
        ss = ''
        if s1 is None:
            ss = strcommand
        else:
            ss = s1 + "." + strcommand
        return (strcommand, str(eval(ss))) 

    def osinfo(self):
        ostuple = ('path'
            , 'name'
            , 'curdir'
            , 'pardir' 
            , 'sep' 
            , 'extsep' )
        oslist = [] 
        for i in ostuple:
            s1, s2 = self.strexec('os', i) 
            oslist.append( str(self.strformat( s1, s2 )) ) 
        return oslist

    def sysinfo(self):
        systuple = ('platform'
            , 'version'
            , 'version_info')
        syslist = []
        for i in systuple:
            s1, s2 = self.strexec('sys',i) 
            syslist.append( str(self.strformat( s1, s2)) ) 
        return syslist

    def printinfo(self):
        l = self.osinfo()
        for i in l:
            print( i)
        for i in self.sysinfo():
            print( i )

###################################################################
if __name__ == '__main__':
    a = lhqenvinfo()
    a.printinfo()
