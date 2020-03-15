# encoded PID in progress
from gpiozero import Robot, DigitalInputDevice
from time import sleep

S_TIME = 1
L_F = 10
L_B = 9
R_F = 8
R_B = 7
E1 = 17
E2 = 18


class Encoder(object):
	def __init__(self, pin):
		self._value = 0
		encoder = DigitalInputDevice(pin)
		encoder.when_activated = self._increment
		encoder.when_deactivated = self._increment
	def reset(self):
		self._value = 0
	def _increment(self):
		self._value += 1

@property
	def value(self):
		return self._value
		

r = Robot((L_F, L_B),(R_F, R_B))

e1 = Encoder(E1)
e2 = Encoder(E2)

m1_speed = 1.0
m2_speed = 1.0

r.value = (m1_speed, m2_speed)

while True:
	print("e1 {} e2 {}".format(e1.value, e2.value))
	sleep(S_TIME)
	
	