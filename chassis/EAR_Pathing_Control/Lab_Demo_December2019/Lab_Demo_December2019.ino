/*
Author: Angelica Smith-Evans
        Jeremy Shaw

*/

#include <Stepper.h>

//////////////////////////////////////////////////////////////////////////////////////
//                        Variable Declaration Section                              //
//////////////////////////////////////////////////////////////////////////////////////
//Speed Control
  int vSpeed = 190;                  // MAX 255
  int turn_speed = 100;              // MAX 255 
  int turn_delay = 10;
  
//Motor Control Connections
// Left Wheel Motor
  int left_wheel_enable = 10;        //enB pin connected to UNO pin 10 to enable LW Motor Driver
  int in1 = 9;                       //in1 pin connected to UNO pin 9 to control LW Motor
  int in2 = 8;                       //in2 pin connected to UNO pin 8 to control LW Motor
// Right Wheel Motor
  int right_wheel_enable = 5;        //enA pin connected to UNO pin 5 to enable RW Motor Driver
  int in3 = 7;                       //in3 pin connected to UNO pin 7 to control RW Motor
  int in4 = 6;                       //in4 pin connected to UNO pin 6 to control RW Motor

// Stepper enables
  int StepBridged = 12;

//Proximity Sensor Connections
  const int front_left_IR = A0;             // connect the front left IR sensor to pin A0
  const int front_right_IR = A1;            // connect the front right IR sensor to pin A1
  int front_left_IR_state = 0;              // variable to store the values from front left sensor
  int front_right_IR_state = 0;             // variable to store the values from front right sensor
  
//LED
  const int LED = 13;
//Buttons
  const int button1Pin = A2;                // button1Pin connected to UNO pin A2
  int button1State = 0;                     // variable for reading the pushbutton status, initially low

//Switch Case Variables
  int ns = 0;
  int cs = 0;
  
//Stepper Control
  const int stepsPerRevolution = 200;
  Stepper myStepper(stepsPerRevolution, 2, 3, 4, 11);
  
