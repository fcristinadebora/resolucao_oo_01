class Contato:

    def __init__(self):
        self.__nome = ''
        self.__telefone = ''
        self.__email = ''
        self.__cpf = ''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

