"""
Fatiamento de strings
012345678
Olá Mundo 
-987654321
Fatiamento [i:f:p] inicio - fim - passo  [::]
Obs: a função len retorna a qtd 
de caracteres da str 
Normalmente quando se 'omite' o final é porque é pra ir ate o final da string
Os ':' são importantes pois indicam para o python para fazer o fatiamento 
O espaço também é um caractere
passo é de quantos em quantos caracteres ele vai pular, normalmente de 1 em 1 
"""
variavel = 'Olá Mundo' 
print(variavel[1:7])
#funcao len
#Contagem é diferente de índice! 
print(variavel[0:9:2])
print(variavel[0:len(variavel):])