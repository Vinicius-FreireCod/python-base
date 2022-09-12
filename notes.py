#!/usr/bin/env python3
""" Bloco de notas 
$ notes.py new "Minha nota"
tag: tech
text:
Anotação geral sobre...

$ notes.py read --tag = tech
...
...
"""
__version__ = "0.1.0"
__author__ = "Vinicius Freire"

from ast import arguments
import os
import sys

path = os.curdir
filepath = os.path.join(path, 'notes.txt')
cmds = ('read', 'new')

arguments = sys.argv[1:]
if not arguments:
    print('Invalid usage')
    print(f'you must specify subcommand {cmds}')
    sys.exit(1)


if arguments[0] not in cmds:
    print(f'Invalid command {arguments[0]}')

while True:

    if arguments[0] == 'read':
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input('Qual a tag:').strip().lower()
        # leitura das notas
        for line in open(filepath):
            title, tag, text = line.split('\t')
            if tag == arg_tag:
                print(f'titulo: {title}')
                print(f'text: {text}')
                print('-' * 30)
                print()

    if arguments[0] == 'new':
        # escrever nota
        try:
            title = arguments[1]
        except IndexError:
            title = input("Qual é o titulo").strip().title()
        text = [
            f'{title}',
            input('tag:').strip(),
            input('text:').strip(),

        ]
        # \t - tsv
        with open(filepath, 'a') as file_:
            file_.write('\t'.join(text) + '\n')
    cont = input(f'Quer continuar {arguments[0]} notas? [N/y]').strip().lower()
    if cont != 'y':
        break
