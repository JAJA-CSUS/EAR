/*
Author: Angelica Smith-Evans

This is an example of a switch case.
  case 0: wait for button input
  case 1: if button input = 1, turn on LED for 5sec
*/
//LED
  const int LED = 13;
//Buttons
  const int button1Pin = A2;                // button1Pin connected to UNO pin A2
  int button1State = 0;                     // variable for reading the pushbutton status, initially low

//Switch Case Variables
  int ns = 0;
  int cs = 0;
  
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  
  //initialize the button pins
  pinMode(button1Pin, INPUT);
  
  pinMode(LED, OUTPUT);
}

void loop() {
while(1)
{
  //cs = ns;
  Serial.println(button1State);
  //serial.println(ns);
  button1State = digitalRead(button1Pin);
    switch (cs) {
      case 0:
      digitalWrite(LED, LOW);
          if (button1State == HIGH)
          {
             cs = 1;
          } else {
             cs = 0;
          } 
        break;
      case 1:
        digitalWrite(LED, HIGH);
        delay(5000);
        cs = 0;
        break;
     /*   
      case '2':
        digitalWrite(4, HIGH);
        break;
        */
      default:
        //cs = 0;
        break;
    }
        }
    delay(1000);
  }

/*
void buttonRead()
{
  // read the state of the pushbutton value:
  button1State = digitalRead(button1Pin);

  if (button1State == '1')
  {
     ns = 1;
  } else {
     ns = 0;
  }  
  
}

void turnOnLED
{
  digitalWrite(LED, HIGH);
  delay(5000);
  ns = 0;
}
*/
