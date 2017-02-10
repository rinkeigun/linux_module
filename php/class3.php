<?php

Class A
{
	public	$var = 'aaa' ;  // 
	protected	$var2 = 'bbb' ; // 
	private	$var3 = 'ccc' ;  // only this class

	public function displayVar()
	{
		echo $this->var ;
		echo $this->var2 ;
		echo $this->var3 ;
	}
}

$a = new A();
echo $a->var ;
echo $a->var2 ;
echo $a->var3 ;
$a->displayVar();

?>
