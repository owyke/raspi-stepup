import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)

ledstatus = False

def toggleLed(chan):
  global ledstatus 
  ledstatus = not ledstatus
  GPIO.output(4, ledstatus)


GPIO.add_event_detect(21, GPIO.RISING, callback=toggleLed, bouncetime=300)


raw_input("Enter to exit.")
GPIO.cleanup()


