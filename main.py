from ToDo import ToDoList
import os
from time import sleep

to_do = ToDoList()

while True:
    os.system('cls')

    opcao = to_do.menu()

    if opcao == 'Adicionar tarefa':
        to_do.adicionar_tarefa()
    elif opcao == 'Alterar status da tarefa':
        to_do.alterar_tarefa()
    elif opcao == 'Remover tarefa':
        to_do.remover_tarefa()
    elif opcao == 'Filtrar por dia':
        to_do.visualizar_tarefas_por_data()
    elif opcao == 'Encerrar':
        print('Encerrando o programa!')
        break
    
    sleep(1)