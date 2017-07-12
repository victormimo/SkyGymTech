// the setup routine runs once when you press reset:
int refsig = 1;
int sig_A, sig_B, sig_C, sig_D, sig_E, sig_F, sig_G;
int val_A, val_B, val_C, val_D, val_E, val_F, val_G;
int weight = 0;
int weight_old = 0;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the raw input on analog pin 0-4:
sig_A = analogRead(A0);
sig_B = analogRead(A1);
sig_C = analogRead(A2);
sig_D = analogRead(A3);
sig_E = analogRead(A4);
sig_F = analogRead(A5);
sig_G = analogRead(A6);

float voltage_A = sig_A * (5.0 / 1023.0);
float voltage_B = sig_B * (5.0 / 1023.0);
float voltage_C = sig_C * (5.0 / 1023.0);
float voltage_D = sig_D * (5.0 / 1023.0);
float voltage_E = sig_E * (5.0 / 1023.0);
float voltage_F = sig_F * (5.0 / 1023.0);
float voltage_G = sig_G * (5.0 / 1023.0);

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
  
  if (voltage_F < refsig) val_F = HIGH; //convert it to digital 0,1 form
  else val_F = LOW;
  String str_F = "F";
  Serial.println(str_F + val_F);
  
  if (voltage_G < refsig) val_G = HIGH; //convert it to digital 0,1 form
  else val_G = LOW;
  String str_G = "G";
  Serial.println(str_G + val_G);
}
