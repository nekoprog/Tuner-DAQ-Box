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
	Serial.begin(115200);
}

void loop() {
	// put your main code here, to run repeatedly:
	wbSensor = analogRead(wbIn);
	//revSensor = pulseIn(revIn,HIGH); //todo
	//spdSensor = pulseIn(spdIn,HIGH); //todo
	afr = (wbLo*(wbSensor/1023))+(wbHi-wbLo); //this shit won't work
	Serial.print(afr);
	//todo
	Serial.print(',');
	Serial.println(0);
	//Serial.print(',');
	//Serial.println(spdSensor);
  delay(50);
}
