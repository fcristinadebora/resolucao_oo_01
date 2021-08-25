from operacao import Operacao

vetor_valores = [ 1.2, 2.5, 3, 6, 8 ]

total = Operacao.soma(vetor_valores)
print('Soma de todos os valores do vetor = ' + str(total))

total_vazio = Operacao.soma([])
print('Soma de todos os valores do vetor vazio = ' + str(total_vazio))