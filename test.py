res = ["", ""]
if True:
    pass

elif res[i] == ' ' and estado == "q6":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    estado = "q7"
    i -= 1

elif res[i] == '*' and estado == "q7":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
        "\t     * "+" \t  D  \t\t q0")
    print("\n")
    estado = "q4"
    i += 1

elif res[i] == ' ' and estado == "q7":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    estado = "q8"
    i += 1

elif res[i] == 'B' and estado == "q7":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    estado = "q9"
    i -= 1

elif res[i] == ' ' and estado == "q8":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    estado = "q9"
    i -= 1

elif res[i] == 'B' and estado == "q8":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    i += 1

elif res[i] == '*' and estado == "q9":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    i -= 1

elif res[i] == ' ' and estado == "q9":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
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
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    i += 1

elif res[i] == ' ' and estado == "q10":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    estado = "q11"
    i -= 1

elif res[i] == '*' and estado == "q11":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    i -= 1

elif res[i] == ' ' and estado == "q11":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    i -= 1

elif res[i] == 'A' and estado == "q11":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q0")
    print("\n")
    i -= 1

elif i < 0 and estado == "q11":
    print("\tq0\t  "+res[i]+"\t "+str(i) +
          "\t     * "+" \t  D  \t\t q1")
    print("\n")
    estado = "q1"
    i += 1
