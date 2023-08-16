#!/usr/bin/env python

import sys
import re

for linha in sys.stdin:
    linha = re.sub(r'[^a-zA-Z0-9\s]', ' ', linha)
    palavras = linha.strip().split()
    for palavra in palavras:
        if palavra:
            palavra = palavra.lower()
            print(f"{palavra}\t1")