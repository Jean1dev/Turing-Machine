import os

class TuringMachine:

    def __init__(self):
        print(self)

    @staticmethod
    def soma():

        numero1 = input("\n\t\t\t\t\t    Digite o Numero :   ")
        numero2 = input("\t\t\t\t\t    Digite o Numero :   ")
		
        operador1 = ""
        operador2 = ""

        i = 0
        for i in range(int(numero1)):
            operador1 += operador1 + "*" 
		

        i = 0
        for i in range(int(numero2)):
            operador2 += operador2 + "*"	
    	

        res = operador1 + " " + operador2 + ""
		#os.system("cls")

        print("\n\t\t________________________SOMA_______________________")
        print("Valores: " + res)
        
        res = list(res)
        estado = "q0"

        print("Estado Atual  |  Leu | Posicao |  Escreveu  |  Direcao  |  Proximo Estado")
        print("\n")

        i = 0
        for i in range(len(res)):

            if res[i] == "*" and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q0")
                print("\n")
                continue

            elif res[i] == " " and estado == "q0":
                print("\tq0\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q1")
                print("\n")
                res[i] = "*"
                estado = "q1"
                continue

            elif res[i] == "*" and estado == "q1":
                print("\tq1\t  "+res[i]+"\t "+str(i)+"\t     * "+" \t  D  \t\t q1")
                print("\n")
                continue

            elif res[i] == " " and estado == "q1":
                print("\tq1\t  "+res[i]+"\t "+str(i)+"\t       "+" \t  E  \t\t q2")
                print("\n")
                res[i - 1] = " "
                estado = "q2"
                print("\tq2\t  "+res[i]+"\t "+str(i - 1)+"\t       "+" \t  FIM  \t\t q2")
                break

            print("\n")
            print("\n")
            result = ''.join(res)
            print("Resultado: " + result)
        #CODIGO DO HADDADA PRA BAIXO

