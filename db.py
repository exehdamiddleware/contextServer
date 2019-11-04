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
    def post_sensores(self, name, uuid, pin, driver, status, gateway, board, type):
        cursor = self.connection.cursor()
        if (len(self.get_sensores(uuid)) ==0 ):
            data = self.get_servidoresborda(board)
            board_id = data[0][0]     
            data = self.get_gateway(gateway)
            gateway_id = data[0][0]

            postgres_insert_query = """ INSERT INTO sensores (nome, uuid, status, pin, driver, gateway_id, servidorborda_id, tiposensor_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (name, uuid, status, pin, driver, gateway_id, board_id, type)
            cursor.execute(postgres_insert_query, record_to_insert)

            self.connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into sensores table")
        else:
            msg = "Tentativa de inserir um sensor com UUID que já existe"
            postgres_insert_query = """ INSERT INTO error (msg, sensor_uuid, servidorborda_uuid, gateway_uuid) VALUES (%s,%s,%s,%s) """
            record_to_insert = (msg, uuid, board, gateway)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into error table")

    def get_sensores(self, uuid):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "select * from sensores where uuid = %s"

        cursor.execute(postgreSQL_select_Query, (uuid,))
        data = cursor.fetchall() 
        
        return data   
    
    def delete_all_sensores(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "delete from sensores"

        cursor.execute(postgreSQL_select_Query)
        self.connection.commit()
    #=====================================================================================================================
    def post_publicacoes(self, date_colect, value_colect, sensor_uuid):
        data = self.get_sensores(sensor_uuid)
        sensor_id = data[0][0]

        cursor = self.connection.cursor()

        postgres_insert_query = """ INSERT INTO publicacoes (datacoleta, valorcoletado, sensor_id) VALUES (%s,%s,%s)"""
        record_to_insert = (date_colect, value_colect, sensor_id)
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
    def post_servidoresborda(self, uuid, name, ip, port, username, password):
        print("POST")
        print(uuid, name, ip, port, username, password)
        cursor = self.connection.cursor()
        if(len(self.get_servidoresborda(uuid))==0):
            postgres_insert_query = """ INSERT INTO servidoresborda (nome, uuid, ip, porta, usuario, senha) VALUES (%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (name, uuid, ip, port, username, password)
            cursor.execute(postgres_insert_query, record_to_insert)

            self.connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into ServidoresBorda table")
        else:
            msg = 'Tentativa de inserir um servidor de borda com UUID que já existe'
            postgres_insert_query = """ INSERT INTO error (msg, servidorborda_uuid) VALUES (%s,%s)"""
            record_to_insert = (msg, uuid)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into error table")

    def get_servidoresborda(self, uuid):
        cursor = self.connection.cursor()

        postgreSQL_select_Query = "select * from servidoresborda where uuid = %s" 

        cursor.execute(postgreSQL_select_Query, (uuid,))
        data = cursor.fetchall() 
        
        return data


    def delete_all_servidoresborda(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "delete from servidoresborda"

        cursor.execute(postgreSQL_select_Query)
        self.connection.commit()
    
    def post_gateway(self, uuid, name, board_uuid):
        cursor = self.connection.cursor()
        if(len(self.get_gateway(uuid))==0):
            data = self.get_servidoresborda(board_uuid)
            board_id = data[0][0]
            postgres_insert_query = """ INSERT INTO gateways (uuid, nome, servidorborda_id) VALUES (%s,%s,%s)"""
            record_to_insert = (uuid, name, board_id)
            cursor.execute(postgres_insert_query, record_to_insert)

            self.connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into gateways table")
        else:
            msg = "Tentativa de inserir um gateway com UUID que já existe"
            postgres_insert_query = """ INSERT INTO error (msg, gateway_uuid) VALUES (%s,%s)"""
            record_to_insert = (msg, uuid)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into error table")
    
    def get_gateway(self, uuid):
        cursor = self.connection.cursor()

        postgreSQL_select_Query = "select * from gateways where uuid = %s"
        cursor.execute(postgreSQL_select_Query, (uuid,))
        data = cursor.fetchall() 
        
        return data


    def delete_all_gateway(self):
        cursor = self.connection.cursor()
        postgreSQL_select_Query = "delete from gateways"

        cursor.execute(postgreSQL_select_Query)
        self.connection.commit()
    
    def post_error(self, msg, sensor, board, gateway, driver):
        cursor = self.connection.cursor()
        postgres_insert_query = """ INSERT INTO error (msg, sensor_uuid, servidorborda_uuid, gateway_uuid, driver) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (msg, sensor, board, gateway, driver)
        cursor.execute(postgres_insert_query, record_to_insert)
        self.connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into error table")

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
