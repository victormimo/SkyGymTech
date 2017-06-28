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
sig_A = analogRead(A0);
sig_B = analogRead(A1);
sig_C = analogRead(A2);
sig_D = analogRead(A3);
sig_E = analogRead(A4);

float voltage_A = sig_A * (5.0 / 1023.0);
float voltage_B = sig_B * (5.0 / 1023.0);
float voltage_C = sig_C * (5.0 / 1023.0);
float voltage_D = sig_D * (5.0 / 1023.0);
float voltage_E = sig_E * (5.0 / 1023.0);

  //Convert analog to digital
  if (voltage_A < refsig) val_A = HIGH; //convert it to digital 0,1 form
    else val_A = LOW;
  if (voltage_B < refsig) val_B = HIGH; //convert it to digital 0,1 form
    else val_B = LOW;
  if (voltage_C < refsig) val_C = HIGH; //convert it to digital 0,1 form
    else val_C = LOW;
  if (voltage_D < refsig) val_D = HIGH; //convert it to digital 0,1 form
    else val_D = LOW;
  if (voltage_E < refsig) val_E = HIGH; //convert it to digital 0,1 form
    else val_E = LOW;

////  Find out current weight moved
//  if (val_A == 1)
//  {          //True if bottom weight is in place
//    if(val_B == 1)
//    {
//      if(val_C == 1)
//      {
//        if (val_D == 1)
//        {
//          if (val_E == 1)
//          {  //True if top weight is stationary
//            weight=50;
//          }
//          else {
//            weight=40;
//            
//          }
//        }
//        else weight=30;
//      }
//      else weight=20;
//    }
//    else weight=10;
//  }
//  else weight=0;

if (val_A == 1 && val_B == 1 && val_C == 1 && val_D == 1 && val_E == 1)
{
  weight = 0;
}
else if (val_B == 1 && val_C == 1 && val_D == 1 && val_E == 1)
{
  weight = 10;
}
else if (val_C == 1 && val_D == 1 && val_E == 1)
{
  weight = 20;
}
else if (val_D == 1 && val_E == 1)
{
  weight = 30;
}
else if (val_E == 1)
{
  weight = 40;
}
else
{
  weight = 50;
}
  //Check for change in weight
  if (weight!=weight_old){
    Serial.println(weight);
  }

  //Set old weight value for comparison
  weight_old = weight;
}
