from db import *

db = Db("postgres","batata","127.0.0.1","5432","contextserver")

# db.list_db()
db.list_table()