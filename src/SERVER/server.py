from flask import Flask, request as f_request, jsonify, render_template
import os
import json
import logging

app = Flask(__name__)


mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def test():
    return 'auto-repo'



# Save data in section1
@app.route('/save', methods=['POST','GET'])
def save_in_section1():
    body = f_request.get_json()
    cursor = mysql.get_db().cursor()
    section = body['section']
    animal = body['animal']
    
    cursor.execute("insert into [table] (section, animal, image) values (%s, %s, %s)", (section, anmimal, image))

    mysql.get_db().commit()
    
    return jsonify({"message": "success"})


if __name__ == '__main__':
    app.run(debug=True)