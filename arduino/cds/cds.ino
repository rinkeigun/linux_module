int val=0; //入力される値を格納する為の変数
void setup() {
  pinMode(12, OUTPUT);
  Serial.begin(9600); //モニターに出力するための設定
}

void loop() {
  //ANALOG INの０番ピンからデータを受け付ける
  val=analogRead(0);
  if( val/4<70) digitalWrite(12, HIGH); //13番ピンの出力をHIGH=5Vにする
  else digitalWrite(12, LOW); //13番ピンの出力をLOW = 0Vにする

  Serial.println(val/4); //入力された値をモニターに出力
  delay(100);
}

