#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as paho
import json
from threading import Thread
from event_treatment import *


class IPC(object):
    """docstring for IPC"""

    def __init__(self, username, password, host, port):
        # ============ Conexão com o Broker ============
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

        self.client.username_pw_set(username=username, password=password)
        self.client.connect(host=host, port=port)
        #==================================================
        
        # Este tópico é utilizado para receber os dados dos gateways       

        # Iniciaiza a conexão com o Broker
        client_loop(self.client).start()

    #==================================================
    # =============== Métodos da Borda ================ 
    def add_subscribe(self, topics):
        for topic in topics:
            try:
                self.client.subscribe(topic, 0)
    
            except Exception as e:
                print(str(e))

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    # Recebe a mensagem do broker e envia para o processamento de eventos para tratar a mensagem
    def on_message(self, mosq, obj, msg):
        print(msg.payload.decode("utf-8"))
        print("========================================================")
        self.event_treatment.process_event(json.loads(msg.payload.decode("utf-8")),msg.topic)
        
    # Envia uma publicação para o Servidor de Contexto
    def on_publish(self, topic, msg):
        # print(topic, msg)
        self.client.publish(topic=topic, payload=msg, qos=0, retain=False)
    

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()    
