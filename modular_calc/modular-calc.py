# modular-calc
from funcoes import percentagem
from funcoes import plus
from funcoes import minus
from funcoes import times
from funcoes import division

print("Bem-vindo! \n Selecione a operação desejada:\n 1) Porcentagem \n 2) Adição \n 3) Subtração \n 4) Multiplicação \n 5) Divisão \n 0) Digite 0 para sair.")

while (input) != 0:
    entrada_usuario = int(input("Digite o número da operação desejada: \n"))
    if entrada_usuario == 1:
        print("Você escolheu porcentagem!\n")
        total = input("Porcentagem: Qual o total de páginas? \n")
        lido = input("Porcentagem: Quantas páginas já foram lidas? \n")
        resposta_porcentagem = percentagem(int(lido), int(total))
        print("Você leu: %s%%." % (resposta_porcentagem))
    if entrada_usuario == 2:
        print("Você escolheu: Adição!\n")
        parcela1 = input("Adição: Insira a primeira parcela: \n")
        parcela2 = input("Adição: Insira a segunda parcela: \n")
        resposta_soma = plus(int(parcela1), int(parcela2))
        print("A soma é: %s." % (resposta_soma))
    if entrada_usuario == 3:
        print("Você escolheu: Subtração!\n")
        minuendo = input("Insira o minuendo: \n")
        subtraendo = input("Insira o subtraendo: \n")
        resposta_diferenca = minus(int(minuendo), int(subtraendo))
        print("O resultado da diferença é: %s." % (resposta_diferenca))
    if entrada_usuario == 4:
        print("Você escolheu multiplicação!\n")
        fator1 = input("Digite o primeiro fator: \n")
        fator2 = input("Digite o segundo fator: \n")
        resposta_times = times(int(fator1), int(fator2))
        print("O produto da multiplicação é: %s" % (resposta_times))

    if entrada_usuario == 5:
        print("Você escolheu divisão!")
        dividendo = input("Insira um dividendo: \n")
        divisor = input("Insira um divisor: \n")
        resposta_division = division(int(dividendo), int(divisor))
        print("A resposta da divisão é: %s" % (resposta_division))
    elif entrada_usuario == 0:
        print("Programa encerrado.")
        break
