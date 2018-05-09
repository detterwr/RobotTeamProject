"""
Functions for moving the robot FORWARD and BACKWARD.
Authors: David Fisher, David Mutchler and Jabari-Aman Delemore.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implment forward_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for forward_by_time.
#   Then repeat for forward_by_encoders.
#   Then repeat for the backward functions.

import ev3dev.ev3 as ev3
import time


def test_forward_backward():
    """
    Tests the forward and backward functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets inches and runs forward_by_time.
      3. Same as #2, but runs forward_by_encoders.
      4. Same as #1, 2, 3, but tests the BACKWARD functions.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    assert left_motor.connected
    assert right_motor.connected
    speed_sp = int(input('Input the speed of the motors:'))
    time_s = int(input('Input time for motors to run:'))
    position_sp = int(input('distance for robot to travel:'))
    forward_seconds(time_s, speed_sp, 'brake')
    backward_seconds(time_s, speed_sp, 'brake')
    forward_by_time(position_sp, speed_sp, 'brake')
    backward_by_time(position_sp, speed_sp, 'brake')
    ev3.Sound.beep().wait()
    forward_by_encoders(position_sp, speed_sp, 'brake')
    backward_by_encoders(position_sp, speed_sp, 'brake')
    ev3.Sound.beep().wait()
def forward_seconds(seconds, speed, stop_action):
    """
    Makes the robot move forward for the given number of seconds at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the given stop_action.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    left_motor.run_forever(speed_sp=(speed * 8))
    right_motor.run_forever(speed_sp=(speed * 8))
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop()


def forward_by_time(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    time = (inches/speed)*4.5
    left_motor.run_timed(speed_sp=speed, time_sp=time)
    right_motor.run_timed(speed_sp=speed, time_sp=time)

def forward_by_encoders(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    left_motor.run_to_rel_pos(position_sp=inches, speed_sp=speed)
    right_motor.run_to_rel_pos(position_sp=inches, speed_sp=speed)
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)
def backward_seconds(seconds, speed, stop_action):
    """ Calls forward_seconds with negative speeds to achieve backward motion. """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    left_motor.run_forever(speed_sp=-(speed * 8))
    right_motor.run_forever(speed_sp=-(speed * 8))
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop()
def backward_by_time(inches, speed, stop_action):
    """ Calls forward_by_time with negative speeds to achieve backward motion. """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    time = (inches/speed)*4.5
    left_motor.run_timed(speed_sp=-speed, time_sp=time)
    right_motor.run_timed(speed_sp=-speed, time_sp=time)
def backward_by_encoders(inches, speed, stop_action):
    """ Calls forward_by_encoders with negative speeds to achieve backward motion. """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    left_motor.run_to_rel_pos(position_sp=-inches, speed_sp=speed)
    right_motor.run_to_rel_pos(position_sp=-inches, speed_sp=speed)
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)


test_forward_backward()