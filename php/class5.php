<?php

Class A
{
	public function __construct()
	{
		echo __CLASS__."\n" ;
		print __CLASS__."\n" ;
		print get_class( $this )."\n" ;
	}
	function __destruct()
	{
		echo "__destruct\n" ;
	}
}

$a = new A();

?>
