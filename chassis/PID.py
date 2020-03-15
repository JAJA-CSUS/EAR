# encoded PID in progress
from gpiozero import Robot, DigitalInputDevice
from time import sleep

S_TIME = 1
L_F = 10
L_B = 9
R_F = 8
R_B = 7


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
