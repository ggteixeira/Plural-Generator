# Módulos:


def percentagem(lido=input, total=input, multiplica=100):
    resultado_porcentagem = lido / total * multiplica
    return round(resultado_porcentagem, 1)


def plus(parcela1=input, parcela2=input):
    resultado_soma = parcela1 + parcela2
    return resultado_soma


def minus(minuendo=input, subtraendo=input):
    resultado_subtracao = minuendo - subtraendo
    return resultado_subtracao


def times(fator1, fator2):
    produto = fator1 * fator2
    return produto


def division(dividendo, divisor):
    quociente = dividendo / divisor
    return round(quociente, 0)
