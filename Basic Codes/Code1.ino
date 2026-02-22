#define X_pin A0
#define Y_pin A1
#define LED_pin 13

int minThreshold = 50;
int maxThreshold = 650;

void setup() {
  pinMode(LED_pin, OUTPUT);
  Serial.begin(115200);
}

void loop() {

  int xValue = analogRead(X_pin);
  int yValue = analogRead(Y_pin);

  Serial.print("X: ");
  Serial.print(xValue);
  Serial.print("  Y: ");
  Serial.println(yValue);

  if (xValue < minThreshold || xValue > maxThreshold ||
      yValue < minThreshold || yValue > maxThreshold) {
    
    digitalWrite(LED_pin, HIGH);
    delay(200);
    digitalWrite(LED_pin, LOW);
    delay(200);
  }
  else {
    digitalWrite(LED_pin, LOW);
  }
}
