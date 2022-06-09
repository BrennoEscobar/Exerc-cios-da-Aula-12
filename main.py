#-------------------------------------------------------
#CALCULANDO A MÉDIA ARITMÉTICA

n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
n3 = float(input("Terceira nota do aluno: "))
n4 = float(input("Quarta nota do aluno: "))
m = (n1 + n2 + n3 + n4) / 4
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1, n2, n3, n4, m))
print("\n")

#-------------------------------------------------------
#CONVERSOR DE METROS PARA CENTÍMETROS
print("----Conversor de Metros para Centímetros---""-")

medida = float(input('Uma distância em metros: '))
cm = medida * 100

print('A medida de {}m corresponde a {:.0f}cm'.format(medida, cm))