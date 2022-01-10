import inquirer
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