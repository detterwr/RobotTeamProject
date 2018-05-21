"""Author: Jabari-Aman Delemore"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()
    # Left Speed Value
    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "800")
    left_speed_entry.grid(row=1, column=0)
    # Right Speed Value
    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "800")
    right_speed_entry.grid(row=1, column=2)
    # Forward
    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: forward(mqtt_client, left_speed_entry, right_speed_entry))
    # Left
    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: left(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: left(mqtt_client, left_speed_entry, right_speed_entry))
    # Stop
    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: stop(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: stop(mqtt_client, left_speed_entry, right_speed_entry))
    # Right
    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: right(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: right(mqtt_client, left_speed_entry, right_speed_entry))
    # Backward
    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: backwards(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: backwards(mqtt_client, left_speed_entry, right_speed_entry))
    # Arm Up
    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))
    # Arm Down
    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    # Find Ball
    f_button = ttk.Button(main_frame, text="Find Ball")
    f_button.grid(row=7, column=2)
    f_button['command'] = (lambda: find_ball(mqtt_client))

    # Say Goal
    g_button = ttk.Button(main_frame, text="Goal")
    g_button.grid(row=7, column=1)
    g_button['command'] = (lambda: goal(mqtt_client))

    g_button = ttk.Button(main_frame, text="Obtain Ball")
    g_button.grid(row=7, column=0)
    g_button['command'] = (lambda: grab_ball(mqtt_client))

    root.mainloop()


# Tkinter Functions
def forward(mqtt_client, left_speed_entry, right_speed_entry):
    left_speed_entry.get()
    print(left_speed_entry.get())
    right_speed_entry.get()
    print(right_speed_entry.get())
    print("I'm reving up!")
    mqtt_client.send_message("go_forward", (int(left_speed_entry.get()), int(right_speed_entry.get())))


def left(mqtt_client, left_speed_entry, right_speed_entry):
    left_speed_entry.get()
    print(left_speed_entry.get())
    right_speed_entry.get()
    print(right_speed_entry.get())
    print("I'm reving left!")
    mqtt_client.send_message("go_left", (int((left_speed_entry.get())), int(right_speed_entry.get())))


def right(mqtt_client, left_speed_entry, right_speed_entry):
    left_speed_entry.get()
    print(left_speed_entry.get())
    right_speed_entry.get()
    print(right_speed_entry.get())
    print("I'm reving right!")
    mqtt_client.send_message("go_right", (int(left_speed_entry.get()), int((right_speed_entry.get()))))


def stop(mqtt_client, left_speed_entry, right_speed_entry):
    left_speed_entry.get()
    print(left_speed_entry.get())
    right_speed_entry.get()
    print(right_speed_entry.get())
    print("I'm stopping!")
    mqtt_client.send_message("stop", (int(left_speed_entry.get()), int(right_speed_entry.get())))


def backwards(mqtt_client, left_speed_entry, right_speed_entry):
    left_speed_entry.get()
    print(left_speed_entry.get())
    right_speed_entry.get()
    print(right_speed_entry.get())
    print("I'm backing up!")
    mqtt_client.send_message("go_backward", (int((left_speed_entry.get())), int((right_speed_entry.get()))))


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


def find_ball(mqtt_client):
    print("Finding Ball")
    mqtt_client.send_message("ball_finder")


def goal(mqtt_client):
    print("Score")
    mqtt_client.send_message("say_goal")


def grab_ball(mqtt_client):
    print("Obtaining the ball.")
    mqtt_client.send_message("ball_obtain")


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


main()
