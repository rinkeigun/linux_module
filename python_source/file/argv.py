# -*- coding: utf-8 -*-

# python3 argv.py a b c
# python3 argv.py a b
# IndexError: list index out of range

import sys

def test_args( args ):
	try:
		print( len( args ) )
		print ( args )
		print ( u'first  arg : ' + args[1] )
		print ( u'second arg : ' + args[2] )
		print ( u'third  arg : ' + args[3] )
	except IndexError as e:
		print ( u'handle IndexError' )

__main__ = '__main__'
if (__main__ == '__main__'):
	test_args( sys.argv ) 

