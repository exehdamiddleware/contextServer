#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
from threading import Thread
import paho.mqtt.client as paho

class Publisher(object):
    """docstring for subscriber."""
    def __init__(self, ip, port):
        self.client = paho.Client()
        self.client.username_pw_set(username="middleware", password="exehda")
        self.client.connect(ip, port)

    def on_publish(self, msg, topic):
        self.client.publish(topic=topic, payload=msg, qos=0, retain=False)
