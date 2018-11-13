import os


class TuringMachine:

    def __init__(self):
        print(self)

    @staticmethod
    def getInputData():
        return input("\n\t\t\t\t\t    Digite o Numero :   ")

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
