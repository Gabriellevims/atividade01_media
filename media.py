import time
nota1 = float(input("Digite nota 1:"))
nota2 = float(input("Digite nota 2:"))
nota3 = float(input("Digite nota 3:"))
time.sleep(0.8)

while nota1<0 or nota2<0 or nota3<0 or nota1>10 or  nota2>10 or nota3>10:
   
    print("sua nota tem que está entre 0 á 10")
    nota1 = float(input("Digite nota 1:"))
 
    nota2 = float(input("Digite nota 2:"))
 
    nota3 = float(input("Digite nota 3:"))
time.sleep(0.5) 
media = (nota1 + nota2 + nota3)/3 
print ("Sua média é: %.2f" % media) 

if media<6: 
    print("REPROVADO😢.")
else: 
    print("APROVADO!😍")