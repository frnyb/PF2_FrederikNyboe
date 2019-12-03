#!/usr/bin/Python3.7

import hardware as hw

hw.init_gpio()

hw.init_sensor(hw.pin_trg, hw.pin_ech)

print("Distance: " + str(hw.get_dist(30)))
