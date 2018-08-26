########restlessapi.py########################
from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class macs(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        mac = db.Column(db.Unicode)
        port = db.Column(db.Integer)
        status = db.Column(db.Integer)
        time = db.Column(db.Unicode)
        updatetime = db.column(db.Unicode)
        probertime = db.column(db.Unicode)
        oid = db.column(db.Unicode)
        notify = db.column(db.Unicode)

db.create_all()


manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(macs, methods=['GET'])

app.run(debug=True)

#######################entity.py==for creating entity and notify it##########


from flask import Flask
import pymysql
from flask import jsonify
import MySQLdb
app = Flask(__name__)



@app.route('/anm')
def index():
        connection = pymysql.connect(host='127.0.0.1', user='root', password='admin123', db='anm')
        with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM macs where notify=1")
                whole = cursor.fetchall()
                connection.commit()

                #print(whole)
                return jsonify(whole)

@app.route('/bnm/<int:post_id>', methods=['GET', 'POST'])
def good(post_id):
        connection = pymysql.connect(host='127.0.0.1', user='root', password='admin123', db='anm')
        with connection.cursor() as cursor:
                cursor.execute("UPDATE macs SET notify = %s WHERE notify = %s", (post_id,1))
                ##hole = cursor.fetchall()
                connection.commit()
                connection.close()








if __name__ == "__main__":
        app.run()
~
