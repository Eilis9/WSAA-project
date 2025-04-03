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
        # elec unit table
        sql_1 = "SELECT * FROM elec.unit ORDER BY year ASC, month ASC"
        cursor.execute(sql_1)
        results_1 = cursor.fetchall()
        # Get column names from the cursor description
        column_names = [desc[0] for desc in cursor.description]
        # Convert each row into a dictionary
        json_results = [dict(zip(column_names, row)) for row in results_1]
        # cost table
        #sql_2 = "SELECT * FROM elec.cost"
        #cursor.execute(sql_2)
        #results_2 = cursor.fetchall()
        self.closeAll()
        #return f"unit table {results_1} cost table {results_2}"
        return json_results
    
    def findbyid(self, year, month):
        cursor = self.getCursor()  
        sql = "SELECT * FROM elec.unit WHERE year = %s AND month = %s"
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
    
    # Delete an entry based on year and month
    def delete(self, year, month):
        cursor = self.getCursor()  
        sql = "DELETE from elec.unit * WHERE year = %s AND month = %s"
        cursor.execute(sql, (year, month))
        self.closeAll()        
        return f"deleted entry for {year}, {month}"
        

dbDAO = dbDAO()

