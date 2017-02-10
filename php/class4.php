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

Class A2 extends A
{
	public $var = 'aaa2' ;
	protected $var2 = 'bbb2' ;
	// private $var3 = 'doesnt work' ;

	function displayVar()
	{
		echo 'Hello :'.$this->var ;
		echo 'Hello :'.$this->var2 ;
		echo 'Hello :'.$this->var3 ;
	}
}

$a = new A();
$a2 = new A2();
echo $a->var ;
//echo $a->var2 ;
//echo $a->var3 ;
$a->displayVar();
$a2->displayVar();

?>
