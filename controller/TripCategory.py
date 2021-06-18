
from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Api,Resource,reqparse
from werkzeug.routing import ValidationError

app = Flask(__name__)
api = Api(app)

mysql = MySQL(app)

def min_length(min_length):
    def validate(s):
        if len(s) >= min_length:
            return s
        raise ValidationError("String must be at least %i characters long" % min)
    return validate


parser = reqparse.RequestParser()
parser.add_argument('name', type=min_length(3), required=True )
parser.add_argument('icon', type=str)
parser.add_argument('active', type=bool)




class Trip_Category(Resource):
    def get(self,pk=None):
        cur = mysql.connection.cursor()
        if pk:
            cur.execute("""SELECT * FROM trip_category WHERE id = %s""", (pk,))
            data = cur.fetchall()
            return {"desired: ":data}
        else:
            query = "SELECT * FROM trip_category "
            cur.execute(query)
            data = cur.fetchall()
            return {"desired: ":data}

    def post(self):
        cur = mysql.connection.cursor()
        args = parser.parse_args()
        name =args['name']
        icon = args['icon']
        active = args['active']
        query = """INSERT INTO trip_category(name, icon, active) VALUES(%s, %s, %s)"""
        cur.execute(query,(name,icon,active))
        mysql.connection.commit()
        return {'message':'successfuly create '}

    def delete(self,pk):
        cur = mysql.connection.cursor()
        cur.execute("""DELETE FROM trip_category WHERE id= %s""", (pk,))
        cur.connection.commit()
        cur.close()
        return {"data":"delete your item"}

