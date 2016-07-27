void setup(){
  Serial.begin(9600); 
}
void loop() {

  float teikou = (1023- analogRead(A0))/1023.0*10000.0 ;
//Serial.println(teikou ) ; //可変抵抗値(A0)表示
Serial.println(calcTemp(analogRead(A1))) ; //温度(A1)表示
delay(5000);
}
// for thermistor NXFT15XH103FA2B
float B=3452.0;
float T0=298.15;
float R0=10.0;
float R1=9.88;

float calcTemp(float raw) {
  float rr1,t;
  rr1= R1 * raw / (1024.0 - raw);
  t = 1.0 / (log(rr1 / R0) / B + (1.0 / T0));
  //return (int)((t - 273.15) * 10.0); //unit 0.1 degree;
  return ((t - 273.15) ); //unit 0.1 degree;
}
