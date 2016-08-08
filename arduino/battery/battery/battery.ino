/*
 * 2016/08/06 Huiqun.Lin
 * 乾電池の電圧測定
 * 接続方法
 *    -  GND
 *    +  A0
 */


void setup(){
  Serial.begin(9600); 
}
void loop() {
  //float vt = (float)analogRead(A0) / 1023.0 * 5.0; // 5V系Arduinoの場合
  float vt = (float)map(analogRead(A0),0, 1023,0,500)/100.0; // mapを使った場合
  Serial.println(vt);
  delay(1000);
}

