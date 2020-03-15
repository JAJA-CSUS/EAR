from gpiozero import Robot, LineSensor
from time import sleep

L_F = 7
L_B = 8
R_F = 9
R_B = 10
LS = 17
RS = 27

robot = Robot(left=(L_F, L_B), right=(R_F, R_B))
l_sensor = LineSensor(LS)
r_sensor= LineSensor(RS)

speed = 0.68

def motor_speed():
    while True:
        l_detect  = int(l_sensor.value)
        r_detect = int(r_sensor.value)
        ## Stage 1
        if l_detect == 0 and r_detect == 0:
            l_motor = 1
            r_motor = 1
        ## Stage 2
        if l_detect == 0 and r_detect == 1:
            l_motor = -1
        if l_detect == 1 and r_detect == 0:
            r_motor = -1
        #print(r, l)
        yield (r_motor * speed, l_motor * speed)

robot.source = motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
l_sensor.close()
r_sensor.close()