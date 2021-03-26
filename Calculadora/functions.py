#coding:utf-8
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def soma(numNormal, num2Normal, num, num2, op):
    result = numNormal + num2Normal 
    resultFormatado = locale.currency(result, grouping=True, symbol=None)
    conta = f'{num} {op} {num2} = {resultFormatado}'
    return conta

def subt(numNormal, num2Normal, num, num2, op):
    result = numNormal - num2Normal 
    resultFormatado = locale.currency(result, grouping=True, symbol=None)
    conta = f'{num} {op} {num2} = {resultFormatado}'
    return conta

def divi(numNormal, num2Normal, num, num2, op):
    result = numNormal / num2Normal 
    resultFormatado = locale.currency(result, grouping=True, symbol=None)
    conta = f'{num} {op} {num2} = {resultFormatado}'
    return conta

def mult(numNormal, num2Normal, num, num2, op):
    result = numNormal * num2Normal 
    resultFormatado = locale.currency(result, grouping=True, symbol=None)
    conta = f'{num} {op} {num2} = {resultFormatado}'
    return conta

def expo(numNormal, num2Normal, num, num2, op):
    result = numNormal ** num2Normal 
    resultFormatado = locale.currency(result, grouping=True, symbol=None)
    conta = f'{num} {op} {num2} = {resultFormatado}'
    return conta

def conversao(num, num2):
    numNormal = str(num).replace(",", ".")
    num2Normal = str(num2).replace(",", ".")
    numNormal = float(numNormal)
    num2Normal = float(num2Normal)
    return numNormal, num2Normal

def separador():
    print("-" * 20)  

def sair():
    while True:
        separador()
        opcao = str(input("Deseja continuar (s/n) ?: "))
        if opcao == "sim":
            loop = True
            print("\n")
            break
        elif opcao == "não":
            loop = False
            separador()
            print("Calculadora finalizada com sucesso!")
            break
        else:
            print("Digite apenas 's' ou 'n' !")