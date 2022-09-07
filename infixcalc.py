#!/usr/bin/env python3
""" Calculadora infix.
"""
__version__ = "0.1.0"
__author__ = "Vinicius Freire"


from ast import arguments
import os
import sys

arguments = {
    "ope": None,
    "num_1": None,
    "num_2": None
}

args = sys.argv[1:]

list_ope = ['sum', 'sub', 'mult', 'div']

if len(args) == 0:
    arguments["ope"] = input("Escolher o tipo de operação:")
    arguments["num_1"] = input("escolher o primeiro numero da operacao:")
    arguments["num_2"] = input("escolher o segundo numero da operacao:")

if len(args) >= 1:
    arguments["ope"] = args[0]
    if len(args) == 1:
        arguments["num_1"] = \
            input("escolher o primeiro numero da operacao:")
        arguments["num_2"] = \
            input("escolher o segundo numero da operacao:")
    if len(args) == 2:
        arguments["num_1"] = args[1]
        arguments["num_2"] = input("escolher o segundo numero da operacao:")
    if len(args) == 3:
        arguments["ope"] = args[0]
        arguments["num_1"] = args[1]
        arguments["num_2"] = args[2]

    # TODO: Tratar ValueError
operacao = arguments["ope"]
num_1 = int(arguments["num_1"])
num_2 = int(arguments["num_2"])

if operacao not in list_ope:
    operacao = input("Escolher o tipo de operação (sum,mult,div ou sub):")

if operacao == "sum":
    resultado = num_1 + num_2
    print(f"o resultado foi {resultado}")

elif operacao == "sub":
    resultado = num_1 - num_2
    print(f"o resultado foi {resultado}")

elif operacao == "mult":
    resultado = num_1 * num_2
    print(f"o resultado foi {resultado}")

elif operacao == "div":
    resultado = num_1 / num_2
    print(f"o resultado foi {resultado}")
