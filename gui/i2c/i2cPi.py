from smbus2 import SMBus
import time

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

def signalToUno(sig):
	bus.write_byte(addr, sig)


def signalFromUno():
	sig = bus.read_byte(addr)
	return sig