#include <Servo.h>


Servo servoLeft;
Servo servoRight;

void setup() {
  servoLeft.attach(13);
  servoRight.attach(12); 
  pinMode(1,OUTPUT);
  pinMode(8,OUTPUT);
  
}

void loop() {
  servoLeft.writeMicroseconds (3000);
  servoRight.writeMicroseconds (1300);
  delay(500);
  servoRight.write(180);
  servoRight.write(180);
  delay(500);
  servoLeft.writeMicroseconds (3000);
  servoRight.writeMicroseconds (1300);
  delay(500);
  servoLeft.writeMicroseconds (3000);
  servoRight.writeMicroseconds (1300);
  delay(500);
  digitalWrite(1, HIGH);   
  delay(16);              
  digitalWrite(1, LOW);
  delay(.70); 
}

