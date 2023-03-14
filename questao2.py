# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
#ele calcule a sequência de Fibonacci e 
#retorne uma mensagem avisando se o número informado pertence ou não a sequência.7

'''
Usei a lógica de usar um while loop para inserir os resultados na lista, apenas
se o número escolhido for menor ou igual ao atual da lista
'''

def NumIsInFib(num):
    '''
    Retorna verdadeiro, caso um número esteja presente na sequência de Fibonacci.

    :param num: número que será verificado se faz parte da sequência de Fibonacci.
    :type num: int
    :return: True se o número estiver na sequêcia e False se não estiver.
    :rtype: bool

    '''

    #inicializei uma lista com os dois primeiros números da sequência
    fib = [0, 1]
    #criei um índice para realizar os cálculos dentro do loop, percorrendo a lista
    index = 0

    while True:
        
        #current se refere ao número da sequência atual
        current = fib[index] + fib[index + 1]
        fib.append(current)

        if current >= num:
            break
        
        index += 1

    if num not in fib:
        return False
    
    return True

num = int(input('Digite um número: '))
   
if NumIsInFib(10):
    print(f'O número {num} está presente na sequência de Fibonacci')
else:
    print(f'O número {num} não está presente na sequência de Fibonacci')