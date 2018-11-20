import os


class TuringMachine:

    def __init__(self):
        print(self)

    @staticmethod
    def getInputData():
        return input("\n\t\t\t\t\t    Digite o Numero :   ")

    # ***********************************************************************
    def divisao(self):
    # *********************************************************************** 
        numero1 = int(self.getInputData())   
        numero2 = int(self.getInputData())

        ret = ['>']
        for item in range(numero1):
            ret.append('*')

        ret.append('_')
        
        for item in range(numero2):
                ret.append('*')
        ret.append('_')
        for item in range(int(numero1 / numero2)):
                ret.append('_')
        ret.append('_')
        for item in range(numero1 % numero2):
            ret.append('_')

        estado = -1
        pos = 0
        while (estado != 21):
            marc = []
            for i in range(pos):
                marc.append(' ')
            marc.append('|')
            auxmarc = ''.join(marc)
            print('{0}'.format(auxmarc))
            aux = ''.join(ret)
            print('{0} \n'.format(aux))
            if (estado == -1):
                pos += 1
                estado += 1
            elif (estado == 0):
                if ret[pos] == '*':
                    estado = 1
                    ret[pos] = '$'
                    pos += 1
            elif (estado == 1):
                if (ret[pos] == '*'):
                    pos += 1
                else:
                    estado = 2
                    pos += 1
            elif (estado == 2):
                if (ret[pos] == '*'):
                    pos += 1
                else:
                    estado = 3
                    pos -= 1
            elif (estado == 3):
                if (ret[pos] == '*'):
                    estado = 4
                    ret[pos] = '$'
                    pos -= 1
            elif (estado == 4):
                if (ret[pos] == '*'):
                    estado = 5
                    pos -= 1
                else:
                    estado = 10
                    pos += 1
            elif (estado == 5):
                if (ret[pos] == '*'):
                    pos -= 1
                elif (ret[pos] == '$'):
                    estado = 6
                    pos += 1
                else:
                    pos -= 1
            elif (estado == 6):
                if (ret[pos] == '*'):
                    estado = 7
                    ret[pos] = '$'
                    pos += 1
                else:
                    estado = 12
                    pos += 1
            elif (estado == 7):
                if (ret[pos] == '*'):
                    pos += 1
                elif (ret[pos] == '$'):
                    estado = 3
                    pos -= 1
                else:
                    estado = 8
                    pos += 1
            elif (estado == 8):
                if (ret[pos] == '*'):
                    pos += 1
                elif (ret[pos] == '$'):
                    estado = 3
                    pos -= 1
                else:
                    estado = 3
                    pos -= 1
            elif (estado == 9):
                if (ret[pos] == '_'):
                    estado = 10
                    pos += 1
            elif (estado == 10):
                if (ret[pos] == '$'):
                    estado = 10
                    ret[pos] = '*'
                    pos += 1
                else:
                    estado = 11
                    pos += 1
            elif (estado == 11):
                if (ret[pos] == '*'):
                    pos += 1
                else:
                    estado = 5
                    ret[pos] = '*'
                    pos -= 1
            elif (estado == 12):
                if (ret[pos] == '*'):
                    pos += 1
                elif (ret[pos] == '$'):
                    estado = 13
                    pos += 1
                else:
                    estado = 20
                    ret[pos] = '>'
                    pos -= 1
            elif (estado == 13):
                if (ret[pos] == '$'):
                    pos += 1
                else:
                    estado = 14
                    pos += 1
            elif (estado == 14):
                if (ret[pos] == '*'):
                    pos += 1
                else:
                    estado = 15
                    pos += 1
            elif (estado == 15):
                if (ret[pos] == '*'):
                    pos += 1
                else:
                    estado = 16
                    ret[pos] = '*'
                    pos -= 1
            elif (estado == 16):
                if (ret[pos] == '>'):
                    estado = 18
                    pos -= 1
                elif (ret[pos] == '$'):
                    estado = 17
                    pos -= 1
                else:
                    pos -= 1
            elif (estado == 17):
                if (ret[pos] == '*'):
                    estado = 18
                    pos += 1
                else:
                    pos -= 1
            elif (estado == 18):
                if (ret[pos] == '$'):
                    estado = 19
                    ret[pos] = '*'
                    pos += 1
            elif (estado == 19):
                if (ret[pos] == '$'):
                    estado = 13
                    pos += 1
                else:
                    estado = 20
                    ret[pos] = '>'
                    pos -= 1
            elif (estado == 20):
                if (ret[pos] == '>'):
                    estado = 21
                    ret[pos] = '_'
                    pos += 1
                else:
                    ret[pos] = '_'
                    pos -= 1
        marc = []
        for i in range(pos):
            marc.append(' ')
        marc.append('|')
        auxmarc = ''.join(marc)
        print('{0} \n'.format(auxmarc))
        aux = ''.join(ret)
        print('{0} \n'.format(aux))
        p = 0
        for item in range(len(ret)):
            if (ret[item] == '>'):
                break
            p += 1
        for item in range(p):
                ret.remove('_')
        print('Fim do procedimento ')
        print(''.join(ret))

    # ***********************************************************************
    def igualar(self):
    # ***********************************************************************
        numero1 = self.getInputData()
        numero2 = self.getInputData()

        numero1 = int(numero1)
        numero2 = int(numero2)

        ret = ['>']
        for item in range(numero1):
            ret.append('*')

        ret.append('_')

        for item in range(numero2):
            ret.append('*')
        if (numero2 != 0):
            for item in range(numero1 - numero2 + 1):
                ret.append('_')
        else:
            for item in range(numero1):
                ret.append('_')
        ret.append('_')

        estado = -1
        pos = 0
        while (estado != 9):
            marc = []
            for i in range(pos):
                marc.append(' ')
            marc.append('|')
            auxmarc = ''.join(marc)
            print('{0}'.format(auxmarc))
            aux = ''.join(ret)
            print('{0} \n'.format(aux))
            
            if (estado == -1):
                pos += 1
                estado += 1
            elif (estado == 0):
                if ret[pos] == '*':
                    estado = 1
                    ret[pos] = '$'
                    pos += 1
                else:
                    estado = 7
                    pos +=1


            elif (estado == 1):
                if (ret[pos] == '*'):
                    pos += 1
                    estado = 2;
                else:
                    estado = 6
                    pos += 1


            elif (estado == 2):
                if (ret[pos] == '*'):
                    pos += 1
                else:
                    estado = 3
                    pos += 1


            elif (estado == 3):
                if (ret[pos] == '*'):
                    estado = 4
                    ret[pos] = '$'
                    pos -= 1
                elif(ret[pos] == '$'):
                    pos += 1
                else:
                    estado = 4
                    ret[pos] = '$'
                    pos -= 1


            elif (estado == 4):
                if (ret[pos] == '*'):
                    estado = 5
                    pos -= 1
                else:
                    pos -= 1


            elif (estado == 5):
                if (ret[pos] == '$'):
                    estado = 0
                    pos += 1
                else:
                    pos -= 1



            elif (estado == 6):
                if (ret[pos] == '$'):
                    pos += 1
                else:
                    estado = 7
                    ret[pos] = '$'
                    pos += 1


            elif (estado == 7):
                if (ret[pos] == '*'):
                    pos += 1
                else:
                    estado = 8
                    pos -= 1

            elif (estado == 8):
                if (ret[pos] == '>'):
                    estado = 9
                    pos += 1
                elif (ret[pos] == '$'):
                    ret[pos] = '*'
                    pos -= 1
                else:
                    ret[pos] = '_'
                    pos -= 1

        marc = []
        for i in range(pos):
            marc.append(' ')
        marc.append('|')
        auxmarc = ''.join(marc)
        print('{0} \n'.format(auxmarc))
        aux = ''.join(ret)
        print('{0} \n'.format(aux))
        print(''.join(ret))
		


    # ***********************************************************************
    def soma(self):
    # ***********************************************************************
        numero1 = self.getInputData()
        numero2 = self.getInputData()

        operador1 = ""
        operador2 = ""

        i = 0
        for i in range(int(numero1)):
            operador1 += operador1 + "*"

        i = 0
        for i in range(int(numero2)):
            operador2 += operador2 + "*"

        res = operador1 + " " + operador2 + ""
		# os.system("cls")

        print("\n\t\t________________________SOMA_______________________")
        print("Valores: " + res)

        res = list(res)
        estado = "q0"

        print("Estado Atual  |  Leu | Posicao |  Escreveu  |  Direcao  |  Proximo Estado")
        print("\n")

        i = 0
        # for i in range(len(res)):
        for i, item in enumerate(res):

            if res[i] == "*" and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q0")
                print("\n")
                continue

            elif res[i] == " " and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q1")
                print("\n")
                res[i] = "*"
                estado = "q1"
                continue

            elif res[i] == "*" and estado == "q1":
                print("\tq1\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q1")
                print("\n")
                continue

            elif res[i] == " " and estado == "q1":
                print("\tq1\t  "+res[i]+"\t "+str(i) +
                      "\t       "+" \t  E  \t\t q2")
                print("\n")
                res[i - 1] = " "
                estado = "q2"
                print("\tq2\t  "+res[i]+"\t "+str(i - 1) +
                      "\t       "+" \t  FIM  \t\t q2")
                break

        print("\n")
        print("\n")
        result = ''.join(res)
        print("Resultado: " + result)

    # **********************************************************************
    def multiplicacao(self):
    # **********************************************************************
        numero1 = self.getInputData()
        numero2 = self.getInputData()

        operador1 = ""
        operador2 = ""

        for i in numero1:
            operador1 += "*"

        for i in numero2:
            operador2 += "*"

        res = operador1 + " " + operador2 + " "

        print("\n\t\t_____________________MULTIPLICACAO______________________________")
        print("\n")
        print("Valores : " + res)

        res = list(res)
        estado = "q0"
        i = 0
        print("Estado Atual  |  Leu | Posicao |  Escreveu  |  Direcao  |  Proximo Estado")
        print("\n")

        while i != -2:

            if res[i] == "*" and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q1")
                print("\n")
                i += 1

            elif res[i] == " " and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q10")
                print("\n")
                estado = "q10"
                i += 1

            elif res[i] == "*" and estado == "q1":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q1")
                print("\n")
                i += 1

            elif res[i] == " " and estado == "q1":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q2")
                print("\n")
                estado = "q2"
                i += 1

            elif res[i] == "*" and estado == "q2":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q2")
                print("\n")
                i -= 1

            elif res[i] == "*" and estado == "q2":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q3")
                print("\n")
                estado = "q3"
                i -= 1

            elif res[i] == "B" and estado == "q2":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q2")
                print("\n")
                i += 1

            elif res[i] == "*" and estado == "q3":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q4")
                print("\n")
                estado = "q4"
                i += 1

            elif res[i] == " " and estado == "q4":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q5")
                print("\n")
                estado = "q5"
                i += 1

            elif res[i] == "B" and estado == "q4":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q4")
                print("\n")
                i += 1

            elif res[i] == "*" and estado == "q5":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q5")
                print("\n")
                i += 1

            elif res[i] == " " and estado == "q5":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q6")
                print("\n")
                estado = "q6"
                i -= 1

            elif res[i] == '*' and estado == "q6":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                      "\t     * "+" \t  D  \t\t q6")
                print("\n")
                i -= 1

            elif res[i] == ' ' and estado == "q6":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q7")
                print("\n")
                estado = "q7"
                i -= 1

            elif res[i] == '*' and estado == "q7":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q4")
                print("\n")
                estado = "q4"
                i += 1

            elif res[i] == ' ' and estado == "q7":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q8")
                print("\n")
                estado = "q8"
                i += 1

            elif res[i] == 'B' and estado == "q7":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q9")
                print("\n")
                estado = "q9"
                i -= 1

            elif res[i] == ' ' and estado == "q8":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q9")
                print("\n")
                estado = "q9"
                i -= 1

            elif res[i] == 'B' and estado == "q8":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q8")
                print("\n")
                i += 1

            elif res[i] == '*' and estado == "q9":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q9")
                print("\n")
                i -= 1

            elif res[i] == ' ' and estado == "q9":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q9")
                print("\n")
                i += 1

            elif res[i] == 'A' and estado == "q9":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q0")
                print("\n")
                estado = "q0"
                i += 1

            elif res[i] == '*' and estado == "q10":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q10")
                print("\n")
                i += 1

            elif res[i] == ' ' and estado == "q10":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q11")
                print("\n")
                estado = "q11"
                i -= 1

            elif res[i] == '*' and estado == "q11":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q11")
                print("\n")
                i -= 1

            elif res[i] == ' ' and estado == "q11":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q11")
                print("\n")
                i -= 1

            elif res[i] == 'A' and estado == "q11":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q11")
                print("\n")
                i -= 1

            elif i < 0 and estado == "q11":
                print("\tq0\t  "+res[i]+"\t "+str(i) +
                    "\t     * "+" \t  D  \t\t q1")
                print("\n")
                estado = "q1"
                i += 1


        print('\n')
        print('\n')
        result = ''.join(res)

        print("Resultado " + result )



    # ***********************************************************************
    def subtracao(self):
    # ***********************************************************************    
        numero1 = self.getInputData()
        numero2 = self.getInputData()

        operador1 = ""
        operador2 = ""

        for it in numero1:
            operador1 += "*"
        
        for it in numero2:
            operador2 += "*"

        res = operador1 + " " + operador2 + " "

        print("\n\t\t________________________SUBTRACAO________________________________")
        print("Valores " + res)
        print("Estado Atual  |  Leu | Posicao |  Escreveu  |  Direcao  |  Proximo Estado")
        print("\n")

        estado = "q0"
        res = list(res)
        i = 0
        while i != -2:
            
            if res[i] == "*" and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q0")
                print("\n")
                i += 1
            
            elif res[i] == " " and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q1")
                print("\n")
                estado = "q1"
                i += 1

            elif res[i] == "*" and estado == "q1":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q1")
                print("\n")
                i += 1

            elif res[i] == " " and estado == "q1":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q2")
                print("\n")
                res[i] = " "
                estado = "q2"
                i -= 1
            
            elif res[i] == "*" and estado == "q2":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q3")
                print("\n")
                res[i] = " "
                estado = "q3"
                i -= 1
            
            elif res[i] == "*" and estado == "q2":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q2")
                print("\n")
                break

            elif res[i] == "*" and estado == "q3":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q3")
                print("\n")
                i -= 1

            elif res[i] == " " and estado == "q3":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q3")
                print("\n")
                i -= 1

            elif i < 0:
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q4")
                print("\n")
                estado = "q4"
                i += 1

            elif res[i] == "*" and estado == "q4":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q0")
                print("\n")
                res[i] = " "
                estado = "q0"
                i += 1

            elif res[i] == " " and estado == "q4":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q4")
                print("\n")
                res[i] = " "
                estado = "q4"
                i += 1

        print('\n')
        print('\n')
        result = ''.join(res)

        print("Resultado " + result )



#a = TuringMachine()
# a.soma()
#a.subtracao()
#a.multiplicacao()
