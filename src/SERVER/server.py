from flask import Flask, request as request, jsonify, render_template
import os
import json
import pymssql
import logging
import pyodbc

app = Flask(__name__)

server='tcp:roadkill-1.database.windows.net'
username='roadkillAdmin'
password='password'
database='roadkill-data'
driver='{ODBC Driver 17 for SQL Server}'




@app.route('/')
def index():
    return 'auto-repo'

@app.route('/test', methods=['GET','POST'])
def test():
    body = request.get_data()
    print(body)
    
    temp=str(body).split('&')
    latitude=temp[0].split('=')[1]
    animal=temp[1].split('=')[1]
    longitude=temp[2].split('=')[1]

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO "+animal+"(latitude, longitude) VALUES (?, ?)",latitude,longitude)
   
    cnxn.commit()
    cnxn.close()
    
    return body

if __name__ == '__main__':
    app.run(debug=True)
    