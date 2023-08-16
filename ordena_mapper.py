#!/usr/bin/env python

import sys

for linha in sys.stdin:
    chave, valor = linha.strip().split('\t')
    print(f"{valor}\t{chave}")