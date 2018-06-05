palavra = str(input("Digite: \n"))

# Letras que formam substantivos plurais em PB:
a = ["s"]
e = ["s"]
i = ["s"]
l = ["es", "is"]
m = ["ns"]
n = ["s"]
o = ["s"]
r = ["es"]
s = ["es"]
u = ["s"]
z = ["es"]

def plural(palavra):
    # Letra a:
    if palavra[-1] == "a": # Talvez dicionários melhores que listas
        print(f"{palavra}{a[0]}")

    # Letra s:
    if palavra[-1] == "s":
        if palavra[-2] == "í":
            print(f"{palavra}{s[0]}")
        elif palavra[-2] == "ê":
            print(f"{palavra}{s[0]}")
        else:
            print(f"{palavra}")

plural(palavra)

acentuadas = ["á", "â", "é", "ê", "í", "ó", "ô", "ú"]
vogais = ["a", "a", "e", "e", "i", "o", "o", "u"]
