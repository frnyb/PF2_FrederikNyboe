#!/usr/bin/python3.7

import time
import RPi.GPIO as gpio
import hardware as hw

sensor_file = "sensor.txt"
motor_l_file = "motor_l.txt"
motor_r_file = "motor_r.txt"

hw.init_gpio()

pin_trigger = 17
pin_echo = 18
pin_motor_l = 9
pin_motor_r = 7

target_dist = 30
base_pwm_l = 95 #65 #50
base_pwm_r = 100 #70 #50
slow_pwm_l = 65 #35 #30
slow_pwm_r = 75 #50 #30

turn_sleep_l = 0.15 #0.2 #0.3
turn_sleep_r = 0.15 #0.2 #0.3
btw_turn_sleep = 0.3
btw_dist_sleep = 0.3
period_sleep = 0.005 # 0.01

dist_diff_thresh = 2

hw.init_sensor(hw.pin_trg, hw.pin_ech)
hw.init_motors(hw.pin_motor_l, hw.pin_motor_r)

def write_sensor(distance):
 with open(sensor_file, 'w') as f:
  f.write("Distance: " + str(distance))

def write_motor_l(pwm):
 with open(motor_l_file, 'w') as f:
  f.write("Motor l PWM: " + str(pwm))

def write_motor_r(pwm):
 with open(motor_r_file, 'w') as f:
  f.write("Motor r PWM: " + str(pwm))

def dist_debounce():
 dist = 0

 for i in range(5):
  dist = dist + hw.get_dist(target_dist)

 return dist / 5

def right():
 pwm_r.ChangeDutyCycle(slow_pwm_r)
 time.sleep(turn_sleep_r)
 pwm_r.ChangeDutyCycle(base_pwm_r)

def left():
 pwm_l.ChangeDutyCycle(slow_pwm_l)
 time.sleep(turn_sleep_l)
 pwm_l.ChangeDutyCycle(base_pwm_l)

pwm_l = gpio.PWM(hw.pin_motor_l, base_pwm_l)
pwm_r = gpio.PWM(hw.pin_motor_r, base_pwm_r)

pwm_l.start(base_pwm_l)
pwm_r.start(base_pwm_r)

write_motor_l(base_pwm_l)
write_motor_r(base_pwm_r)

while (True):
 dist_f = dist_debounce()
 write_sensor(dist_f)
 time.sleep(btw_dist_sleep)
 dist_s = dist_debounce()

 diff = dist_f - dist_s

 if (diff > dist_diff_thresh):
  left()
 elif (diff < -dist_diff_thresh):
  right()
  right()
 else:
  if(dist_s > target_dist):
   right()
   time.sleep(btw_turn_sleep)
   left()
  elif(dist_s < target_dist):
   left()
   time.sleep(btw_turn_sleep)
   right()
