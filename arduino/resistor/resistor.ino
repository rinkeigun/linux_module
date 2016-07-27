void setup(){
  Serial.begin(9600); 
}
void loop() {
Serial.println((1023- analogRead(A0))/1023.0*10000.0) ; //可変抵抗値(A0)表示
 delay(1000);
}

