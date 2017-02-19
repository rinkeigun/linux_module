<?php
 
class hoge {
    public function __construct() {
        echo "run hoge constructor\n";
    }
    public function __destruct() {
        echo "run hoge destructor\n";
    }
}
class foo extends hoge{
    public function __construct() {
        parent::__construct(); // 継承元クラスのコンストラクターを呼ぶ
        echo "run foo constructor\n";
    }
    public function __destruct() {
        echo "run foo destructor\n";
        parent::__destruct(); // 継承元クラスのデストラクターを呼ぶ
    }
}
//
$obj = new foo();
