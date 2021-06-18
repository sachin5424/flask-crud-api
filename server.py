
from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from flask_restful import Api
from controller.TripCategory import Trip_Category
app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'P@ssw0rd'
app.config['MYSQL_DB'] = 'citycabs'
mysql = MySQL(app)


api.add_resource(Trip_Category,"/","/<int:pk>")



if __name__ == "__main__":
    app.run(debug=True)

