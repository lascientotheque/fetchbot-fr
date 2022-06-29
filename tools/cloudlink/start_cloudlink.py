#!/usr/bin/env python
# coding: utf-8

from cloudlink import CloudLink
import json

import gpiozero

import time
import motor_control

# Set motor speed
motor_speed=0.25
# Set duration
duration=0.5


def on_packet(message):
    
    print("cmd is {0}".format(message))
    
    # Vérifie si le message est une commande pour Raspberry
    
    print(message['val'])
    
    if message['val']=="forward":
        motor_control.forward(speed=motor_speed, duration=duration)
    
    if message['val']=="left":
        motor_control.turn_left(speed=motor_speed, duration=duration)

    if message['val']=="right":
        motor_control.turn_right(speed=motor_speed, duration=duration)

def on_connect(client):
    print("New client connected:", client["id"])

def on_error(error):
    print("Got an error: {0}".format(error))

def on_close(client):
    print("Client disconnected:", client["id"])

cl = CloudLink(debug=True)


cl.callback("on_packet", on_packet)
cl.callback("on_error", on_error)
cl.callback("on_connect", on_connect)
cl.callback("on_close", on_close)

cl.server()




