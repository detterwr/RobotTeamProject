"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    
    # TODO: Implement the Snatch3r class as needed when working the sandbox exercises
    # (and delete these comments)

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor()
        self.ir_sensor = ev3.InfraredSensor()
        self.color = ev3.ColorSensor()

        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected
        assert  self.touch_sensor
        assert self.ir_sensor
        assert self.color

    def forward(self, inches, speed=100, stop_action='brake'):
        K = 360 / 4.5
        degrees_for_motor = K * inches
        self.left_motor.run_to_rel_pos(position_sp=degrees_for_motor,
                                       speed_sp=8*speed,
                                       stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees_for_motor,
                                        speed_sp=8*speed,
                                        stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")
    def backwards(self, inches, speed=100, stop_action='brake'):
        K = 360 / 4.5
        degrees_for_motor = K * inches
        self.left_motor.run_to_rel_pos(position_sp=-degrees_for_motor,
                                       speed_sp=-(8 * speed),
                                       stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=-degrees_for_motor,
                                        speed_sp=-(8 * speed),
                                        stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")
    def left(self, degrees, speed=100, stop_action='brake'):
        K = 360 / 4.5
        degree_for_motor = K * degrees
        self.right_motor.run_to_rel_pos(position_sp=degree_for_motor,
                                        speed_sp=8*speed,
                                        stop_action=stop_action)
        self.right_motor.wait_while("running")
    def right(self, degrees, speed=100, stop_action='brake'):
        K = 360 / 4.5
        degree_for_motor = K * degrees
        self.left_motor.run_to_rel_pos(position_sp=degree_for_motor,
                                        speed_sp=8 * speed,
                                        stop_action=stop_action)
    def spin_left(self, degrees, speed=100, stop_action='brake'):
        self.left_motor.run_to_rel_pos(position_sp=(degrees * -5), speed_sp=(speed * -8))
        self.right_motor.run_to_rel_pos(position_sp=(degrees * 5), speed_sp=(speed * 8))



    def spin_right(self, degrees, speed=100, stop_action='brake'):
        self.left_motor.run_to_rel_pos(position_sp=(degrees * -5), speed_sp=-(speed * -8))
        self.right_motor.run_to_rel_pos(position_sp=(degrees * 5), speed_sp=-(speed * 8))


    def go_forward(self, lspeed, rspeed):
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)


    def go_backward(self, lspeed, rspeed):
        lspeed = (-1) * lspeed
        rspeed = (-1 )* rspeed
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)


    def go_right(self, lspeed, rspeed):
        rspeed = (-1) * rspeed
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)


    def go_left(self, lspeed, rspeed):
        lspeed = (-1) * lspeed
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)

    def stop(self, lspeed, rspeed):
        lspeed = 0
        rspeed = 0
        self.left_motor.run_forever(speed_sp=lspeed)
        self.right_motor.run_forever(speed_sp=rspeed)


    def arm_up(self):
        position = 14.2 * 360
        self.arm_motor.run_to_abs_pos(position_sp=position, speed_sp=900)
        while True:
            if self.touch_sensor.is_pressed:
                break
        self.arm_motor.stop()
        ev3.Sound.beep().wait()


    def arm_down(self):
        position = 0 * 360
        self.arm_motor.run_to_abs_pos(position_sp=position, speed_sp=400)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()



    def shutdown(self):
        ev3.Sound.speak("aastaa  La veesta,....Bey bee").wait()
        self.running = False

    def say_geese(self):
        ev3.Sound.speak("geese").wait()

