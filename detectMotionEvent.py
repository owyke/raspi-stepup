import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

MOTION_PIN=21

GPIO.setup(MOTION_PIN, GPIO.IN)

def motionDetected(PIN):
	if GPIO.input(MOTION_PIN) == 1:
		print "Rising pin " + str(PIN) 
	else:
		print "Dropping pin " + str(PIN)

try:
	GPIO.add_event_detect(MOTION_PIN, GPIO.BOTH, callback=motionDetected)	
	while 1:	
		time.sleep(10000)

except KeyboardInterrupt:
	print "Slut!"
	GPIO.cleanup()


