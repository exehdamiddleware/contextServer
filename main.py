#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import _thread
from subscriber import *
from publisher import *
import time
import json

# https://www.w3schools.com/python/python_json.asp

# Para gerar uuid, entre no link: https://www.uuidgenerator.net
# O tópico de publicação é o mesmo uuid, dessa forma garanto que dado sensor é publicado num único local 
sensor_uuid = "3aa027bd-4afc-461c-b353-c2535008f4ce"
gw_uuid = "3aa027bd-4afc-461c-b353-c2535008f4ce"

sub = Subscriber()
sub.add_subscribe('GW')

time.sleep(1) 


# JSON é composto pelos dados da borda, ip e port, e uuid do sensor
msg = {'uuid': sensor_uuid}
# convert into JSON:
msg = json.dumps(msg)

# Dados do gateway
topic = "GW_"+gw_uuid

pub = Publisher("127.0.0.1", 1883)
conta =0
while(conta < 10):
     pub.on_publish(msg, topic)
     conta = conta +1
