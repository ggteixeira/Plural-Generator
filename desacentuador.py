# Aqui será construída uma função
# que auxiliará na remoção de acentos
# para que palavras como "inglês"
# sejam geradas como "ingleses" em vez de "inglêses"

acentuadas = ["á", "â", "é", "ê", "í", "ó", "ô", "ú"]
vogais = ["a", "a", "e", "e", "i", "o", "o", "u"]

def desacento(palavra):
    for letra in palavra:
        if letra in acentuadas:
            acentuada = letra
            index_desacento = acentuadas.index(letra)
            index_acento = palavra.index(letra)
            palavra = palavra.replace(acentuada, vogais[index_desacento])
    return print(palavra)
desacento("inglêses")

'''
acentos = {
    "a": ["á", "â"],
    "e": ["é", "ê"],
    "i": ["í"],
    "o": ["ó", "ô"],
    "u": ["ú"]
}
'''
