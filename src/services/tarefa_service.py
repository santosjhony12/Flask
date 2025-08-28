from repositories import tarefa_repository

def get_tarefas():
    return [t.to_dict() for t in tarefa_repository.listar_tarefas()]

def criar_tarefa(titulo, feito):
    return tarefa_repository.salvar_tarefa(titulo, feito)

def update_tarefa(id, titulo, feito):
    return tarefa_repository.update_tarefa(id, titulo, feito).to_dict()

