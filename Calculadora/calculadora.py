#coding:utf-8
import functions

print("#" * 2 + "Seja Bem vindo!" + 2 * "#")
functions.separador()

loop = True
while loop == True:
    try:
        num,op,num2 = input("conta: ").split(" ")

        num = str(num)
        op = str(op)
        num2 = str(num2)

        convertido = functions.conversao(num, num2)

        numNormal = convertido[0]
        num2Normal = convertido[1]

        if op == "+":
            functions.separador()
            print(functions.soma(numNormal, num2Normal, num, num2, op))
            loop = functions.sair()
        elif op == "-":
            functions.separador()
            print(functions.subt(numNormal, num2Normal, num, num2, op)) 
            loop = functions.sair()
        elif op == "/":
            functions.separador()
            print(functions.divi(numNormal, num2Normal, num, num2, op))
            loop = functions.sair()
        elif op == "*":
            functions.separador()
            print(functions.multi(numNormal, num2Normal, num, num2, op))
            loop = functions.sair()
        elif op == "^":
            functions.separador()
            print(functions.expo(numNormal, num2Normal, num, num2, op))
            loop = functions.sair()
        else:
            functions.separador()
            print("Opção inválida")
    except:
        functions.separador()
        print("Digite apenas números!")