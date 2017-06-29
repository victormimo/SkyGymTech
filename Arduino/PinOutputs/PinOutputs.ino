 //this code measures the difference between two rising edges of the digitalised signal coming from hall sensor and then prints the rpm.
 //pin A0 is the signal pin
 int refsig = 1; //for converting the analog signal coming from hall sensor to digital through arduino code
 int val_A;//the digital value of the incoming analog signals of A
 int val_B;//and of B
 int prev_val_A = 0;
 int prev_val_B = 0;
 long t_A, t_B, t_B_old=0, cur_t; //time variables
 int r = 0.04; //m
 int way = -1;
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
   if (sig_A > refsig) val_A = HIGH; //convert it to digital 0,1 form
   else val_A = LOW;

  String str_A = "A";

   Serial.println(str_A + val_A);

   if (prev_val_A == 0 && val_A == 1) { //check for rising edge
     cur_t = micros();
     //Serial.println(cur_t);
     //Serial.println(1000000 * 60 / (cur_t - t)); //print the rpm
     //Serial.println(way*1000000 * 2 * 3.14 * 0.04 / (cur_t - t_A)); //print the rpm
     t_A = micros();
   }
   prev_val_A = val_A;

   //HALL EFFECT B
    if (sig_B > refsig) val_B = HIGH; //convert it to digital 0,1 form
   else val_B = LOW;

  String str_B = "B";

  Serial.println(str_B + val_B);
   
   if (prev_val_B == 0 && val_B == 1) { //check for rising edge
     cur_t = micros();
     t_B = micros();
      //Compare two times
      //Serial.println (t_A);
      if((t_A - t_B_old) < (t_B - t_A))
      {
        //Serial.println("Clockwise");
        way = 1;
      }
      else 
      {
        way = -1;
      } 
      t_B_old = t_B;
 }
   prev_val_B = val_B;   
   
 }
