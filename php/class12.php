<?php
//
class hoge {
    public function __call($name, $args) {
        echo "call {$name}\n";
        var_dump($args);
    }
    public static function __callStatic($name, $args) {
        echo "callStatic {$name}\n";
        var_dump($args);
    }
}
//
$obj = new hoge();
$obj->func();
hoge::func_static();
