// the setup routine runs once when you press reset:
int refsig = 1;
int sig_A, sig_B, sig_C, sig_D, sig_E;
int val_A, val_B, val_C, val_D, val_E;
int weight = 0;
int weight_old = 0;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the raw input on analog pin 0-4:
sig_A = analogRead(A2);
sig_B = analogRead(A3);
sig_C = analogRead(A4);
sig_D = analogRead(A5);
sig_E = analogRead(A6);

float voltage_A = sig_A * (5.0 / 1023.0);
float voltage_B = sig_B * (5.0 / 1023.0);
float voltage_C = sig_C * (5.0 / 1023.0);
float voltage_D = sig_D * (5.0 / 1023.0);
float voltage_E = sig_E * (5.0 / 1023.0);

  //Convert analog to digital
  if (voltage_A < refsig) val_A = HIGH; //convert it to digital 0,1 form
    else val_A = LOW;
  String str_A = "A";
  Serial.println(str_A + val_A);
  if (voltage_B < refsig) val_B = HIGH; //convert it to digital 0,1 form
    else val_B = LOW;
  String str_B = "B";
  Serial.println(str_B + val_B);
  if (voltage_C < refsig) val_C = HIGH; //convert it to digital 0,1 form
    else val_C = LOW;
  String str_C = "C";
  Serial.println(str_C + val_C);
  if (voltage_D < refsig) val_D = HIGH; //convert it to digital 0,1 form
    else val_D = LOW;
  String str_D = "D";
  Serial.println(str_D + val_D);
  if (voltage_E < refsig) val_E = HIGH; //convert it to digital 0,1 form
    else val_E = LOW;
  String str_E = "E";
  Serial.println(str_E + val_E);
}
