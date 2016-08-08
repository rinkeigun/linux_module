/*
 * 2016/08/06 Huiqun.Lin
 * 可変抵抗
 * ピンの位置【上向き】
 * 　　　①　　　③
 * 　　　　　②
 * 接続方法
 * 真ん中のピン：A0
 * 両サイド：GND, 5V(どっちでも大丈夫と思ったが、違うようです。どっちは正しいか）
 * 
 */

void setup(){
  Serial.begin(9600); 
}
void loop() {
  Serial.println("test") ;
  //Serial.println((1023- analogRead(A0))/1023.0*10000.0) ; //可変抵抗値(A0)表示
  Serial.println(analogRead(A0)/1023.0*10000.0) ; //可変抵抗値(A0)表示
  Serial.println(map( analogRead(A0), 0.0, 1023.0, 0.0, 1000.0)*10.0) ; //可変抵抗値(A0)表示, map
  delay(1000);
}

