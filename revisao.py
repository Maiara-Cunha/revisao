#comentarios
# tipos de dados
a = 23 #int
b = 25.4 #float
c = "Proz" # strg
d = True  #bool

#Concatenação
e = str(a) + " " + c
print(e)

#Criando Listas
lista = [a, b, c, d, e]
print(lista)

#Adicionando dados em uma lista
lista.append(56.8)
print(lista)

#removendo dados de uma lista (pop usa o indice da lista que começa sempre em 0)
lista.pop(2)
print(lista)

#removendo dados de uma lista (remove usa o elemento digitado )
lista.remove(23)
print(lista)

##estruturas condicionais
#simples

idade = 16

if (idade >= 18):
  print("Você é Maior de Idade.")

else:
  print("Você é Menor de Idade.")

  ##estruturas condicionais
#composta

nota = 9.9

if (nota >= 7):
  print("Você foi Aprovado.")
elif((nota >= 4) & (nota < 7)):
  print("você está em Recuperação.")
else:
  print("Você está Reprovado.")

#Estruturas de Repetição
for i in range (10):
  print(i)

for i in range (10):
  print(i + 1)

i = 0
while (i <= 5 ):
  print(i)
  i = i + 1

#interação em lista

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lista1:
  print("numero: " + str(i))