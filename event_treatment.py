#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from db import *

class Event_Treatment(object):

    def __init__(self):
        pass  
    
    def add_object_ipc(self, object_ipc):
        print("ADD IPC")
        try:
            self.ipc = object_ipc
            self.device = Device_Process(self.ipc, self.process_configuration_db)
        except Exception as e:
            print(str(e))

    # Tipos de eventos:
    # - Agendamento de device
    # - Coleta ou atuação de um device
    # - Processamento de uma regra agendada
    # - Anúncio de recursos
    # - Recursos recebidos pelo GW
    # - Publicação
    # - Gathering - Action and collect

    def process_event(self, jsonObject, topic=None):

        try:
            db = Db("postgres","UFPEL2o19","127.0.0.1","5432", topic)

            # Salva os dados de configuração do DB
            if jsonObject['type'] == "configuration":
                # Salva os dados de configuração do Servidor de Borda

                if "edge_server" in jsonObject:
                    db.post_servidoresborda(jsonObject['edge_server']['uuid'], jsonObject['edge_server']['name'],jsonObject['edge_server']['ip'], jsonObject['edge_server']['port'] ,jsonObject['edge_server']['username'],jsonObject['edge_server']['password'])
                
                elif "gateway" in jsonObject:
                    # Salva os dados de configuração do ga
                    db.post_gateway(jsonObject['gateway']['uuid'],jsonObject['gateway']['name'], jsonObject['edge_server']['uuid'])
                    
                    # Salva os dados de configuração dos sensores              
                    for sensor in jsonObject['sensors']:
                        db.post_sensores(sensor['name'],sensor['uuid'],sensor['pin'],sensor['driver'],True,jsonObject['gateway']['uuid'],jsonObject['edge_server']['uuid'])


            # Salva os dados de coleta do DB
            elif jsonObject['type'] == "collect":
                db.post_publicacoes(jsonObject['date'],jsonObject['data'],jsonObject['uuid_sensor'])

        except Exception as e:
            print("Event Process")
            print(str(e))