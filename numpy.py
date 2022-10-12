import numpy as np
import sys

a = np.array([1,2,3], dtype = 'int16')
#a = np.array([1,2,3], dtype = 'float')
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print("___________________")

#.ndim: Pegando o numero de dimensões do array
print(f"ndim: A dimensão do array b é igual: {b.ndim}")

#shape: Retorna (linhas, colunas)
print(f"shape: O numero de linhas e colunas de b: {b.shape}")

#Dtype: Retorna quanta memoria uma matriz usa
print(f"Dtype: O tipo de armazenamento em a é: {a.dtype}")

#Determinando o tipo de aramazenamento na matriz
c = np.array([1,2,3], dtype="int16")
print(f"Dtype = 'int16': Alterei o tipo de armazenamento para: {c.dtype}")

#Total de itens no array
print(f"Total de itens no array 'a': {a.size}")

#Pegando o tamanho de cada item 
print(f"Cada item em 'a' tem em bytes: {a.itemsize} de tamanho")

#Total de tamanho
print(f"O total de bytes no array é: {a.nbytes}")

#Acessando /Alterando elementos especificos de linhas e colunas

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
#Pegando um elemento especifico array[linha,coluna]
print(f"Linha 2 e coluna 6, o elemento é:  {c[1,5]}")

#Pegando uma linha especifica
print(f"A linha epsecifica é:  {c[0,]}")

#Pegando uma coluna especifica
print(f"A coluna epsecifica é:  {c[:,2]}")

#Tornando um pouco mais sofisticado matriz[linha, elemento_inicial: elemento final: passo ]
c[0,0:-1:2]


#Exemplo em 3D
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
print("________________________\n")
#Pegando um elemento especifico
#matriz[bloco, matriz, elemento]
print(d[0,1,1])
print("________________________\n")
#Substituindo valores
d[:,1,:] = [[9,9],[8,8]]
print(d)

#Initializing Different Types of Arrays

#Matriz de zeros
np.zeros((2,2,3)) #((quantidadeMatrizes, linhas, colunas))

#Matriz de um
z =np.ones((4,2,2,), dtype=np.uint8)
print(z)
#Qualquer outro numero
np.full((2,2),99)

#Qualquer outro numero
np.full_like(a,4)

#Numeros decimais aleatorios
np.random.rand(4,2) #(linhas, colunas)

#Valores inteiros aleatorios
np.random.randint(4,17, size = (3,3)) #(Entre num_inicial, num_final, size = (linhas, colunas))

#Matriz identidade
np.identity(3)

#Repetindo arrays
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)
