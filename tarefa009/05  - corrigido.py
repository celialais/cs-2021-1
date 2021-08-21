#Mostra quantos salários míminos a pessoa recebe
salMinino = float (input("Entre com valor do salario minimo: "))
seuSalario = float (input ("Entre com valor do seu salario: "))

qtdSalario = seuSalario / salMinino #cálculo da quantidade de salários mínimos recebidos

print("O seu salário é referente a {} salários mínimos".format(qtdSalario))