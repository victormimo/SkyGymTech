int car = 0;

void setup() {
  Serial.begin(9600); // use the same baud-rate as the python side
}
void loop() {
  //Serial.print("Hello world from Ardunio!"); // write a string
  //Serial.print("\t");
 Serial.println(car);
  delay(1000);
  car = car + 1;
}
