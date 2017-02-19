<?php

namespace foo;

Class A
{
	public function __construct()
	{

		echo __TRAIT__."\n" ;
		echo __DIR__."\n" ;
		echo __FILE__."\n" ;
		echo __NAMESPACE__."\n" ;
		echo __CLASS__."\n" ;
		echo __FUNCTION__."\n" ;
		echo __METHOD__."\n" ;
		echo __LINE__."\n" ;
	}
	function __destruct()
	{
		echo "__destruct\n" ;
	}
}

$a = new A();

?>
