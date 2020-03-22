from smbus2 import SMBus
import time

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

def signalToUno(sig):
	bus.write_byte(addr, sig)


def signalFromUno():
	bus.write_byte(addr, 0) #Polling dev #8 for data.
	sig = bus.read_byte(addr)
	return sig
