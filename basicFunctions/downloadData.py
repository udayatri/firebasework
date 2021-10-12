from databaseFunctions.createAllTables import createAllTables
import pandas as pd
import sqlite3
from flask import send_file

   
def download():   
    filePath = "dataTable.xlsx"
    #create sql connection
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()
    #sql command to read the data
    writer = pd.ExcelWriter(filePath,engine='xlsxwriter')
    #convert 
    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    types=con.execute(sql_query)
    listOfTables=[]
    for i in types:
        for j in i:
            listOfTables.append(j)

    for table_name in listOfTables:
        sheet_name=table_name
        sql ="select * from "+sheet_name
        #load data into dataframe
        dft = pd.read_sql(sql,connection)
        #print(dft.head(5))
        dft.to_excel(writer, sheet_name=sheet_name,index=False)
    writer.save()
    connection.commit()
    connection.close()  
    return
    #return send_file(path, as_attachment=True)