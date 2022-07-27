#define CLOSE_LIMIT 5

int trig = 2;
int echo = 3;
int buzzer = 5;


void setup(){
Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(buzzer, OUTPUT);
}
  
void loop(){
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  
  int time = pulseIn(echo, HIGH);
  int distance = (time * 0.034)/ 2;
  
  Serial.println("Distance: ");
  Serial.println(distance);
  
  if (distance <= CLOSE_LIMIT){
    Serial.println("Door Open");
    digitalWrite(buzzer, HIGH);
  } else {
    Serial.println("Door Close");
    digitalWrite(buzzer, LOW);    
  }
  

  delay(10);
 
}
