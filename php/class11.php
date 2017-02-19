<?php
//
class hoge {
    public function __get($name) {
        echo "get: name is {$name}\n";
        return 'dummy';
    }
    public function __set($name, $val) {
        echo "set: {$name} <= {$val}\n";
    }
//
    private $i_;
}
//
$obj = new hoge();
$obj->i_;
var_dump($obj->i_);
$obj->i_ = 1;
var_dump($obj);
