from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = '159357pass'
app.config['TEMPLATES_AUTO_RELOAD'] = True

url = "mongodb+srv://venger0001:gIr7jYEF92LG43TJ@cluster0.z0t5e.mongodb.net/pass_safe_db?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pass_safe_db
