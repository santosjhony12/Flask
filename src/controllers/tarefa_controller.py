from flask import Blueprint, jsonify, request
from services import tarefa_service
from flask import abort
from flask_restx import Namespace, Resource, fields

api = Namespace("tarefas", description="Operações relacionadas as tarefas")

tarefa_model = api.model(
    "Tarefa",
    {
        "id": fields.String(readonly=True, description="ID da tarefa"),
        "titulo": fields.String(required=True, description="Título da tarefa"),
        "feito": fields.Boolean(required=True, description="Status da tarefa")
    }
)

#PRECISO USAR O VERNO HTTP NO NOME DO MÉTODO
@api.route("/")
class TarefaList(Resource):
    @api.doc("listar_tarefas")
    @api.marshal_list_with(tarefa_model)
    def get(self):
        return tarefa_service.get_tarefas()

    @api.doc("criar_tarefa")
    @api.expect(tarefa_model, validate=True)
    @api.marshal_with(tarefa_model, code=201)
    def post(self):
        dados = api.payload
        novo_id = tarefa_service.criar_tarefa(dados['titulo'], dados['feito'])
        return {"id": novo_id, **dados}, 201
    
@api.route("/<id>")
@api.param("id", "ID da tarefa")
class Tarefa(Resource):
    # @api.doc("buscar_tarefa")
    # @api.marshal_with(tarefa_model)
    # def get(self, id):
    #     """Busca tarefa pelo ID"""
    #     tarefa = tarefa_service.get_tarefa(id)
    #     if tarefa:
    #         return tarefa
    #     api.abort(404, "Tarefa não encontrada")

    @api.doc("atualizar_tarefa")
    @api.expect(tarefa_model, validate=True)
    @api.marshal_with(tarefa_model)
    def put(self, id):
        """Atualiza tarefa pelo ID"""
        dados = api.payload
        tarefa = tarefa_service.atualizar_tarefa(id, dados["titulo"], dados["feito"])
        if tarefa:
            return tarefa
        api.abort(404, "Tarefa não encontrada")

    # @api.doc("deletar_tarefa")
    # def delete(self, id):
    #     """Deleta tarefa pelo ID"""
    #     ok = tarefa_service.deletar_tarefa(id)
    #     if ok:
    #         return {"mensagem": "Tarefa removida com sucesso"}
    #     api.abort(404, "Tarefa não encontrada")