#!/usr/bin/env python

import sys

for linha in sys.stdin:
    partes = linha.strip().split(' ', 1)
    chave = partes[0]
    palavras = partes[1].split(',')
    total_palavras = len(palavras)
    print(f"{chave}\t{total_palavras}")
