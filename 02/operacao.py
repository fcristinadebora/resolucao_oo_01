class Operacao:
    @staticmethod
    def soma(vetor_valores):
        total = 0
        for valor in vetor_valores:
            total = total + valor

        return total