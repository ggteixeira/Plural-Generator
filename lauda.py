num_char = int(input("Caracteres (com espaço): \n"))
tam_lauda = 1700 # Uma evolução do programa é criar uma caixa pro usuário poder ajustar o tamanho da lauda
val_lauda = 4 # Uma outra evolução do programa é criar uma caixa pro usuário poder ajudstar o valor cobrado por lauda

price = ((num_char / tam_lauda) * val_lauda)

print("Preço estipulado: R$ %2.2f" %(price))
