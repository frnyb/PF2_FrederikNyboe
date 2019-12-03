# PF2_FrederikNyboe
The major structure of the solution is as follows:
## main.sh
This script simply exposes a tcp server, that executes handler.sh on request and forwards the given input. This is done using socat.
## handler.sh
This script reads the given command from stdin and acts accordingly:
* When getdist is called, if the wallflower.py script is running, will return the latest distance value read from the file sensor.txt, which is written to from wallflower.py every time a distance measurement is made. If wallflower.py is not running, the script get_sensor.py will be executed to fetch one distance measurement.
* When getmotors is called, if the wallflower.py script is running, will return the latest motor pwm signal read from the files motor_l.txt and motor_r.txt. If not, 0 is returned for both motors.
* When start is called, if wallflower.py is not already running, it will be started and the process id will be saved in a temporary file, /tmp/wallflower.pid. If it is already running, nothing will happen.
* When stop is called, if wallflower.py is running, the saved process id will be fecthed from /tmp/wallflower.pid. The the script shutdown.py will be executed to ensure cleanup of the GPIOs. If wallflower.py is not running, nothing will happen.
## hardware.py
This module exposes methods for hardware control used by wallflower.py, shutdown.py, and get_dist.py.
## get_dist.py
This script executes one distance measurement and prints to stdout.
## shutdown.py
This script performs GPIO cleanup of the pins used.
## wallflower.py
This script, utilizing the methods of hardware.py, intializes the GPIOs and starts the controller. The controller is built around  base pwm for each motor and a slow pwm for each motor. Furthermore, a target distance from the wall has been set.
Two distance measurements are made with pause in between. If the difference is positive, it means that the robot is driving away from the wall. This is then counteracted by decreasing the PWM signal on the right motor to the slow pwm for a short time, changing the robots resulting direction to be more alligned with the wall. If the difference is negative, vice versa.
If the difference is close to zero within some threshold, it means that the robot is driving approxemately parallel to the wall. Then, instead of looking at the difference in distance, the absolute value of the last distance measurement is considered. If the distance is greater than the target distance, the robot drives first to the right, sleeps, and then drives to the left. This will result in the robot getting closer to the wall but staying with a course parallel to the wall, hopefully. If the distance to the wall is less than the target distance, vice versa.
This loops until the process is killed.
