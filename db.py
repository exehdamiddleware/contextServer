import psycopg2

class Db(object):
   
    def __init__(self, user, password, host, port, database):
        self.connection = psycopg2.connect(user = user,
                                  password = password,
                                  host = host,
                                  port = port,
                                  database = database)

    def list_db(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
        
        for table in cursor.fetchall():
            print(table)

    def list_table(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from usuarios"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 
   
        print("Print each row and it's columns values")
        for row in mobile_records:
            print("teste", row)

    


# try:
#     connection = psycopg2.connect(user = "postgres",
#                                   password = "batata",
#                                   host = "127.0.0.1",
#                                   port = "5432",
#                                   database = "contextserver")

#     cursor = connection.cursor()
#     # Print PostgreSQL Connection properties
#     # print ( connection.get_dsn_parameters(),"\n")

#     # Print PostgreSQL version
#     # cursor.execute("SELECT version();")
#     # record = cursor.fetchone()
#     # print("You are connected to - ", record,"\n")
#     cursor.execute("""SELECT table_name FROM information_schema.tables
#        WHERE table_schema = 'public'""")
#     for table in cursor.fetchall():
#         print(table)

# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
# finally:
#     #closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")