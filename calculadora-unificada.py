# coding: utf-8

import funcoes

# Calculadora

print("Bem-vindo! \n Selecione a operação desejada:\n")
print("1) Porcentagem")
print("2) Adição")
print("3) Subtração")
print("4) Multiplicação")
print("5) Divisão")
print("Ou Digite 0 para sair")

while (input) != 0:
    entrada_usuario = int(input("Digite o número da operação desejada: \n"))
    # Porcentagem (páginas lidas):
    if entrada_usuario == 1:
        print("Você escolheu porcentagem de páginas lidas!\n")
        total = input("Porcentagem: Qual o total de páginas? \n")
        lido = input("Porcentagem: Quantas páginas já foram lidas? \n")
        resposta_porcentagem = percentagem(int(lido), int(total))
        print("Você leu: %5.2f%%." % (resposta_porcentagem))
    # Adição:
    if entrada_usuario == 2:
        print("Você escolheu: Adição!\n")
        parcela1 = input("Adição: Insira a primeira parcela: \n")
        parcela2 = input("Adição: Insira a segunda parcela: \n")
        resposta_soma = plus(int(parcela1), int(parcela2))
        print("A soma é: %s." % (resposta_soma))
    # Subtração:
    if entrada_usuario == 3:
        print("Você escolheu: Subtração!\n")
        minuendo = input("Insira o minuendo: \n")
        subtraendo = input("Insira o subtraendo: \n")
        resposta_diferenca = minus(int(minuendo), int(subtraendo))
        print("O resultado da diferença é: %s." % (resposta_diferenca))
    # Multiplicação:
    if entrada_usuario == 4:
        print("Você escolheu multiplicação!\n")
        fator1 = input("Digite o primeiro fator: \n")
        fator2 = input("Digite o segundo fator: \n")
        resposta_times = times(int(fator1), int(fator2))
        print("O produto da multiplicação é: %s" % (resposta_times))
    # Divisão:
    if entrada_usuario == 5:
        print("Você escolheu divisão!")
        dividendo = input("Insira um dividendo: \n")
        divisor = input("Insira um divisor: \n")
        resposta_division = division(int(dividendo), int(divisor))
        print("A resposta da divisão é: %s" % (resposta_division))
    elif entrada_usuario == 0:
        print("Calculadora encerrada.")
        break

# Github, eu quero te amar.
