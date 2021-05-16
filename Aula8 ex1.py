# exercicio aula 8 mod2

# 1.	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:

L = [5, 7, 2, 9, 4, 1, 3]
a = (len(L))
b = max(L)
c = min(L)
d = sum(L)
exerF = L.sort(reverse=True)
exerG = L.sort()

questaoA = int(input("Qual a tamanho da lista ? : \n "))
if  questaoA != a:
    print(" VOCE ESTA ERRADO !")
else:
    print (" PARABENS VOCE ACERTO !")    

questaoB = int(input("Qual o maior numero da lista: \n "))

if questaoB != b:
    print(" VOCE ESTA ERRADO! ")
else:
    print ("PARABENS VOCE ACERTOU! ")    

questaoC = int(input("Qual menor valor da lista: \n "))
if  questaoC != c :

    print( "VOCE ESTA ERRADO ! ")
else:    
    print('PARABENS VOCE ESTA CORRETO !')

questaoD = int(input("Qual o valor da soma da lista: \n "))

if questaoD != d :

    print(" VOCE ESTA ERRADO !")
else:    
    print("PARABENS VOCE ESTA CORRETO !")

questaoF = input("Ordene a lista de forma Decrescente: \n ")    
if questaoF != exerG:
    print(" ORDEM INCORRETA ! ")
else :    
    print(" PARABENS VOCE ESTA CORRETO!")

questaoG = input(" Ordene a lista de forma Crescente ! ")  
if questaoG != exerF:
    print (" VOCE ESTA ERRADO !")
else :
    print ("PARABENS VOCE ESTA CORRETO !")    






