print ("Informe sua idade com anos, dias e meses")
anos = int(input("Quantos anos você tem: ")) 
meses = int(input("Quantos meses: ")) 
dias = int(input("Quantos dias: "))

idadeDias = (anos*365)+(meses*30)+dias

print ("Sua idade em dias é: {}".format(idadeDias))
