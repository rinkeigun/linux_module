<?php
 
class hoge {
  public function __construct($v) {
    $this->_val = $v;
  }
  public function getVal() {
    return $this->_val;
  }
//
private $_val;
}
//
$obj = new hoge('vall');
var_dump( $obj->getVal() );
