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

# TO DO: perhaps include an id in the table
    def create(self, values):
        cursor = self.getCursor()
        sql = "INSERT INTO elec.unit (year, month, unit, cost_code) VALUES (%s, %s, %s, %s)"
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
    
    def findbyid(self, year, month):
        cursor = self.getCursor()
     
        sql = "SELECT * FROM elec.unit WHERE year = %s AND month = %s"
        print(f"Debug: year={year}, type={type(year)}")
        print(f"Debug: month={month}, type={type(month)}")

        cursor.execute(sql, (year, month))
        results = cursor.fetchall()
        self.closeAll()
        
        return results
    
    def update_unit(self, values):
        cursor = self.getCursor()  # Get the database cursor
        sql = "update elec.unit set unit=%s, cost_code=%s where year=%s and month=%s"
        print(f"Debug: SQL={sql}, values={values}")  # Debugging
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return "update"

    def delete(self, id):
        return "delete"
        

dbDAO = dbDAO()

