import RPi.GPIO as gpio
import time

pin_motor_l = 9
pin_motor_r = 7
pin_trg = 17
pin_ech = 18

def init_gpio():
 gpio.setmode(gpio.BCM)
 gpio.setwarnings(False)

def init_motors(pin_l, pin_r):
 gpio.setup(pin_motor_l, gpio.OUT)
 gpio.setup(pin_motor_r, gpio.OUT)

def init_sensor(pin_trigger, pin_echo):
 gpio.setup(pin_trigger, gpio.OUT)
 gpio.setup(pin_echo, gpio.IN)

def get_dist(target_dist):
 time.sleep(0.01)
 gpio.output(pin_trg, True)
 time.sleep(0.00001)
 gpio.output(pin_trg, False)

 start = time.time()
 stop = time.time()

 while gpio.input(pin_ech) == 0:
  start = time.time()
 
 while gpio.input(pin_ech) == 1:
  stop = time.time()
  if (stop - start) > 0.01:
   return target_dist
 elapsed = stop - start

 if elapsed >= 0.04:
  elapsed = 0

 dist = elapsed * 34326 / 2

 return dist

def cleanup():
 gpio.cleanup()
