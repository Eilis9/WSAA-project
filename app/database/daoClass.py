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


    def create(self, reading):
        cursor = self.getCursor()
        sql = "INSERT INTO elec.unit (year, month, unit, cost_code) VALUES (%s, %s, %s, %s)"
        values = (reading.get("year"), reading.get("month"), reading.get("unit"), reading.get("cost_code"))
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        reading["id"] = newid
        self.closeAll()
        return newid
    
    def getAll(self):
        cursor = self.getCursor()
        # elec unit table
        # sql_1 = "SELECT * FROM elec.unit ORDER BY year ASC, month ASC"
        # Joins the data from the 2 database tables to get the reading and cost info
        sql_1= """
        SELECT elec.unit.id, elec.unit.year, elec.unit.month, elec.unit.unit, 
        elec.cost.cost_code, elec.cost.supplier, round(elec.cost.s_charge, 3) as s_charge, round(elec.cost.unit_cost, 3) as unit_cost from elec.unit
        INNER JOIN elec.cost 
        ON elec.cost.cost_code = elec.unit.cost_code
        ORDER by year ASC, month ASC;"""
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
    
    def findbyyear(self, year):
        cursor = self.getCursor()  
        sql = "SELECT unit, month FROM elec.unit WHERE year = %s"
        cursor.execute(sql, (year,))
        results = cursor.fetchall()
        self.closeAll()        
        return results


    def update_unit(self, id, reading):
        
        cursor = self.getCursor()  # Get the database cursor
        
        sql = "update elec.unit set year=%s, month=%s, unit=%s, cost_code=%s where id=%s"
        values = (reading.get("year"), reading.get("month"), reading.get("unit"), reading.get("cost_code"), id)
        print(f"Debug: SQL={sql}, values={values}")  # Debugging
        
        result = cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return result
    
    # Delete an entry based on id
    def delete(self, id):
        print(f"Debug: delete id={id}")  # Debugging
        cursor = self.getCursor()  
        sql = "DELETE from elec.unit WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()        
        return f"deleted entry for {id}"
        

        

dbDAO = dbDAO()

