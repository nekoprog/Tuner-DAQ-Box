int wbLo = 10; //afr user input
int wbHi = 20; //afr user input
int wbIn = A0;
int revIn = A1;
int spdIn = A2;
int wbSensor = 0;
unsigned long revSensor = 0; //counts per second
unsigned long spdSensor = 0; //counts per second
float afr = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  wbSensor = analogRead(wbIn);
  revSensor = pulseIn(revIn,HIGH); //todo
  spdSensor = pulseIn(spdIn,HIGH); //todo
  delay(100);
  afr = (wbSensor*(wbLo/1023.0))+(wbHi-wbLo);
  Serial.println(afr); //todo
  Serial.println(revSensor);
  Serial.println(spdSensor);
}
