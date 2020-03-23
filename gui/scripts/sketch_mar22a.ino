int r = 1;
void setup(){
  Serial.begin(9600);
}
void loop(){
  if(Serial.available()){         //From RPi to Arduino
    r = r * (Serial.read() - '0');  //conveting the value of chars to integer
    Serial.println(r);
  }
}
