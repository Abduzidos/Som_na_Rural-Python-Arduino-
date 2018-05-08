int LedPin = 2;
int ButtonPin = 7;
void setup() {
 // put your setup code here, to run once:
 pinMode(LedPin, OUTPUT);
 pinMode(ButtonPin, INPUT);
 Serial.begin(9600);
}

void loop() {
 // put your main code here, to run repeatedly:
 int x = digitalRead(ButtonPin);
 if (x == HIGH) {
   digitalWrite(LedPin, HIGH);
   Serial.print(x);
   delay(1000);
 }
 else {
   digitalWrite(LedPin, LOW);
 }
}
