from .contato import Contato
from .tarefa import Tarefa

class Agenda:

    def __init__(self):
        self.__proprietario = ''
        self.__ano = 0
        self.__contatos = []
        self.__tarefas = []

    def get_proprietario(self):
        return self.__proprietario

    def set_proprietario(self, proprietario):
        self.__proprietario = proprietario

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_contatos(self):
        return self.__contatos

    def add_contato(self, contato):
        self.__contatos.append(contato)

    def get_tarefas(self):
        return self.__tarefas

    def add_tarefa(self, tarefa):
        self.__tarefas.append(tarefa)

    def remover_contato(self, contato):
        self.__contatos.remove(contato)

    def get_contato(self, posicao_contato):
        return self.__contatos[posicao_contato]

    def remover_tarefa(self, tarefa):
        self.__tarefas.remove(tarefa)

    def get_tarefa(self, posicao_tarefa):
        return self.__tarefas[posicao_tarefa]