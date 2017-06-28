int sensorpin = 0;                 // analog pin used to connect the sharp sensor
int val = 0;                 // variable to store the values from sensor(initially zero)
int dist = 0;

void setup()
{
  Serial.begin(9600);               // starts the serial monitor
}
 
void loop()
{
  val = analogRead(sensorpin);       // reads the value of the sharp sensor
  dist = 4800/(val - 20);
  Serial.println(dist);            // prints the value of the sensor to the serial monitor
  delay(100);                    // wait for this much time before printing next value
}
