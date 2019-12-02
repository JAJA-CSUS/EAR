/* 
The purpose of this code is to test an IR Proximity Sensor component to check if it is working.
The IR Sensor is connected to pin A0, 5v source, and ground of the arduino UNO board.
*/

int sensorpin = A0;          // A0 pin connects the IR sensor
int val = 0;                 // variable that stores the values from the IR sensor (initially zero)

void setup()
{
  Serial.begin(9600);             // starts the serial monitor (data rate=9600bps)
}
 
void loop()
{
  val = analogRead(sensorpin);    // reads the value of the IR sensor, stores in variable var
  Serial.println(val);            // prints the value of var to the serial monitor
  delay(400);                     // wait 400ms before next IR sensor read
}
