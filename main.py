#!/usr/bin/env python
# -*- coding: utf-8 -*-

from read_json import *
from ipc import *

read_json = Read_JSON()
jsonR = read_json.read("configuration")

# Informações de acesso ao Broker
username = jsonR['broker_mqtt']['user']
password = jsonR['broker_mqtt']['password']
host = jsonR['broker_mqtt']['ip']
port = jsonR['broker_mqtt']['port']


# Lista de tópicos + ES onde o Servidor de Contexto recebe as informações das Bordas


ipc = IPC(username, password, host, port)

ipc.on_publish("juca", "juca")