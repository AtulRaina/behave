from sqlalchemy import create_engine
import pandas as pd
import urllib

'''Remember that we created a driver and refered that driver'''

engine = create_engine('mssql+pyodbc://test')

sql = 'Select * from orders'


records=pd.read_sql_query(sql,engine,chunksize=5)




print(records[['OrderID', 'ShipCountry']])
