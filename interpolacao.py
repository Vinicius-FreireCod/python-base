#!/usr/bin/env python3
""" Emails de produtos para cliente
"""
__version__ = "0.1.0"
__author__ = "Vinicius Freire"

from ast import arguments
import email
from re import template
import sys
import os

arguments = sys.argv[1:]

if not arguments:
    print('Informe o nome do arquivo de emails')
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filename):
    name, email = line.split(',')

    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            'nome': name,
            'produto': 'caneta',
            'texto': 'Escrever muito bem',
            'link': 'http//meunomenaoejony.com',
            'quantidade': 1,
            'preco': 50.5,
        }
    )
    print('-' * 50)