void setup() 
{
  // initialize serial communication:
  Serial.begin(9600);
  
  //initialize the button pins
  pinMode(button1Pin, INPUT);
  
  pinMode(LED, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  myStepper.setSpeed(45);

  delay(3000);

}

void loop() {
  while(1)
  {
    button1State = digitalRead(button1Pin);             //read value from button1
    Serial.print("Button 1 state = ");
    Serial.print(button1State);
    Serial.print("; cs ");
    Serial.println(cs);
    front_left_IR_state = analogRead(front_left_IR);    //read value from FL sensor and store value in front_left_IR_state 
    front_right_IR_state = analogRead(front_right_IR);  //read value from FR sensor and store value in front_right_IR_state
      //switch to state 1 if button1 is pressed
      switch (cs) {
        case 0:
            digitalWrite(LED, HIGH);
            
            if (button1State == HIGH)
            {
               digitalWrite(LED,LOW);
               cs = 1;
            } else {
               cs = 0;
            } 
        break;

        //nudge forward
        case 1:
            analogWrite(left_wheel_enable, 180);
            analogWrite(right_wheel_enable, 180);
            
            digitalWrite(in1, LOW);
            digitalWrite(in2, HIGH);  
            digitalWrite(in3, LOW);
            digitalWrite(in4, HIGH); 
            delay(500);
            cs = 2;
        break;

        //path towards shelves along black line
        case 2:
              if(front_right_IR_state > 500 && front_left_IR_state < 500)
              {
              Serial.println("turning left--right side IR off");
            
              digitalWrite(in1,LOW); 
              digitalWrite (in2,LOW);                      
              digitalWrite(in3,HIGH);
              digitalWrite (in4,LOW);
            
              analogWrite (left_wheel_enable, vSpeed);
             // analogWrite (right_wheel_enable, turn_speed);
              }
              
            //left side IR sensor detects black line, right side does not
            if(front_right_IR_state < 500 && front_left_IR_state > 500)
              {
              Serial.println("turning right--left side IR off");
              
              digitalWrite(in1,HIGH); 
              digitalWrite (in2,LOW);                      
              digitalWrite(in3,LOW);
              digitalWrite (in4,LOW);
            
            //  analogWrite (left_wheel_enable, turn_speed);
              analogWrite (right_wheel_enable, vSpeed);
            
              delay(turn_delay);
              }
              
            //neither left or right IR sensors detect black line
            if(front_right_IR_state < 500 && front_left_IR_state < 500)
              {
              Serial.println("going forward");
            
              digitalWrite(in1,LOW); 
              digitalWrite (in2,HIGH);                      
              digitalWrite(in3,LOW);
              digitalWrite (in4,HIGH);
             
              analogWrite (left_wheel_enable, vSpeed);
              analogWrite (right_wheel_enable, vSpeed);
            
              delay(turn_delay);
              } 
            
            //if front left and front right IR sensors detect line, stop motors
            if(front_right_IR_state > 500 && front_left_IR_state > 500)
              { 
              Serial.println("stop");
              
              analogWrite (left_wheel_enable, 0);
              analogWrite (right_wheel_enable, 0);
              }
             if(front_right_IR_state > 500 && front_left_IR_state > 500)
              { 
                cs = 3;
              } else
              {
                cs = 2;
              }
        break;
        
        //move arm upwards to pick up cubby
        case 3:
          // counterclockwise ==> going up
          myStepper.step(stepsPerRevolution);
          Serial.println("STEPPER!");
          delay(800);
          cs = 4;
        break;

        //nudge backwards
        case 4:
            analogWrite(left_wheel_enable, 180);
            analogWrite(right_wheel_enable, 180);
            
            digitalWrite(in1, HIGH);
            digitalWrite(in2, LOW);  
            digitalWrite(in3, HIGH);
            digitalWrite(in4, LOW); 
            delay(500);
            cs = 5;
        break;

        case 5:
          // go back to start.

          
          //right side IR sensor detects black line, left side does not
          if(front_right_IR_state > 500 && front_left_IR_state < 500) {
            Serial.println("right side IR off");
            
            digitalWrite (in1,LOW);
            digitalWrite(in2,LOW);                       
            digitalWrite (in3,HIGH);
            digitalWrite(in4,LOW);
            
            analogWrite (left_wheel_enable, vSpeed);
            analogWrite (right_wheel_enable, turn_speed);
          }
          
          //left side IR sensor detects black line, right side does not
          if(front_right_IR_state < 500 && front_left_IR_state > 500) {
            Serial.println("left side IR off");
            
            digitalWrite (in1,HIGH);
            digitalWrite(in2,LOW);                       
            digitalWrite (in3,LOW);
            digitalWrite(in4,LOW);
            
            analogWrite (left_wheel_enable, turn_speed);
            analogWrite (right_wheel_enable, vSpeed);
            
            delay(turn_delay);
          }
          
          //neither left or right IR sensors detect black line
          if(front_right_IR_state < 500 && front_left_IR_state < 500) {
            Serial.println("going backward");
            
            digitalWrite(in1,HIGH); 
            digitalWrite (in2,LOW);                      
            digitalWrite(in3,HIGH);
            digitalWrite (in4,LOW);
            
            analogWrite (left_wheel_enable, vSpeed);
            analogWrite (right_wheel_enable, vSpeed);
            
            delay(turn_delay);
          }
          
          //if front left and front right IR sensors detect line, stop motors
          if(front_right_IR_state > 500 && front_left_IR_state > 500) { 
            Serial.println("stop");
            
            analogWrite (left_wheel_enable, 0);
            analogWrite (right_wheel_enable, 0);
            cs = 0;
          } else {
            cs = 5;
          }

          break;
          
        default:
          //cs = 0;
          break;
      }
  }
  //ns = cs;
  delay(50); // may have to switch this back to 200?
}
