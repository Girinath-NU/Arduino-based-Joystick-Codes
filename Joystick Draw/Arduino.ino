#define X_pin A0
#define Y_pin A1
#define SW_pin 2

void setup() {
  Serial.begin(115200);
  pinMode(SW_pin, INPUT_PULLUP);
}

void loop() {
  int xValue = analogRead(X_pin);
  int yValue = analogRead(Y_pin);
  int button = digitalRead(SW_pin);

  Serial.print(xValue);
  Serial.print(",");
  Serial.print(yValue);
  Serial.print(",");
  Serial.println(button);

  delay(20);
}
