<?php
//
class hoge {
    public function __invoke() {
        echo "call method\n";
    }
}
//
$obj = new hoge();
$obj();
