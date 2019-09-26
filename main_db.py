
from db import *

db = Db("postgres","UFPEL2o19","127.0.0.1","5432","context_server2")

print(len(db.get_gateway("042b8880-9f52-4042-9c06-e0f6f00e22b7"))==0)




#data = db.get_servidoresborda("3aa027bd-4afc-461c-b353-c2535008f4ce")

#print(data)
#db.delete_all_publicacoes()
#db.delete_all_sensores()

#db.post_gateway("3aa027bd-4afc-461c-b353-c2535008f4ce", "SB1")



#db.list_table_fields("tipossensores")

#print(db.get_all_sensores())
#print("=========================")

#db.post_sensores("Sensor_1","c08042cf-8610-4bd4-8bea-6320ce7c613b",True)

#print(db.get_all_sensores())

# db.get_tipos_sensores("tipossensores")
# db.list_db()
# db.list_table_data("tipossensores")
# db.list_table_fields("tipossensores")             


# data = db.get_all_sensores()
# data = db.get_tipos_sensores("tiposensor_id = 1")


#data = db.get_all_publicacoes()
#print(data)

#print("===========================================")

#db.delete_all_publicacoes()
#data = db.get_all_publicacoes()
#print(data)
#print("===========================================")
# db.post_tipos_sensores()

# db.post_sensores("New_sensor", "5627e626-6821-4897-ab47-bc9dfa395b85", True)

# db.post_publicacoes("2019-09-22 20:16:45", 19.5, "3109381b-ad7f-41b2-8262-1c2061f338f9")
