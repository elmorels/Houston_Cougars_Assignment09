#DatabaseManagement.py     

import pyodbc

class DatabaseManagement:
    def connectToDatabase(self):
        '''
        Establishes a connection to our secret service database
        @Return Connection object: The connection object
        '''
    
        conn = pyodbc.connect('Driver={SQL Server};'
                'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                'Database=GroceryStoreSimulator;'
                'uid=IS4010Login;'
                'pwd=P@ssword2;')

        return conn




