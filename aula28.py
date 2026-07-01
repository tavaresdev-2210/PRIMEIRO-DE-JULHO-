""""
#Formatação de strings 
#f - float
x ou X - hexadecimal 
(caracteres) (<>^) (quantidade)
> - Esquerda 
<- Direita
^ - Centro
= - Força o número a aparecer antes dos zeros 
Sinal - + ou - 
Ex.: 0 > -100,.1f
Convertion Flags -!r !s !a  !repr___!str___!ask
"""
#Exemplo de Caracteres
#virgula separa o milhar, ja o .2f serve para colocar quantos decimais
#decidir no terminal, como o exemplo visto acima 
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: <20}')
print(f'{variavel: >20}')
print(f'{variavel: ^20}')
print(f'{1000.9242920032:,.2f}')
print(f'O hexadecimal de 1500 é % {1500:08X}')
print(f'{variavel!r}')