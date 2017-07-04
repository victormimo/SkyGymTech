 //this code measures the difference between two rising edges of the digitalised signal coming from hall sensor and then prints the rpm.
 //pin A0 is the signal pin
 int refsig = 1; //for converting the analog signal coming from hall sensor to digital through arduino code
 int val_A;//the digital value of the incoming analog signals of A
 int val_B;//and of B
 
 void setup()
 {
   Serial.begin(9600);
   pinMode(A0, INPUT);
   pinMode(A1, INPUT);
 }
 void loop()//Measure RPM
 {
   float sig_A = analogRead(A0); //read raw value of hall sensor A
   float sig_B = analogRead(A1); //read raw value of hall sensor B

   sig_A = sig_A * (5.0 / 1023.0);
   sig_B = sig_B * (5.0 / 1023.0);
   
   //HALL EFFECT A
   if (sig_A > refsig) val_A = LOW; //convert it to digital 0,1 form
   else val_A = HIGH;
  String str_A = "A";
   Serial.println(str_A + val_A);

   
   //HALL EFFECT B
    if (sig_B > refsig) val_B = LOW; //convert it to digital 0,1 form
   else val_B = HIGH;
  String str_B = "B";
  Serial.println(str_B + val_B);
   
 }
