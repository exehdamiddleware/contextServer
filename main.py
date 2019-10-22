#!/usr/bin/env python
# -*- coding: utf-8 -*-

from read_json import *

read_json = Read_JSON()
jsonR = json_read.read("configuration")

# Informações de acesso ao Broker
username = jsonR['broker_mqtt']['user']
password = jsonR['broker_mqtt']['password']
host = jsonR['broker_mqtt']['ip']
port = jsonR['broker_mqtt']['port']


# Lista de tópicos + ES onde o Servidor de Contexto recebe as informações das Bordas
topics = jsonR['topics']
topics.append("ES")


event_treatment = Event_Treatment(jsonR)
ipc = IPC(event_treatment, username, password, host, port, topics)

event_treatment.add_object_ipc(ipc)