import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animacao(i, contTempo, contValor):
    global camera
    global valoresVermelhoUp, valoresVermelhoDown
    global kernel

    check, frame = camera.read()
    # filtrando a imagem
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel=kernel)
    # convertendo para HSV
    filtro = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    filtro = cv2.inRange(filtro, valoresVermelhoDown,
                         valoresVermelhoUp)

    result = cv2.bitwise_and(frame, frame, mask=filtro)
    _, thresh = cv2.threshold(cv2.cvtColor(result, cv2.COLOR_BGR2GRAY), 50, 255, 0)
    contornos, hierarquia = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    area = [cv2.contourArea(c) for c in contornos]

    if area:
        cv2.drawContours(frame, contornos[area.index(max(area))], 0, (0, 255, 0), 3)

    cv2.imshow('resultado', result)
    cv2.imshow('filtro', filtro)
    cv2.imshow('frame', frame)
    cv2.imshow('thresh', thresh)

    '''
    sintaxe estranha, mas quer dizer que o tempo sera
    sempre incrementado em uma unidade em relacao a
    posicao anterior da lista.
    '''
    contTempo.append(contTempo[len(contTempo) - 1] + 1)
    contValor.append(100 * (sum(area) / (640 * 480)))

    ax.clear()
    ax.plot(contTempo, contValor)

    plt.title('Porcentagem de vermelho na imagem')
    plt.ylabel('porcentagem')

# _________________ OPENCV _________________
camera = cv2.VideoCapture(0)

#setando o intervalo de vermelho para a imagem
valoresVermelhoDown = np.array([0, 50, 50])
valoresVermelhoUp = np.array([7, 255, 255])

kernel = np.ones((3, 3), np.uint8)

# _______________ MATPLOTLIB _________________
figura = plt.figure()
ax = figura.add_subplot(1, 1, 1)

'''
fargs esta recebendo os valores iniciais do grafico (0, 0). Ele recebe como lista
pois, dentro de 'animacao' esses valores correspondem a listas, que serao atualizadas
com os novos dados
'''

ani = animation.FuncAnimation(figura, animacao, fargs=([0], [0]), interval=100)
plt.show()

cv2.destroyAllWindows()
camera.release()