int pm = A1;

int led1 = 13;
int led2 = 11;
int led3 = 10;
int led4 = 9;
int led5 = 8;
int led6 = 7;
int led7 = 6;
int led8 = 4;
int led9 = 3;
int led10 = 2;

int minVal = 40;
int maxVal = 1020;

void setup()
{
  pinMode(pm, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);
  pinMode(led9, OUTPUT);
  pinMode(led10, OUTPUT);

  Serial.begin(9600);
}

void loop()
{
  int value = analogRead(pm);
  Serial.println(value);
  

  if (value >= minVal && value < 120)
  {
    digitalWrite(led1, HIGH);
  }
  else 
  { 
    digitalWrite(led1, LOW);
  }
  if(value >=100 && value < 220)
  {
    digitalWrite(led2, HIGH);
  }
  else
  {
    digitalWrite(led2, LOW);
  }
  if(value >=200 && value < 320)
  {
    digitalWrite(led3, HIGH);
  }
  else 
  {
    digitalWrite(led3, LOW);
  }
  if(value >=300 && value < 420)
  {
    digitalWrite(led4, HIGH);
  }
  else
  {
    digitalWrite(led4, LOW);
  }
  if(value >=400 && value < 520)
  {
    digitalWrite(led5, HIGH);
  }
  else
  {
    digitalWrite(led5, LOW);
  }
  if(value >=500 && value < 620)
  {
    digitalWrite(led6, HIGH);
  }
  else
  {
    digitalWrite(led6, LOW);
  }
  if(value >=600 && value < 720)
  {
    digitalWrite(led7, HIGH);
  }
  else
  {
    digitalWrite(led7, LOW);
  }
  if(value >=700 && value < 820)
  {
    digitalWrite(led8, HIGH);
  }
  else
  {
    digitalWrite(led8, LOW);
  }
  if(value >= 800 && value < 920)
  {
    digitalWrite(led9, HIGH);
  }
  else
  {
    digitalWrite(led9, LOW);
  }
  if(value >= 900 && value < maxVal)
  {
    digitalWrite(led10, HIGH);
  }
  else
  {
    digitalWrite(led10, LOW);
  }
} 


































































































 
