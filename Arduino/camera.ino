int ButtonPin = 7;
int ButtonPin2 = 8;
void setup() {
 // put your setup code here, to run once:
 pinMode(ButtonPin, INPUT);
 pinMode(ButtonPin2,INPUT);
 Serial.begin(9600);
}

void loop() {
 // put your main code here, to run repeatedly:
 int x = digitalRead(ButtonPin);
 int y = digitalRead(ButtonPin2);
 if (x == HIGH) {
   Serial.print(x);
   delay(1000);
 }
 if(y == HIGH){
   Srial.print('2');
   delay(1000);
 }

 
}
