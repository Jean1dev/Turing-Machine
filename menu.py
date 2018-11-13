#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from Turing import TuringMachine

class Menu:
    __turingInstance = ''
    value_chose = 0

    def __init__(self):
        self.__turingInstance = TuringMachine()


    def input(self):
        return input(" - Digite a op :   ")

    def start(self):
        print("\n\t\t\t\t==============================\n")
        print("\t\t\t\t==1 - Soma  \t           ==\n")
        print("\t\t\t\t==2 - Subtração  \t      ==\n")
        print("\t\t\t\t==3 - Multiplicação      ==\n")
        print("\t\t\t\t==0 - Sair   \t          ==\n")
        print("\n\t\t\t\t==============================\n")
        self.value_chose = self.input()
        self.switch()

    def switch(self):
        if self.value_chose == '1':
            self.__turingInstance.soma()

        elif self.value_chose == '2':
            self.__turingInstance.subtracao()
        
        elif self.value_chose == '3':
            self.__turingInstance.multiplicacao()
        
        elif self.value_chose == '0':
            self.finish()

        self.start()

    def finish(self):
        exit()
        

