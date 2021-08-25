from .agenda import Agenda
from .contato import Contato

class Main:
    def __init__(self):
        self.em_execucao = True
        self.agenda = Agenda()
        self.agenda.set_proprietario('Prof Debs')
        self.agenda.set_ano(2021)

    def mostrar_menu(self):
        print('')
        print('=========================')
        print('A G E N D A  V I R T U A L')
        print('=========================')
        print('Selecione uma opção:')
        print('1. Cadastrar contato')
        print('0. Sair do programa')

    def ler_opcao_menu(self):
        opcao = input(' > ')

        if (opcao == '0'):
            print('Obrigada por usar nosso software, finalizando execução')
            self.em_execucao = False
            return

        if (opcao == '1'):
            self.cadastrar_contato()


    def cadastrar_contato(self):
        print('Novo contato')
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        cpf = input('CPF: ')

        contato = Contato()
        contato.set_nome(nome)
        contato.set_telefone(telefone)
        contato.set_email(email)
        contato.set_cpf(cpf)

        self.agenda.add_contato(contato)
        print('Contato adicionado com sucesso.')

