from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pe=23
rec=24
GPIO.setup(pe,GPIO.OUT)
GPIO.setup(rec,GPIO.OUT)
GPIO.output(pe,0)
GPIO.output(rec,0)
def Recording():
	sleep(3)
	print("recording started")
	GPIO.output(pe, 1)
	sleep(10)
	GPIO.output(pe, 0)
	sleep(5)
	print("recording ended")
def play():
	print("Started")
	GPIO.output(rec, 1)
	sleep(1)
	GPIO.output(rec, 0)
	sleep(10)
	print("Ended")
while True:
	Recording()
	play()
