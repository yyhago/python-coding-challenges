class Tarefa:

    id_global = 0

    def __init__(self, descricao, prioridade):
        
        self.id = Tarefa.id_global
        Tarefa.id_global += 1

        self.descricao = descricao
        self.prioridade = prioridade
        self.concluido = False

    def __repr__(self):
        return f"Tarefa: {self.descricao } (Prioridade: {self.prioridade})"
    


class GerenciadorTarefas:

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        self.tarefas_armazenadas = []

    def adicionar_tarefa(self, descricao, prioridade):
        nova = Tarefa(descricao, prioridade)
        self.tarefas_armazenadas.append(nova)
        return nova

    def remover_tarefa(self, id):
        for tarefa in self.tarefas_armazenadas:
            if tarefa.id == id:
                self.tarefas_armazenadas.remove(tarefa)
                return
        raise ValueError(f"Tarefa com ID: {id} não encontrada!")


    def marcar_concluido_tarefa(self, id):
        for tarefa in self.tarefas_armazenadas:
            if tarefa.id == id:
                tarefa.concluido = True
                return
        raise ValueError(f"Não foi possivel marcar a tarefa como concluído.")

    def pegar_tarefas_prioridade(self, prioridade):
        lista_filtrada = []
        for tarefa in self.tarefas_armazenadas:
            if tarefa.prioridade == prioridade:
                lista_filtrada.append(tarefa)
        return lista_filtrada
    



# Instanciando o gerenciador (Singleton)
g1 = GerenciadorTarefas()
g2 = GerenciadorTarefas()
print("Singleton funcionando?", g1 is g2)  # True

# Adicionando tarefas
t1 = g1.adicionar_tarefa("Estudar Python", 3)
t2 = g1.adicionar_tarefa("Fazer exercícios", 1)
t3 = g1.adicionar_tarefa("Revisar POO", 2)
print("\nTarefas adicionadas:")
print(t1)
print(t2)
print(t3)

# Listar tarefas por prioridade
print("\nTarefas com prioridade 1:")
print(g1.pegar_tarefas_prioridade(1))

print("\nTarefas com prioridade 3:")
print(g1.pegar_tarefas_prioridade(3))

# Marcar como concluída
g1.marcar_concluido_tarefa(t1.id)
print(f"\nTarefa {t1.id} concluída?")
print(t1.concluido)  # Deve mostrar True

# Remover tarefa
print("\nRemovendo tarefa t2...")
g1.remover_tarefa(t2.id)

print("Tarefas restantes:")
for tarefa in g1.tarefas_armazenadas:
    print(tarefa)

# Tentar marcar/remover com ID inválido
try:
    g1.marcar_concluido_tarefa(999)  # ID inexistente
except ValueError as e:
    print("\nErro ao marcar como concluída:", e)

try:
    g1.remover_tarefa(999)  # ID inexistente
except ValueError as e:
    print("Erro ao remover tarefa:", e)
