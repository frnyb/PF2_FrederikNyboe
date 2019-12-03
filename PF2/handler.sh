#!/bin/bash

command=$1

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

#if [ $command = "getdist" ]
#then
# if test -f "sensor.txt"
# then
#  echo $(cat sensor.txt)
# else
#  echo $(python3 get_sensor.py)
# fi
#elif [ $command = "getmotors" ]
#then
# if test -f "motor_l.txt"
# then
#  echo $(cat motor_l.txt)
#  echo $(cat motor_r.txt)
# else
#  echo "Motor l PWM: 0"
#  echo "Motor r PWM: 0"
# fi
#elif [ $command = "start" ]
# echo "hej"
#fi

# if test -f "motor_l.txt"
# then
#  echo "Already running."
# else
#  python3 wallflower.py &
#  echo "$!" > /tmp/wallflower.pid
#  echo "Started!"
# fi
#fi
#elif [ $command = "stop" ]
#then
# if test -f "motor_l.txt"
# then
#  kill $(cat /tmp/wallflower.pid)
#  rm motor_l.txt motor_r.txt sensor.txt
#  echo "Stopped!"
# else
#  echo "Not started yet."
# fi
#else
# echo "Unknown command."

