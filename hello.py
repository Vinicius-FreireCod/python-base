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
__version__ = "0.1.3"
__author__ = "Vinicius Freire"

from ast import arguments
import os
import sys

arguments = {
    "lang": None,
    "count": 1
}
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option ´{key}´")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, Word!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",

}

print(
    msg[current_language] * int(arguments["count"])
)
