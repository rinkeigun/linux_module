<?php
 
class hoge {
  public function setVal($v) { $this->_val = $v; }
  public function getVal() { return $this->_val; }
//
private $_val;
}
//
$obj = new hoge();
$obj->setVal('test');
var_dump( $obj->getVal() );
