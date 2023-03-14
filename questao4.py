'''
4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e 
o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. 
Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

'''
#carro: rp -> franca
#caminhao franca -> rp
def Tempo(vel_obj1, vel_obj2, distancia):
    '''
    Retorna o tempo em que dois objetos vão se encontrar, tendo como base suas velocidades e a distância.

    :param vel_obj1: Velocidade em km/h de um objeto.
    :type vel_obj1: float
    :param vel_obj2: Velocidade em km/h de um outro objeto.
    :type vel_obj2: float
    :param distancia: Distância em que os dois objetos estarão percorrendo.
    :type distancia: float
    :return: Tempo em horas.
    rtype: float
    '''
    return distancia/(vel_obj1 + vel_obj2)

def Distancia(vel_obj, tempo):
    '''
    Retorna a distância, tendo como base a velocidade e o tempo.
    distancia = velocidade x tempo

    :param vel_obj: Velocidade de um objeto em km/h
    :type vel_obj: float
    :param tempo: Tempo em horas
    :type tempo: float
    :return: Distância em km.
    rtype: float
    '''
    return vel_obj * tempo

#Primeiramente decidi calcular o tempo em que o carro e o caminhão iriam demorar para se encontrar na rodovia.
#Com esse resultado poderia saber quantos km eles iriam percorrer até chegar ao ponto de encontro.
#O carro percorreu uma distância maior do que o caminhão para chegar até esse ponto.
#E levando em consideração que o carro está saindo da cidade de RP, podemos concluir que ele está mais distante.
#Logo, o caminhão está mais perto.
#O pedágio acaba não interferindo, pois o carro é bem mais rápido que o caminhão.

velocidade_carro = 110
velocidade_caminhao = 80

distancia_RP = 100

tempo_encontro = Tempo(velocidade_carro, velocidade_caminhao, distancia_RP)
distancia_encontro_carro = Distancia(velocidade_carro, tempo_encontro)
distancia_encontro_caminhao = Distancia(velocidade_caminhao, tempo_encontro)

print(f'O tempo para o encontro será de: {tempo_encontro:.2f} horas')
print(f'Para chegar ao ponto de encontro o carro percorreu: {distancia_encontro_carro:.2f} km')
print(f'Para chegar ao ponto de encontro o caminhão percorreu: {distancia_encontro_caminhao:.2f} km')

if distancia_encontro_caminhao < distancia_encontro_carro:
    print('O caminhão vai estar mais próximo da cidade de Ribeirão Preto')
else:
    print('O carro estará mais próximo da cidade de Ribeirão Preto')