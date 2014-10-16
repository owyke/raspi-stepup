import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

MOTION_PIN=21

GPIO.setup(MOTION_PIN, GPIO.IN)


try:
	print "Looking for motion"
	while True:
		if GPIO.input(MOTION_PIN):
			print "Rora sig lite!"
		time.sleep(1)

except KeyboardInterrupt:
	print "Slut!"
	GPIO.cleanup()


