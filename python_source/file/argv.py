# _*_ coding: utf-8 _*_

# python3 argv.py a b c
# python3 argv.py a b
# IndexError: list index out of range

import sys

def test_args( a ):
	try:
		print( len( a ) )
		print ( a )
		print ( u'first  arg : ' + a[1] )
		print ( u'second arg : ' + a[2] )
		print ( u'third  arg : ' + a[3] )
	except IndexError as e:
		print ( u'handle IndexError' )
if __name__ == "__main__":
	test_args( sys.argv ) 

