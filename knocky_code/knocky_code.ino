/* Copyright {2016} {Rach95}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

int pinPiezo = A0;
int pinRele = 8;
int oldValue = 10;
int duration = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(200);
  pinMode(pinPiezo, INPUT);
  pinMode(pinRele, OUTPUT);
}

void loop() {
  int newValue = 0;
  int maxValue = 0;
  String answer = "";

  answer = Serial.readString();

  if (answer == "open") {
    Serial.println("La puerta se abre");
    digitalWrite(pinRele, HIGH);
  }

  newValue = analogRead(pinPiezo);

  if (newValue != 10) {
    duration++;
  }

  if (newValue < 10) { //Evitar ruido
    oldValue = 10;
  } else if (newValue > 10) { //Se toca
    if (newValue > oldValue) {
      oldValue = newValue;
    } else if (newValue < oldValue) {
      maxValue = oldValue;

      if (newValue != maxValue) { //Si cambia el valor maximo
        Serial.println("Valor maximo: " + (String) oldValue);
        Serial.println("Duracion: " + (String) duration);
        //delay(250);
        duration = 0;
      }
    }
  }

}
