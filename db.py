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

    def list_table_data(self, table):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from "+table

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall() 
   
        for row in data:
            print(row)
            print("-------------------------------------")

    def list_table_fields(self, table):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from "+table
        cursor.execute(postgreSQL_select_Query)
        # cursor.execute("Select * FROM usuarios")

        colnames = [desc[0] for desc in cursor.description]
        print(colnames)

    #=====================================================================================================================
    def post_tipos_sensores(self):
        cursor = self.connection.cursor()

        # postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
        postgres_insert_query = """ INSERT INTO tipossensores (nome, descricao, unidade, tipo) VALUES (%s,%s,%s,%s)"""
        record_to_insert = ('juca', 'One Plus 6', '950', 950)
        cursor.execute(postgres_insert_query, record_to_insert)

        self.connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into tipossensores table")

    def get_all_tipos_sensores(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from tipossensores"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall() 
        
        return data    
    
    def get_tipos_sensores(self, rule):
        cursor = self.connection.cursor()

        postgreSQL_select_Query = "select * from tipossensores where " + rule

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall() 
        
        return data
    #=====================================================================================================================
    def post_sensores(self, name, uuid, status):
        cursor = self.connection.cursor()

        postgres_insert_query = """ INSERT INTO sensores (nome, uuid, status) VALUES (%s,%s,%s)"""
        record_to_insert = (name, uuid, status)
        cursor.execute(postgres_insert_query, record_to_insert)

        self.connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into sensores table")

    def get_all_sensores(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from sensores"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall() 
        
        return data   

    #=====================================================================================================================
    def post_publicacoes(self, date_colect, value_colect, sensor_uuid):
        cursor = self.connection.cursor()

        postgres_insert_query = """ INSERT INTO publicacoes (datacoleta, valorcoletado, sensor_uuid) VALUES (%s,%s,%s)"""
        record_to_insert = (date_colect, 29, sensor_uuid)
        cursor.execute(postgres_insert_query, record_to_insert)

        self.connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into publicacoes table")

    def get_all_publicacoes(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from publicacoes"

        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall() 
        
        return data

    def delete_all_publicacoes(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "delete from publicacoes"

        cursor.execute(postgreSQL_select_Query)
        self.connection.commit()

    #=====================================================================================================================
    def post_servidoresborda(self, uuid, name, value_colect, sensor_uuid):
        cursor = self.connection.cursor()

        postgres_insert_query = """ INSERT INTO publicacoes (datacoleta, valorcoletado, sensor_uuid) VALUES (%s,%s,%s)"""
        record_to_insert = (date_colect, 29, sensor_uuid)
        cursor.execute(postgres_insert_query, record_to_insert)

        self.connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into publicacoes table")



    


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