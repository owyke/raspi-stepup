import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  if(GPIO.input(21) == 0):
    print("koppla sig lite")
  else:
    print("koppla av")
  time.sleep(0.2)
GPIO.cleanup()



