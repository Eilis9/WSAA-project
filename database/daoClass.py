import mysql.connector
from dbconfig import mysql as config

class dbDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""


    def __init__(self):
        self.host = config['host']
        self.user = config['user']
        self.password = config['password']
        self.database = config['database']

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    def create(self, values):
        cursor = self.getCursor()
        sql = "INSERT INTO elec (name, age) VALUES (%s, %s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * FROM elec.unit"
        cursor.execute(sql)
        results = cursor.fetchall()
        self.closeAll()
        return results
    
    def findbyid(self, id):
        cursor = self.getCursor()       
        sql = "SELECT * FROM elec where id = %s"
        cursor.execute(sql, (id,))
        results = cursor.fetchall()
        self.closeAll()
        
        return results
    
    def update(self, id):
        return "update"

    def delete(self, id):
        return "delete"
        

dbDAO = dbDAO()

