<?php
 
class hoge {
    public function A() {
        echo "call hoge's A\n";
    }
//
private $i_ = 1;
}
//
class foo extends hoge {
    public function A() {
        echo "call foo's A\n";
    }
//
private $i_ = 999;
}
//
$foo_obj = new foo();
var_dump($foo_obj);