#Jabari's Project

    def ball_finder(self):
        while True:
            self.left_motor.run_forever(speed_sp=(100 * -8))
            self.right_motor.run_forever(speed_sp=(100 * 8))
            current_proximity = self.ir_sensor.proximity
            print("IR Distance = {}".format(current_proximity))
            if current_proximity <= 80:
                self.left_motor.stop()
                self.right_motor.stop()
                ev3.Sound.beep().wait()
                break
    def ball_obtain(self):
        while True:
            self.left_motor.run_forever(speed_sp=(100 * 8))
            self.right_motor.run_forever(speed_sp=(100 * 8))
            current_proximity = self.ir_sensor.proximity
            print("IR Distance = {}".format(current_proximity))
            if current_proximity <= 10:
                self.left_motor.stop()
                self.right_motor.stop()
                ev3.Sound.beep().wait()
                break

    def forward_to_goal(self, lspeed, rspeed):
        while True:
            current_color = self.color.color
            print("color = {}".format(current_color))
            self.left_motor.run_forever(speed_sp=lspeed)
            self.right_motor.run_forever(speed_sp=rspeed)
            if current_color == ev3.ColorSensor.COLOR_RED:
                self.right_motor.run_forever(speed_sp=rspeed)
                self.left_motor.run_forever(speed_sp=0)
                time.sleep(1)
                self.right_motor.stop()
                self.left_motor.stop()
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=lspeed)
                time.sleep(1.5)
                self.right_motor.stop()
                self.left_motor.stop()
            elif current_color == ev3.ColorSensor.COLOR_YELLOW:
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=lspeed)
                time.sleep(1)
                self.right_motor.stop()
                self.left_motor.stop()
                self.right_motor.run_forever(speed_sp=rspeed)
                self.left_motor.run_forever(speed_sp=0)
                time.sleep(1.5)
                self.right_motor.stop()
                self.left_motor.stop()
            elif current_color == ev3.ColorSensor.COLOR_BLUE:
                self.right_motor.stop()
                self.left_motor.stop()
                break


    def say_goal(self):
        ev3.Sound.speak("Gouaouaouaouaouaouaouaouaouaouaouaouaouaouaou al").wait()
#Will's Project

    # def search(self):
    #     closest_ir = 50
    #     cur_pos = 0
    #     closestpos = 0
    #     for p in range(12):
    #         if self.ir_sensor.proximity <= closest_ir:
    #             ev3.Sound.speak("Update", str(self.ir_sensor.proximity)).wait()
    #             closest_ir = self.ir_sensor.proximity
    #             closestpos = cur_pos
    #             cur_pos = cur_pos + 30
    #             self.spin_right(30, 30)
    #             self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    #         else:
    #             ev3.Sound.speak(str(closest_ir))
    #             cur_pos = cur_pos + 30
    #             self.spin_right(30, 30)
    #             self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    #
    #     self.spin_right(closestpos, 20)
    #     ev3.Sound.speak(str(closestpos)).wait()
    #     return closestpos*30

    #def grab(self):

    map_angle = 0
    map_dist = 0

    def search(self):
        current_pos = 0
        closest_ir = self.ir_sensor.proximity
        closest_pos = 0

        inc = 15
        rep = int(340/inc)

        for _ in range(rep):
            if self.ir_sensor.proximity <= closest_ir:
                ev3.Sound.beep().wait()
                closest_ir = self.ir_sensor.proximity
                closest_pos = current_pos
                ev3.Sound.beep().wait()
                current_pos = current_pos + inc
                self.spin_right(inc,20)
                self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
            else:
                #ev3.Sound.speak("No").wait()
                current_pos = current_pos + inc
                self.spin_right(inc,20)
                self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.speak(str(closest_pos)).wait()
        if closest_pos > 170:
            self.spin_right((-1*(340-closest_pos)),-30)
        else:
            self.spin_left(closest_pos, 30)


    def grab(self):
        distance = self.ir_sensor.proximity
        ev3.Sound.beep().wait()
        if distance > 50:
            self.forward(10, 40)
            self.arm_up()
            self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.backwards(distance/5, 40)
        else:
            distance = distance/5
            self.forward(distance, 40)

            self.arm_up()
            self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.backwards(distance, 40)

        btn = ev3.Button()
        while True:
            if btn.left:
                self.arm_down()
                break

        map_dist = distance





    def loop_forever(self):
        # This is a convenience method that I don't really recommend for most programs other than m5.
        #   This method is only useful if the only input to the robot is coming via mqtt.
        #   MQTT messages will still call methods, but no other input or output happens.
        # This method is given here since the concept might be confusing.
        self.running = True
        while self.running:
            time.sleep(0.1)
