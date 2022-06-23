#!/usr/bin/env python
# coding: utf-8
# %%

# """
# 
# CloudLink Server
# 
# CloudLink server as of 0.1.7.2.
# For more information, please visit https://hackmd.io/G9q1kPqvQT6NrPobjjxSgg
# 
# """
# 

# %%


from cloudlink import CloudLink
import json

import gpiozero

import time
import motor_control


# %%


def on_packet(message):
    
    print("cmd is {0}".format(message))
    
    # Vérifie si le message est une commande pour Raspberry
    
    print(message['val'])
    
    if message['val']=="forward":
        motor_control.forward(speed=0.5, duration=0.5)
    
    if message['val']=="left":
        motor_control.turn_left(speed=0.5, duration=0.5)

    if message['val']=="right":
        motor_control.turn_right(speed=0.5, duration=0.5)

def on_connect(client):
    print("New client connected:", client["id"])

def on_error(error):
    print("Got an error: {0}".format(error))

def on_close(client):
    print("Client disconnected:", client["id"])


# %%


cl = CloudLink(debug=True)
# Instanciate CloudLink


# %%




cl.callback("on_packet", on_packet)
cl.callback("on_error", on_error)
cl.callback("on_connect", on_connect)
cl.callback("on_close", on_close)
# Specify callbacks to functions above

    #cl.setMOTD("CloudLink test", enable=True)
    # Turn on Message-Of-The-Day

cl.server()
# Run the server


# %%





# %%




