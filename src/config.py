from pymongo import MongoClient

client = MongoClient("mongodb://localhost")

db = client["db_tarefas"]