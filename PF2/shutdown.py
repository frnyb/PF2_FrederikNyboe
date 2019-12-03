#!/usr/bin/python3.7

import hardware as hw
import RPi.GPIO as gpio

hw.init_gpio()

hw.init_motors(hw.pin_motor_l, hw.pin_motor_r)
hw.init_sensor(hw.pin_trg, hw.pin_ech)

gpio.output(hw.pin_motor_l, False)
gpio.output(hw.pin_motor_r, False)

hw.cleanup()
