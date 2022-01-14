from ToDo import ToDoList
import os
from time import sleep

to_do = ToDoList()

while True:
    os.system('cls')

    to_do.visualizar_tarefas_dia()
    opcao = to_do.menu()

    if opcao == 'Mostrar todas tarefas':
        os.system('cls')
        print('Todas as tarefas')
        to_do.imprimir_lista_tarefas(to_do.lista)
        input("\n Digite ENTER para continuar")
    elif opcao == 'Adicionar tarefa':
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