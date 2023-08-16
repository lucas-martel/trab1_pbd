#!/usr/bin/env python

import sys

valor_atual = None
chave_atual = None

for linha in sys.stdin:
    valor, chave = linha.strip().split('\t')

    if valor_atual is None:
        valor_atual= valor
        chave_atual = chave
    elif valor == valor_atual:
        chave_atual = f"{chave_atual}, {chave}"
    else:
        print(f"{valor_atual}\t{chave_atual}")
        valor_atual = valor
        chave_atual = chave

if valor_atual is not None:
    print(f"{valor_atual}\t{chave_atual}")
