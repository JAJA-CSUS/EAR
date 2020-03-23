/*
Author: Angelica Smith-Evans
        Jeremy Shaw
		
The purpose of this code is to path a robot towards a cubby, to pick up a cubby from a shelf
and bring it back to a point.

*/

//////////////////////////////////////////////////////////////////////////////////////
//                        Declaration Section                              //
//////////////////////////////////////////////////////////////////////////////////////
//Speed Control
int vSpeed = 190;                  // MAX 255
int turn_speed = 100;              // MAX 255 
int turn_delay = 10;
  
//Motor Driver
//Left Wheel
#define left_wheel_enable 10        //enB pin connected to UNO pin 10 to enable LW Motor Driver
#define L1 9                       //L1 pin connected to UNO pin 9 to control LW Motor
#define L2 8                       //L2 pin connected to UNO pin 8 to control LW Motor
// Right Wheel
#define right_wheel_enable 5        //enA pin connected to UNO pin 5 to enable RW Motor Driver
#define R1 7                       //R1 pin connected to UNO pin 7 to control RW Motor
#define R2 6                       //R2 pin connected to UNO pin 6 to control RW Motor

// Stepper Driver
#define dirPin 2
#define stepPin 3
#define enaPin 4
#define stepsPerRevolution 800
#define basketLimitPin A5              // limit switch for basket lifter arm
#define stepTime 700                // was 700 for NEMA 17
int basketLimit = LOW;

//Proximity Sensor
#define front_left_IR A0             // connect the front left IR sensor to pin A0
#define front_right_IR A1            // connect the front right IR sensor to pin A1
int front_left_IR_state = 0;              // variable to store the values from front left sensor
int front_right_IR_state = 0;             // variable to store the values from front right sensor
#define rear_left_IR A3
#define rear_right_IR A4
int rear_left_IR_state = 0;
int rear_right_IR_state = 0;
  
//LED
#define LED 5                        // ATP LED pin 5; Arduino Uno Mega pin 13

//Buttons
#define button1Pin A2                // button1Pin connected to UNO pin A2
int button1State = 0;                     // variable for reading the pushbutton status, initially low

//Switch Case Variables
int ns = 0;
int cs = 0;

// Basket state
int haveBasket = 0;

// Which cubby
int cubby = 1;  // default assumes 1. Range 1-4

// skipStep
int skipStep = 1;

// i2c setup, may not be necessary
#include <Wire.h>
#define sAddr 8  // PyPi chose 8, iirc (check for hex vs decimal)
int i2cSwitch = 0;
int i2cCount = 0;

//serial to PyPi
int inByte = 0;
int r = 1;

//////////////////////////////////////////////////////////////////////////////////////
//                                Board Set-up Section                              //
//////////////////////////////////////////////////////////////////////////////////////
  
void setup() 
{
  // initialize serial communication:
  Serial.begin(9600);
  haveBasket = 1;
  
  //initialize the button pins
  pinMode(button1Pin, INPUT);
  
  pinMode(LED, OUTPUT);
  pinMode(L1, OUTPUT);
  pinMode(L2, OUTPUT);
  pinMode(R1, OUTPUT);
  pinMode(R2, OUTPUT);
  
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enaPin, OUTPUT);

  pinMode(basketLimitPin, INPUT);

  pinMode(front_left_IR, INPUT);
  pinMode(front_right_IR, INPUT);
  pinMode(rear_left_IR, INPUT);
  pinMode(rear_right_IR, INPUT);


  if(analogRead(basketLimitPin) < 500){
          digitalWrite(enaPin, LOW);  // active low
          digitalWrite(dirPin, HIGH);
          while(analogRead(basketLimitPin) < 500) {
            digitalWrite(stepPin, HIGH);
            delayMicroseconds(stepTime);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(stepTime);
          }
          digitalWrite(enaPin, HIGH);
  }
  digitalWrite(enaPin, LOW);
  digitalWrite(dirPin, LOW);
          for (int i = 0; i < stepsPerRevolution; i++) {
            digitalWrite(stepPin, HIGH);
            delayMicroseconds(stepTime);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(stepTime);
          }
  digitalWrite(enaPin, HIGH);
  //Something else
  delay(500);
}

//////////////////////////////////////////////////////////////////////////////////////
//                                Main Code Section                                 //
//////////////////////////////////////////////////////////////////////////////////////

