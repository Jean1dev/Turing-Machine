#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Turing import TuringMachine
import platform
import os


class Menu:
    __turingInstance = ''
    value_chose = 0

    def __init__(self):
        self.__turingInstance = TuringMachine()

    def clear(self):
        system = platform.system()
        if(system == "Windows"):
            os.system('cls')
        else:
            os.system('clear')

    def input(self):
        return input(" - Digite a op :   ")

    def start(self):
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|      Maquina de Turing      |")
        print("|-----------------------------|")
        print("|      1 - Soma               |")
        print("|      2 - Subtração          |")
        print("|      3 - Multiplicação      |")
        print("|      4 - Divisão            |")
        print("|      0 - Sair               |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

        self.clear()
        self.value_chose = self.input()
        self.switch()

    def switch(self):
        if self.value_chose == '1':
            self.__turingInstance.soma()

        elif self.value_chose == '2':
            self.__turingInstance.subtracao()

        elif self.value_chose == '3':
            self.__turingInstance.multiplicacao()

        elif self.value_chose == '4':
            self.__turingInstance.igualar()

        elif self.value_chose == '0':
            self.finish()

        self.start()

    def finish(self):
        exit()
