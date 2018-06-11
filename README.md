Isto é o README do plural-generator

O Plural Generator é um projeto cujo objetivo é gerar plurais para substantivos (não compostos) do Português Brasileiro (PB), incluindo suas exceções, usando algoritmos linguísticos escritos em Python 3.

Foi construída uma função chamada "desacentuador.py", responsável por remover o 1º acento que encontrar em palavras do PB. Ela foi incorporada dentro do algoritmo principal, especificamente dentro do bloco responsável por gerar o plural de palavras teminadas em "s". Oxítonas terminadas em "s" como "inglês", que antes era gerada "inglêses" no plural, agora têm seu acento removido antes de serem transformadas em plural.
