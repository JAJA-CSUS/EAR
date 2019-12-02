#include <Stepper.h>

const int stepsPerRevolution = 200;

Stepper myStepper(stepsPerRevolution, 2, 3, 4, 11);

void setup()
{
  //set speed to be 60 rpm
  myStepper.setSpeed(45);

  Serial.begin(9600);


  
}

void loop()
{
 //clockwise ==> going down
 myStepper.step(stepsPerRevolution);
 delay(800);

 //counterclockwise ==> going up
 myStepper.step(-stepsPerRevolution);
 delay(800);
}
