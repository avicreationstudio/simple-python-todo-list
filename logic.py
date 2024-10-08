import sqlite3

# # -----------------------------------------
#        Mention your data base name
# # -----------------------------------------

TABLE_CONFIG = [
    ("PHONE_NO","VARCHAR(255)"),
    ("FIRST_NAME","VARCHAR(255)"),
    ("LAST_NAME","VARCHAR(255)"),
    ("SURNAME","VARCHAR(255)"),
    ("EMAIL","VARCHAR(255)"),
    ("JOB","VARCHAR(255)"),
    ("RELATIONSHIP","VARCHAR(255)"),
    ("ADDRESS","VARCHAR(255)"),
    ("BIRTHDAY","VARCHAR(255)"),
    ("NICK_NAME","VARCHAR(255)"),
]



class Logic:
    def createTable(db_name, tb_name):
        connection = sqlite3.connect(db_name)
        
        line1 = f"CREATE TABLE IF NOT EXISTS {tb_name} ("
        line2 = "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        line3 = " NOT NULL,".join(li[0] + " " + li[1] for li in TABLE_CONFIG )
        line4 = ");"
        query = " ".join([line1,line2,line3,line4])

        connection.execute(query)
        connection.commit()
        connection.close()
    
    def insertTable(db_name, tb_name, column, value):
        connection = sqlite3.connect(db_name)
        query = f"INSERT INTO {tb_name} ( {column} ) VALUES ( '{value}' );"
        connection.execute(query)
        connection.commit()
        connection.close()

    def deleteTable(db_name,tb_name, id):
        connection = sqlite3.connect(db_name)
        query = f"DELETE FROM {tb_name} WHERE id={id} ;"
        connection.execute(query)
        connection.commit()
        connection.close()
    
    def selectTable(db_name,tb_name):
        connection = sqlite3.connect(db_name)
        query = f"SELECT * FROM {tb_name};"
        cursor = connection.execute(query)
        table = []
        for row in cursor:
            table.append(row)
        connection.close()
        return table
    
        
    