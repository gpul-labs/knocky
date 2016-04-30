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
int oldValue = 10;

void setup() {
  Serial.begin(9600);
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

      Serial.println("Valor maximo: " + (String) oldValue);
      Serial.println("Duracion: " + (String) duration);
      duration = 0;
    }
  }

}
