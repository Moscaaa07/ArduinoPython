const int pinPIR = 2;
const int pinLDR = A0;
const int pinLED = 13;

void setup() {
  pinMode(pinPIR, INPUT);
  pinMode(pinLED, OUTPUT);
  Serial.begin(9600);

  digitalWrite(pinLED, LOW);

  // Stabilizzazione PIR (IMPORTANTE)
  delay(30000);
}

void loop() {
  int movimento = digitalRead(pinPIR);
  int luce = analogRead(pinLDR);

  // Invio dati a Python
  Serial.print(movimento);
  Serial.print(",");
  Serial.println(luce);

  // Ricezione comando da Python
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == '1') {
      digitalWrite(pinLED, HIGH);
    } else if (comando == '0') {
      digitalWrite(pinLED, LOW);
    }
  }

  delay(200); // più stabile della 100
}