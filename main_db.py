from db import *

db = Db("postgres","batata","127.0.0.1","5432","contextserver2")



db.list_table_fields("tipossensores")
# db.get_tipos_sensores("tipossensores")
# db.list_db()
# db.list_table_data("tipossensores")
# db.list_table_fields("tipossensores")             


# data = db.get_all_tipos_sensores()
# data = db.get_tipos_sensores("tiposensor_id = 1")
# print(data)

# db.post_tipos_sensores()

db.post_sensores("New_sensor", "5627e626-6821-4897-ab47-bc9dfa395b85", True)

# db.post_publicacoes("2019-09-22 20:16:45", 19.5, "3109381b-ad7f-41b2-8262-1c2061f338f9")