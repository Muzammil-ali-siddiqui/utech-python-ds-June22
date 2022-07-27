int buttonstatus = 0;
int button = 4;
int buzzer = 8;
int led1 = 2;
int led2 = 12;

void setup()
{
  pinMode(button, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  Serial.begin (9600);
}

void loop()
{
  buttonstatus = digitalRead(button);
  Serial.println(buttonstatus);
  if (buttonstatus == HIGH)
  { digitalWrite(buzzer, HIGH);
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
  }
  else
  {
    digitalWrite(buzzer, LOW);
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
  }
}
