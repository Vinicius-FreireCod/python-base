#!/usr/bin/env python3
"""Hello Word Multi Linguas

Dependendo da lingua configurada no ambiente o programa
exibe a mensagem correspondente.

Como usar:

Tenha a variavel Lang devidamente configurada ex:
     export LANG=pt_BR

Execução:

     python3 hello.py
     ou
     ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Vinicius Freire"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, Word!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",

}

print(msg[current_language])
