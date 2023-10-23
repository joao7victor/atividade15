# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

print("o triangulo existe")
l1=float(input("digite o lado1"))
l2=float(input("digite o lado2"))
l3=float(input("digite o lado3"))

if l1+l2>l3 and l2+l3>l1 and l3+l1>l3:
    print("as medidas formam um triangulo")
else:
    print("essas medidas não formam um triangulo")