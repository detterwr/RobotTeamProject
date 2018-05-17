
import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com
import robot_controller as robo

def main():

    mqtt_client = com.MqttClient()
    #mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Test")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    geese_button = ttk.Button(main_frame, text="Geese")
    geese_button.grid(row=0, column=0)
    # forward_button and '<Up>' key is done for your here...
    geese_button['command'] = lambda: print("Swans")
   # geese_button['command'] = lambda: mqtt_client.send_message("Pelicans")

    root.mainloop()

main()
