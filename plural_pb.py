palavra = str(input("Digite: \n"))

a = ["s"]
s = ["es"]

def plural(palavra):
    # Letra a:
    if palavra[-1] == "a":
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

# Isto é um teste de commit.
# Se o teste der certo, este arquivo não estará no repo da modular_calc
