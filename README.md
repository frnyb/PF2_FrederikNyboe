# PF2_FrederikNyboe
The major structure of the solution is as follows:
## main.sh
This script simply exposes a tcp server, that executes handler.sh on request and forwards the given input. This is done using socat.
## handler.sh
This script reads the given command from stdin and acts accordingly:
* When getdist is called, if the wallflower.py script is running, will return the latest distance value read from the file sensor.txt, which is written to from wallflower.py every time a distance measurement is made. If wallflower.py is not running, the script get_sensor.py will be executed to fetch one distance measurement.
* When getmotors is called, if the wallflower.py script is running, will return the latest motor pwm signal read from the files motor_signal
