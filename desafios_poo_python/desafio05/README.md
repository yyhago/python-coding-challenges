5. Gerenciador de Tarefas 

Implemente um GerenciadorTarefas com Singleton e classe Tarefa.
Requisitos:

Tarefa: descricao, prioridade, concluida.
GerenciadorTarefas: Singleton, métodos para adicionar, remover, marcar como concluída e filtrar por prioridade.

Exemplo:
gerenciador = GerenciadorTarefas()
t1 = gerenciador.adicionar_tarefa("Estudar POO", 3)
t2 = gerenciador.adicionar_tarefa("Fazer exercícios", 1)
gerenciador.marcar_concluida(t1.id)
print(gerenciador.get_tarefas_prioridade(1))  # [Tarefa: Fazer exercícios (Prioridade: 1)]
