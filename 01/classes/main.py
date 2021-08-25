from .agenda import Agenda

class Main:
    def __init__(self):
        self.agenda = Agenda()
        self.agenda.set_proprietario('Prof Debs')
        self.agenda.set_ano(2021)

    def mostrar_menu(self):
        print('Selecione uma opção:')
        print('1. Cadastrar contato')

