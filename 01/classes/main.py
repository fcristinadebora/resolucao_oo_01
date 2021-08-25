from .agenda import Agenda

class Main:
    def __init__(self):
        self.agenda = Agenda()
        self.agenda.set_proprietario('Prof Debs')
        self.agenda.set_ano(2021)

    def mostrar_menu(self):
        print('Selecione uma opção:')
        print('1. Cadastrar contato')
        print('0. Sair do programa')

    def ler_opcao_menu(self):
        opcao = input(' > ')

        if (opcao == '0'):
            print('Obrigada por usar nosso software, finalizando execução')
            return

        if (opcao == '1'):
            self.cadastrar_contato()


    def cadastrar_contato(self):
        print('Novo contato')
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        cpf = input('CPF: ')

