/*
Author: Angelica Smith-Evans
        
The purpose of this code is to control the pathing of the robot but receiving 
input from proximity sensors, and changing the direction of the robot's 
trajectory through the motor control.
This code is currently in it's bare bones stages. I've written so far what needs to be completed
*/

//////////////////////////////////////////////////////////////////////////////////////
//                        Variable Declaration Section                              //
//////////////////////////////////////////////////////////////////////////////////////
//Speed Control
  int vSpeed = 120;                  // MAX 255
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

//Proximity Sensor Connections
  const int front_left_IR = A0;             // connect the front left IR sensor to pin A0
  const int front_right_IR = A1;            // connect the front right IR sensor to pin A1
  int front_left_IR_state = 0;              // variable to store the values from front left sensor
  int front_right_IR_state = 0;             // variable to store the values from front right sensor

//////////////////////////////////////////////////////////////////////////////////////
//                                Pin Set-up Section                                //
//////////////////////////////////////////////////////////////////////////////////////
void setup() 
{
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  Serial.begin(9600);                       // starts the serial monitor (data rate=9600bps)  
  delay(3000);                              // wait 3 seconds before starting main code execution
}

//////////////////////////////////////////////////////////////////////////////////////
//                             Pathing Control Section                              //
//////////////////////////////////////////////////////////////////////////////////////
void loop()
{

//need to do: implement a mode bit which traces if bot moving forward or backward
//            implement a counter which traces the mode bit switching to trace current point of the robot

  
front_left_IR_state = analogRead(front_left_IR);    //read value from FL sensor and store value in front_left_IR_state 
front_right_IR_state = analogRead(front_right_IR);  //read value from FR sensor and store value in front_right_IR_state

//right side IR sensor detects black line, left side does not
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
  
  delay(200); //run through code every .3 second
        
}//end of main
