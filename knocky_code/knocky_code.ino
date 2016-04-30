int pinPiezo = A0;
int oldValue = 10;

void setup() {
  Serial.begin(115200);
  pinMode(pinPiezo, INPUT);
}

void loop() {
  int newValue = 0;
  int maxValue = 0;
  int duration = 0;
  long ardTime = 0;

  ardTime = millis();

  newValue = analogRead(pinPiezo);
  //Serial.println(ardTime + "\t" + newValue);

  if (newValue < 10) {
    oldValue = 10;
    duration++;
  } else if (newValue > 10) {
    if (newValue > oldValue) {
      oldValue = newValue;
    } else if (newValue < oldValue) {
      maxValue = oldValue;

      Serial.println("Valor maximo: " + oldValue);
      Serial.println("Duracion: " + duration);
      duration = 0;
    }
  }

}
