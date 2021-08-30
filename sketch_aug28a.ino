#define RED 8
#define GREEN 7
#define BLUE 3

String value, color;

void setup()
{

  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  analogWrite(RED, 255);
  delay(1000);
  analogWrite(RED, 0);
  analogWrite(GREEN, 255);
  delay(1000);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 255);
  delay(1000);
  analogWrite(BLUE, 0);
  delay(1000);
}

void loop()
{

  if (Serial.available() > 0)
  {
    color = Serial.readStringUntil('\n');
    if (color == "R")
    {
      value = Serial.readStringUntil('\n');
      analogWrite(RED, value.toInt());
    }
    if (color == "G")
    {
      value = Serial.readStringUntil('\n');
      analogWrite(GREEN, value.toInt());
    }
    if (color == "B")
    {
      value = Serial.readStringUntil('\n');
      analogWrite(BLUE, value.toInt());
    }
  }
}
