from flask import Flask
from controllers.tarefa_controller import api as tarefa_api
from flask_restx import Api
app = Flask(__name__)
api = Api(app, version="1.0", title="Tarefas API", description="API para gerenciar tarefas")

api.add_namespace(tarefa_api, path="/tarefas")

if __name__ == "__main__":
    app.run(debug=True)
