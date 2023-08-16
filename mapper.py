#!/usr/bin/env python

import sys

for linha in sys.stdin:
    palavras = linha.split()  # Separa as palavras por espaços em branco
    for palavra in palavras:
        print(f"{palavra}\t1")