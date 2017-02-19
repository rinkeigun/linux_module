<?php
//
class hoge {
    public function __toString() {
        return "hoge to string";
    }
}
//
$obj = new hoge();
$s = 'data is ' . $obj;
echo "{$s}\n";
