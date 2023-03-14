"""
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

Utilizei o seguinte "teste de mesa" para chegar ao resultado final.

Execução 1:
k = 1
soma = 1

Execução 2:
k = 2
soma = 3

Execução 3:
k = 3
soma = 6

Execução 4:
k = 4
soma = 10

Execução 5:
k = 5
soma = 15

Execução 6:
k = 6
soma = 21

Execução 7:
k = 7
soma = 28

Execução 8:
k = 8
soma = 36

Execução 9:
k = 9
soma = 45

Execução 10:
k = 10
soma = 55

Execução 11:
k = 11
soma = 66

Execução 12:
k = 12
soma = 78

Execução 13:
k = 13
soma = 91

o termo 'enquanto' refere-se ao loop while utilizado em diversas linguagens da computação.
Essa estrutura de loop verifica se a condição é verdadeira antes de executar as instruções.
Nesse caso, a condição era de que a variável inteira k fosse menor que a variável indice, cujo valor
atribuído era 13.
Era previsível que os comandos se repetiriam treze vezes, pois dentro do blco de código dentro do while, 
o k era apenas incrementado e ele havia começado com o valor 0 fora do loop.
Em cada repetição a variável soma, somava a si mesma, o valor de k.
Para obter o resultado final de soma fora do loop, foi necessário fazer o teste de mesa.
Quando o k chegou no valor 13 (valor que quebraria as condições do while na próxima verificação),
a variável soma tinha 91 atribuído a si.

O resultado é comprovado com o seguinte código em python: 

"""

indice = 13
soma = k = 0

while k < 13:
    k+= 1
    soma += k

print(soma) # resultado: 91