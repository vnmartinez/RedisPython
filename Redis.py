import Redis

class AplicativoTarefas:
    def __init__(self):
        self.Redis_client = redis.Redis(host='localhost', port=6379, db=0)
        self.task_counter = 'contador_de_tarefas'

    def adicionar_tarefa(self, descricao):
        id_tarefa = self.redis_client.incr(self.task_counter)
        chave_tarefa = f'tarefa:{id_tarefa}'
        self.redis_client.hmset(chave_tarefa, {'id': id_tarefa, 'descricao': descricao})
        print(f'Tarefa adicionada com ID: {id_tarefa}')

    def listar_tarefas(self):
        ids_tarefas = self.redis_client.keys('tarefa:*')
        for id_tarefa in ids_tarefas:
            dados_tarefa = self.redis_client.hgetall(id_tarefa)
            print(f"ID: {dados_tarefa[b'id'].decode()}, Descrição: {dados_tarefa[b'descricao'].decode()}")

    def remover_tarefa(self, id_tarefa):
        chave_tarefa = f'tarefa:{id_tarefa}'
        if self.redis_client.exists(chave_tarefa):
            self.redis_client.delete(chave_tarefa)
            print(f'Tarefa com ID {id_tarefa} removida')
        else:
            print(f'Tarefa com ID {id_tarefa} não encontrada')

if __name__ == "__main__":
    app_tarefas = AplicativoTarefas()

    while True:
        print("\nMenu do Aplicativo de Tarefas:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        escolha = input("Selecione uma opção: ")

        if escolha == "1":
            descricao = input("Informe a descrição da tarefa: ")
            app_tarefas.adicionar_tarefa(descricao)
        elif escolha == "2":
            app_tarefas.listar_tarefas()
        elif escolha == "3":
            id_tarefa = int(input("Informe o ID da tarefa para remover: "))
            app_tarefas.remover_tarefa(id_tarefa)
        elif escolha == "4":
            print("Encerrando o Aplicativo de Tarefas")
            break
        else:
            print("Opção inválida. Por favor, selecione novamente.")
