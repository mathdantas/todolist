import inquirer
import csv

def menu():

    lista_menu = [
        inquirer.List(
        "escolha_menu",
            message="O que você deseja fazer?",
            choices=[
                'Adicionar tarefa',
                'Alterar status da tarefa',
                'Remover tarefa',
                'Tarefas de outro dia',
                'Encerrar'
                ],
        ),
    ]

    return inquirer.prompt(lista_menu)
# o título, a data de realização e a categoria da tarefa. Você deverá salvar essas três informações 
# (além de uma informação de que o status da tarefa está como Pendente) dentro de um arquivo CSV 
# (tarefas.csv, por exemplo).
def adicionar_tarefa():
    lista_tarefa = [
        inquirer.Text("titulo", message="Titulo: "),
        inquirer.Text("data_de_realizacao", message="Data de realização: "),
        inquirer.List(
        "categoria",
            message="O que você deseja fazer?",
            choices=[
                "Pessoal",
                "Profissional"
                ],
        )
    ]
    tarefa = inquirer.prompt(lista_tarefa)
    tarefa['status'] = 'Pendente'
    tarefa_lista = list(tarefa.values())
    
    with open('tarefas.csv', 'a') as tarefas_csv:
        escritor = csv.writer(tarefas_csv, delimiter=';', lineterminator='\n')
        escritor.writerow(tarefa_lista)

adicionar_tarefa()
