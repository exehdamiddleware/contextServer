#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
from threading import Thread
import paho.mqtt.client as paho
from publisher import *
import json
import datetime

class Subscriber(object):
    """docstring for subscriber."""
    def __init__(self):
        self.uuid = "b0013009-740b-4373-9aec-687c7818df06"


        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

        self.client.username_pw_set(username="middleware", password="exehda")
        self.client.connect(host="127.0.0.1", port=1883)

        # CLIENT_LOOP é colocado em uma thread para que o programa não entre em
        # loop e não add novos TOPICOS
        client_loop(self.client).start()

    def add_subscribe(self, topico):
        self.client.subscribe(topico, 0)

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    def on_message(self, mosq, obj, msg):
        print("-------Enviando para SC-------")
        msg_json = msg.payload.decode("utf-8")
        msg_json = json.loads(msg_json)
        #print(msg_json)
        
        msg_json["uuid_edge"] = self.uuid
        
        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        
        msg_json["date"] = date_str
       
        msg_json = json.dumps(msg_json)
     
        print(msg_json)
        topic = "teste"

        pub = Publisher("200.132.96.10", 1883)
        pub.on_publish(msg_json, topic)

        # print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mosq, obj, mid):
        #print("mid: "+str(mid))
        pass

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
