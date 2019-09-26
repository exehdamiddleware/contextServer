from db import *

db = Db("postgres","UFPEL2o19","127.0.0.1","5432","context_server2")

db.delete_all_publicacoes()
db.delete_all_sensores()
db.delete_all_gateway()
db.delete_all_servidoresborda()

