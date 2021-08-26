from .agenda import Agenda
from .contato import Contato
from .tarefa import Tarefa

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
        print('2. Listar contatos')
        print('3. Excluir contato')
        print('4. Cadastrar tarefa')
        print('5. Listar tarefas')
        print('6. Excluir tarefa')
        print('0. Sair do programa')

    def ler_opcao_menu(self):
        opcao = input(' > ')

        if (opcao == '0'):
            print('Obrigada por usar nosso software, finalizando execução')
            self.em_execucao = False
            return

        if (opcao == '1'):
            self.cadastrar_contato()
        elif (opcao == '2'):
            self.listar_contatos()
        elif (opcao == '3'):
            self.excluir_contato()
        elif (opcao == '4'):
            self.cadastrar_tarefa()
        elif (opcao == '5'):
            self.listar_tarefas()
        elif (opcao == '6'):
            self.excluir_tarefa()


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

    def listar_contatos(self):
        print('Lista de contatos:')
        contatos_da_agenda = self.agenda.get_contatos()
        for indice, contato in enumerate(contatos_da_agenda):
            print('Numero: ' + str(indice) + ' - Contato: ' + contato.get_nome() + ' / Tel: ' + contato.get_telefone())

    def excluir_contato(self):
        self.listar_contatos()
        indice_para_excluir = input('Digite o número do contato ')

        try:
            contato_selecionado = self.agenda.get_contato(int(indice_para_excluir))
        except:
            print('Contato inválido')
            return

        self.agenda.remover_contato(contato_selecionado)
        print('Contato excluído com sucesso')

    def cadastrar_tarefa(self):
        print('Nova tarefa')
        descricao = input('Descricao: ')
        status = input('Concluída? 1 - sim / 0 - não ')

        tarefa = Tarefa()
        tarefa.set_descricao(descricao)
        if (status == '1'):
            tarefa.set_status_concluida()
        elif(status == '0'):
            tarefa.set_status_pendente()
        else:
            print('Status inválido')
            return


        self.agenda.add_tarefa(tarefa)
        print('Tarefa adicionada com sucesso.')

    def listar_tarefas(self):
        print('Lista de tarefas:')
        tarefas_da_agenda = self.agenda.get_tarefas()
        for indice, tarefa in enumerate(tarefas_da_agenda):
            print('Numero: ' + str(indice) + ' - ' + tarefa.get_descricao() + ' / status: ' + tarefa.get_status())

    def excluir_tarefa(self):
        self.listar_tarefas()
        indice_para_excluir = input('Digite o número da tarefa ')

        try:
            tarefa_selecionada = self.agenda.get_tarefa(int(indice_para_excluir))
        except:
            print('Tarefa inválida')
            return

        self.agenda.remover_tarefa(tarefa_selecionada)
        print('Tarefa excluída com sucesso')