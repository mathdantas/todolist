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

#Alterar status da Tarefa: Ao solicitar essa opção o usuário poderá alterar
#o status de uma determinada tarefa, ou seja, se a tarefa está como Pendente,
#ficará como Concluída, e vice-versa. Para isso, ele deve informar o título da tarefa. 
# Você deverá alterar a coluna de Status do arquivo, referente à tarefa que possui o título informado pelo usuário.

def alterar_tarefa():

    with open('tarefas.csv', 'r') as tarefas_csv:
        tabela = csv.reader(tarefas_csv, delimiter=';', lineterminator='\n')
        conteudo = list(tabela)

    lista_tarefas = [
        inquirer.List(
        "tarefa",
            message="Qual tarefa deseja modificar o status?",
            choices=conteudo
        )
    ]

    alterar_tarefa = inquirer.prompt(lista_tarefas)
    
    for index, tarefa in enumerate(conteudo):
        if tarefa == alterar_tarefa["tarefa"]:
            if tarefa[3] == 'Pendente':
                conteudo[index][3] = 'Concluida'
                print('Sucesso: ', conteudo[index])
            else:
                conteudo[index][3] = 'Pendente'
                print('Sucesso: ', conteudo[index])

    with open('tarefas.csv', 'w') as tarefas_csv:
        escritor = csv.writer(tarefas_csv, delimiter=';', lineterminator='\n')
        escritor.writerows(conteudo)    


def remover_tarefa():

    with open('tarefas.csv', 'r') as tarefas_csv:
        tabela = csv.reader(tarefas_csv, delimiter=';', lineterminator='\n')
        conteudo = list(tabela)

    lista_tarefas = [
        inquirer.List(
        "tarefa",
            message="Qual tarefa deseja remover?",
            choices=conteudo
        )
    ]

    tarefa_para_excluir = inquirer.prompt(lista_tarefas)
    
    conteudo.remove(tarefa_para_excluir["tarefa"])
    print(f'Sucesso: {tarefa_para_excluir["tarefa"]} removida.' )

    with open('tarefas.csv', 'w') as tarefas_csv:
        escritor = csv.writer(tarefas_csv, delimiter=';', lineterminator='\n')
        escritor.writerows(conteudo)  

def visualizar_tarefas_por_data():

    with open('tarefas.csv', 'r') as tarefas_csv:
        tabela = csv.reader(tarefas_csv, delimiter=';', lineterminator='\n')
        conteudo = list(tabela)
        datas_com_duplicatas = [linha[1] for linha in conteudo] 
        datas_sem_duplicatas = set(datas_com_duplicatas)
        lista_datas = list(datas_sem_duplicatas)

    lista_tarefas = [
        inquirer.List(
        "data",
            message="Deseja visualizar as tarefas de qual data?",
            choices=lista_datas
        )
    ]

    data_selecionada = inquirer.prompt(lista_tarefas)
    

    for index, tarefa in enumerate(conteudo):
        if tarefa[1] == data_selecionada["data"]:
            print(tarefa)