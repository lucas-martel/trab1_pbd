#!/usr/bin/env python
import sys
import re

for linha in sys.stdin:
    palavras = linha.strip().split()
    for palavra in palavras:
        palavra = palavra.lower()
        if re.match(r"^[A-Za-z]+$", palavra):
            print(f"{palavra}\t1")