import csv
import inquirer
from datetime import datetime
from datetime import timedelta
class ToDoList():
    def __init__(self):
        self.lista = self.__ler_csv()
    
    def __ler_csv(self):
        with open('tarefas.csv', 'r') as tarefas_csv:
            tabela = csv.reader(tarefas_csv, delimiter=';', lineterminator='\n')
            conteudo = list(tabela)
            
        return conteudo

    def __salvar_csv(self):
        with open('tarefas.csv', 'w') as tarefas_csv:
            escritor = csv.writer(tarefas_csv, delimiter=';', lineterminator='\n')
            escritor.writerows(self.lista)

    def __tarefa_existe(self, titulo, data_de_realizacao):
        self.lista = self.__ler_csv()
        for tarefa in self.lista:
            if tarefa[0] == titulo and tarefa[1] == data_de_realizacao:
                return True
            else:
                return False

    def __ordenar_lista(self):
        self.lista = sorted(self.lista, key=lambda x: self.__converter_data(x))

    def __converter_data(self, lista_tarefa):
        data = lista_tarefa[1]
        data_ordenada = data.split('/')[::-1]
        return ''.join(data_ordenada)

    def menu(self)-> str:

        lista_menu = [
            inquirer.List(
            "escolha_menu",
                message="O que você deseja fazer?",
                choices=[
                    'Adicionar tarefa',
                    'Alterar status da tarefa',
                    'Remover tarefa',
                    'Filtrar por dia',
                    'Encerrar'
                    ],
            ),
        ]

        escolha = inquirer.prompt(lista_menu)
        return escolha["escolha_menu"]
     
    def __coletar_data(self) -> dict:
        
        data_de_realizacao = [ 
            inquirer.List(
                "data_de_realizacao",
                message="Data de realizacao:",
                choices=[
                    "Hoje",
                    "Amanha",
                    "Outra data"
                    ],
            )
        ]

        data = inquirer.prompt(data_de_realizacao)

        if data['data_de_realizacao'] == 'Hoje':
            data['data_de_realizacao'] = datetime.today().strftime('%d/%m/%Y')

        elif data['data_de_realizacao'] == 'Amanha':
            tomorrow = datetime.today() + timedelta(days=1)
            data['data_de_realizacao'] = tomorrow.strftime('%d/%m/%Y')            

        else:
            data_de_realizacao = [ inquirer.Text("data_de_realizacao", message="Data de realizacao: ") ]
            data = inquirer.prompt(data_de_realizacao)

        return data


    def adicionar_tarefa(self):

        tarefa = inquirer.prompt([inquirer.Text("titulo", message="Titulo: ")])
        tarefa.update( self.__coletar_data() )
        tarefa.update( inquirer.prompt([inquirer.List(
                                                    "categoria",
                                                        message="O que você deseja fazer?",
                                                        choices=[
                                                            "Pessoal",
                                                            "Profissional"
                                                            ]
                                                    )]))

        tarefa['status'] = 'Pendente'
        tarefa['titulo'] = tarefa['titulo'].strip()
        tarefa_lista = list(tarefa.values())

        if self.__tarefa_existe(tarefa_lista[0],tarefa_lista[1]):
            return print('Erro: essa tarefa já existe.')

        self.lista.append(tarefa_lista)
        self.__ordenar_lista()

        self.__salvar_csv()

        print(f'Sucesso: tarefa adicionada.' )

    def alterar_tarefa(self):

        lista_tarefas = [
            inquirer.List(
            "tarefa",
                message="Qual tarefa deseja modificar o status?",
                choices=self.lista
            )
        ]

        alterar_tarefa = inquirer.prompt(lista_tarefas)
        
        for index, tarefa in enumerate(self.lista):
            if tarefa == alterar_tarefa["tarefa"]:
                if tarefa[3] == 'Pendente':
                    self.lista[index][3] = 'Concluida'
                    print('Sucesso: ', self.lista[index])
                else:
                    self.lista[index][3] = 'Pendente'
                    print('Sucesso: ', self.lista[index])

        self.__salvar_csv()  


    def remover_tarefa(self):

        lista_tarefas = [
            inquirer.List(
            "tarefa",
                message="Qual tarefa deseja remover?",
                choices=self.lista
            )
        ]

        tarefa_para_excluir = inquirer.prompt(lista_tarefas)
        
        self.lista.remove(tarefa_para_excluir["tarefa"])
        print(f'Sucesso: {tarefa_para_excluir["tarefa"]} removida.' )

        self.__salvar_csv()

    def visualizar_tarefas_por_data(self):
        datas_com_duplicatas = [linha[1] for linha in self.lista] 
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
        

        for index, tarefa in enumerate(self.lista):
            if tarefa[1] == data_selecionada["data"]:
                print(tarefa)