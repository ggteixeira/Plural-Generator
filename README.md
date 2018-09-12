# Isto é o README do Plural Generator

O **plural-generator** é um projeto cujo objetivo é gerar plurais para substantivos (não compostos) do Português Brasileiro (PB), incluindo suas exceções, usando algoritmos linguísticos escritos em Python 3.

------

**11 de junho de 2018:** 

Foi construída uma função chamada "desacentuador.py", responsável por remover o 1º acento que encontrar em palavras do PB. Ela foi incorporada dentro do algoritmo principal, especificamente dentro do bloco responsável por gerar o plural de palavras teminadas em "s". Oxítonas terminadas em "s" como "inglês", que antes era gerada "inglêses" no plural, agora têm seu acento removido antes de serem transformadas em plural.

**7 de julho de 2018:**

A lista inicial de plurais foi [ligeiramente reorganizada](https://github.com/guiemi/plural-generator/commit/fa6e0f3c97cc690e254d18a323b48ee08bf1149b#diff-3d3943198c6294e846e0694542384a39) com base em [HUBACK (2017)](https://revistas.ufpr.br/abralin/article/view/52337).

------

**REFERÊNCIAS**

HUBACK, Ana Paula. PLURAIS IRREGULARES DO PORTUGUÊS BRASILEIRO: EFEITOS DE FREQUÊNCIA. Revista da ABRALIN, [S.l.], v. 9, n. 1, maio 2017. ISSN 0102-7158. Disponível em: <https://revistas.ufpr.br/abralin/article/view/52337>. Acesso em: 07 jul. 2018. doi:http://dx.doi.org/10.5380/rabl.v9i1.52337.

