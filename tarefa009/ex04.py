codPeca1 = int (input("Informe o código da primeira peça: "))
valorPeca1 = float (input("Informe o valor da primeira peça: "))
qtdaPeca1 = int (input("Informe a quantidade da primeira peça: "))

codPeca2 = int (input("Informe o código da segunda peça: "))
valorPeca2 = float (input("Informe o valor da segunda peça: "))
qtdaPeca2 = int (input("Informe a quantidade da segunda peça: "))

IPI = float(input("Informe o valor do IPI"))

porcIPI = (valorPeca1*qtdaPeca1 + valorPeca2*qtdaPeca2)*(IPI/100+1)

print("A porcentagem do IPI e a ser acrescida nas peças é {}".format(IPI))