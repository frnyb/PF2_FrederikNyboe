#!/bin/bash

read command

case $command in
 
 "getdist")
  if test -f "sensor.txt"
  then
   echo $(cat sensor.txt)
  else
   echo $(./get_sensor.py)
  fi
  ;;

 "getmotors")
  if test -f "motor_l.txt"
  then
   echo $(cat motor_l.txt)
   echo $(cat motor_r.txt)
  else
   echo "Motor l PWM: 0"
   echo "Motor r PWM: 0"
  fi
  ;;

 "start")
  if test -f "motor_l.txt"
  then
   echo "Already running."
  else
   ./wallflower.py &
   echo "$!" > /tmp/wallflower.pid
   echo "Started!"
  fi
  ;;

 "stop")
  if test -f "motor_l.txt"
  then
   kill $(cat /tmp/wallflower.pid)
   ./shutdown.py
   rm motor_l.txt motor_r.txt sensor.txt
   echo "Stopped!"
  else
   echo "Not started yet."
  fi
  ;;

 *)
  echo "Unknown command."
  ;;

esac