void loop() {
  while(1) {
    button1State = digitalRead(button1Pin);             //read value from button1
    front_left_IR_state = analogRead(front_left_IR);    //read value from FL sensor and store value in front_left_IR_state 
    front_right_IR_state = analogRead(front_right_IR);  //read value from FR sensor and store value in front_right_IR_state
    rear_left_IR_state = analogRead(rear_left_IR);    //read value from FL sensor and store value in front_left_IR_state 
    rear_right_IR_state = analogRead(rear_right_IR);  //read value from FR sensor and store value in front_right_IR_state

    switch (cs) {
//state 0: wait for button press
      case 0:
        
          digitalWrite(LED, HIGH);
          skipStep = 1; //remember to change this functionality
          if (button1State == HIGH) {
             digitalWrite(LED,LOW);
             cs = 1;  // 1, normally
          } else {
             cs = 0;
          } 

          if(Serial.available()){
            r=r*(Serial.read()-'0');
            Serial.println(r);
            cs = 1;
          }
      break;

//state 1: nudge chassis forward
      case 1:
          analogWrite(left_wheel_enable, 180);
          analogWrite(right_wheel_enable, 180);
          
          digitalWrite(L1, LOW);
          digitalWrite(L2, HIGH);  
          digitalWrite(R1, LOW);
          digitalWrite(R2, HIGH); 
          delay(500);
          cs = 2;
      break;

//state 2: path chassis towards shelves along black line
      case 2:
            if(front_right_IR_state > 500 && front_left_IR_state < 500)
            {
//            Serial.println("turning left--right side IR off");
          
              digitalWrite(L1,LOW); 
              digitalWrite (L2,LOW);                      
              digitalWrite(R1,HIGH);
              digitalWrite (R2,LOW);
            
              analogWrite (left_wheel_enable, vSpeed);
           // analogWrite (right_wheel_enable, turn_speed);
            }
            
          //left side IR sensor detects black line, right side does not
          if(front_right_IR_state < 500 && front_left_IR_state > 500)
            {
//            Serial.println("turning right--left side IR off");
            
              digitalWrite(L1,HIGH); 
              digitalWrite (L2,LOW);                      
              digitalWrite(R1,LOW);
              digitalWrite (R2,LOW);
            
            //  analogWrite (left_wheel_enable, turn_speed);
              analogWrite (right_wheel_enable, vSpeed);
            
              delay(turn_delay);
            }
            
          //neither left or right IR sensors detect black line
          if(front_right_IR_state < 500 && front_left_IR_state < 500)
            {
//            Serial.println("going forward");
          
              digitalWrite(L1,LOW); 
              digitalWrite (L2,HIGH);                      
              digitalWrite(R1,LOW);
              digitalWrite (R2,HIGH);
             
              analogWrite (left_wheel_enable, vSpeed);
              analogWrite (right_wheel_enable, vSpeed);
            
              delay(turn_delay);
            } 
          
          //if front left and front right IR sensors detect line, stop motors
          if(front_right_IR_state > 500 && front_left_IR_state > 500) { 
//            Serial.println("stop");
              analogWrite (left_wheel_enable, 0);
              analogWrite (right_wheel_enable, 0);
            }
           if(front_right_IR_state > 500 && front_left_IR_state > 500) { 
              cs = 3;
            } else {
              cs = 2;
            }
      break;
      
//state 3: move arm upwards/downwards to pick up/put down cubby
      case 3:
        delay(500);
        digitalWrite(enaPin, LOW);  // active low
        if(haveBasket) {
          digitalWrite(dirPin, HIGH);
          do {
//            basketLimit = analogRead(basketLimitPin);
            digitalWrite(stepPin, HIGH);
            delayMicroseconds(stepTime);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(stepTime);
          } while(analogRead(basketLimitPin) < 500);
           haveBasket = 0;
        } else {
          digitalWrite(dirPin, LOW);
          for (int i = 0; i < stepsPerRevolution; i++) {
            digitalWrite(stepPin, HIGH);
            delayMicroseconds(stepTime);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(stepTime);
          }
          haveBasket = 1;
        }
        digitalWrite(enaPin, HIGH); // disable stepper controller after finish
        delay(500);
        cs = 4;
      break;

//state 4: nudge backwards
      case 4:
          analogWrite(left_wheel_enable, 180);
          analogWrite(right_wheel_enable, 180);
          
          digitalWrite(L1, HIGH);
          digitalWrite(L2, LOW);  
          digitalWrite(R1, HIGH);
          digitalWrite(R2, LOW); 
          delay(500);
          cs = 5;
      break;
	
//state 5: move chassis back towards start
      case 5:   
        //right side IR sensor detects black line, left side does not
        if(rear_right_IR_state > 500 && rear_left_IR_state < 500) {
//          Serial.println("right side IR off");
          digitalWrite(L1,LOW);
          digitalWrite(L2,LOW);                       
          digitalWrite(R1,HIGH);
          digitalWrite(R2,LOW);
          analogWrite (right_wheel_enable, vSpeed);
        }
        
        //left side IR sensor detects black line, right side does not
        if(rear_right_IR_state < 500 && rear_left_IR_state > 500) {
//          Serial.println("left side IR off");
          digitalWrite(L1,HIGH);
          digitalWrite(L2,LOW);                       
          digitalWrite(R1,LOW);
          digitalWrite(R2,LOW);
          analogWrite (left_wheel_enable, vSpeed);
          
          delay(turn_delay);
        }
        
        //neither left or right IR sensors detect black line
        if(rear_right_IR_state < 500 && rear_left_IR_state < 500) {
//          Serial.println("going backward");
          digitalWrite(L1,HIGH); 
          digitalWrite (L2,LOW);                      
          digitalWrite(R1,HIGH);
          digitalWrite (R2,LOW);
          analogWrite (left_wheel_enable, vSpeed);
          analogWrite (right_wheel_enable, vSpeed);
          
          delay(turn_delay);
        }
        
        //if front left and front right IR sensors detect line, stop motors
        if(rear_right_IR_state > 500 && rear_left_IR_state > 500) { 

          if(skipStep != 0) {
            digitalWrite(L1, HIGH);
            digitalWrite(L2, LOW);  
            digitalWrite(R1, HIGH);
            digitalWrite(R2, LOW); 
            analogWrite (left_wheel_enable, vSpeed);
            analogWrite (right_wheel_enable, vSpeed);
            delay(250);
            skipStep--;
          } else {
//          Serial.println("stop");
            digitalWrite(L1, LOW);
            digitalWrite(L2, LOW);  
            digitalWrite(R1, LOW);
            digitalWrite(R2, LOW); 
            analogWrite (left_wheel_enable, 0);
            analogWrite (right_wheel_enable, 0);
            cs = 0;
          }
        } else {
          cs = 5;
        }
        break;
        
      default:
        //cs = 0;
        break;
    }
  }
  delay(50); // may have to switch this back to 200?
}
