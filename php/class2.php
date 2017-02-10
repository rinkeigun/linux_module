<?php

Class A
{
	public	$var = 'aaa' ;

	public function displayVar()
	{
		echo $this->var ;
		echo get_class( $this ) ;
	}
}

$a = new A();
$a->displayVar();

?>
