from bson import ObjectId
from config import db
from models.tarefa import Tarefa
from pymongo import ReturnDocument

colecao = db["tarefas"]

def listar_tarefas():
    docs = colecao.find()
    return [Tarefa(id=doc["_id"], titulo=doc["titulo"], feito=doc["feito"]) for doc in docs]

def buscar_por_id(id):
    doc = colecao.find_one({"_id": ObjectId(id)})
    if doc:
        return Tarefa(id=doc["_id"], titulo=doc["titulo"], feito=doc["feito"])
    return None

def salvar_tarefa(titulo, feito):
    result = colecao.insert_one({"titulo": titulo, "feito": feito})
    return str(result.inserted_id)

def update_tarefa(id, titulo, feito):
    doc = colecao.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "feito": feito}}, return_document=ReturnDocument.AFTER)
    if doc:
        return Tarefa(id=doc['_id'], titulo=doc['titulo'], feito=doc['feito'])
    return None