#!/usr/bin/env python3

"""Exibe relatorio de criancas por atividades

Imprimir a lista de criancas agrupadas por sala que frequenta
cada uma das atividades.
"""

__version__ = "0.0.1"
__author__ = "Vinicius Freire"

# Dados
salas = {
    "1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "Ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

for key in aulas.keys():
    alunos = {}
    print(f"Alunos da atividade {key}\n")

    for i in salas.keys():
        alunos[i] = set(salas[i]) & set(aulas[key])
        print(f"Sala {i}", alunos[i])

    print("-" * 20)
    print()
