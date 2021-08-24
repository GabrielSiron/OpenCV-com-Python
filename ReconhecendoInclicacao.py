import cv2
import numpy as np
import math

def mostrar(img, inf, val):
    texto = "{} = {} graus".format(inf, val)

    fonte = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    escala = 2
    espess = 3
    tamanho, lixo = cv2.getTextSize(texto, fonte, escala, espess)

    cv2.putText(img, texto, (int(img.shape[1]/10 - tamanho[0]/10),
                int(img.shape[0]/10 + tamanho[1]/10)), fonte,
                escala, (0,255,0), espess)


def aplicarMascara(frameHsv, intervaloB, intervaloA):
    baixo = np.array(intervaloB)
    alto  = np.array(intervaloA)

    mask = cv2.inRange(frameHsv, baixo, alto)
    return mask

def contMaior(contorno):
    if contorno:
        d = 0
        maxi = len(contorno[0])
        for i in range(len(contorno)):
            if len(contorno[i]) > maxi:
                maxi = len(contorno[i])
                d = contorno[i]

        return d

    return 1

def desenharAngulo(img, alto, baixo):    
    cv2.line(img, (alto[0], alto[1]),
             (baixo[0], baixo[1]), (0, 255, 0), 2)
    cv2.line(img, (baixo[0] - 100, baixo[1]),
             (baixo[0] + 100, baixo[1]), (0, 255, 0), 2)
    cv2.circle(img, (baixo[0], baixo[1]), 15,
               (255, 255, 0), 2)


'''

        baixo - [101, 98, 133]
        alto  - [134, 255, 170]

'''
        
cap = cv2.VideoCapture(0)


#para salvar um vídeo do código em execução
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#out = cv2.VideoWriter('output.mp4', fourcc, 15.0, (640, 480))

while True:
    ret, frame = cap.read()
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('a', img)

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
        
        mascara = aplicarMascara(hsv, [91, 20, 115], [134, 255, 170])
        
        k = cv2.waitKey(30) & 0xFF
        
        if k == 27:
            break

        lixo, thresh = cv2.threshold(mascara, 127, 255, cv2.THRESH_BINARY)
        contorno, hierarquia = cv2.findContours(thresh, cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)

        #cv2.imshow('c', thresh)
        
        c = contMaior(contorno)

        if type(c) != int:
            area = cv2.contourArea(c)
            if cv2.contourArea(c) > 1800:
            
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                #lista = [maisBaixo, maisAlto, p3, p4] = box
                #alt = abs(maisBaixo[1] - maisAlto[1])
                #larg = abs(maisBaixo[0] - maisAlto[0])
                larg = 0
                cAlto = cBaixo = 0
                maior = 0
                menor = 640
                '''
                lista = [box[0][0], box[1][0], box[2][0], box[3][0]]
                lista.sort()
                '''
                
                for i in range(4):
                    if box[i][1] > maior:
                        maior = box[i][1]
                        cBaixo = box[i]

                            
                for j in range(4):
                    if box[j][0] < menor:
                        menor = box[j][0]
                        cAlto = box[j]
                        
                if type(cAlto) != int and type(cBaixo) != int:
                    alt = abs(cAlto[1] - cBaixo[1])
                    larg = abs(cAlto[0] - cBaixo[0])
                    
                if larg != 0:
                    tg = alt/larg
                    
                    mi = 0
                    fi = 90
                    dif2 = 0
                    while True:
                        media = int((mi+fi)/2)
                        tgM = math.tan(math.pi/180*(media))
                        dif1 = abs(tg - tgM)
                        h = ((larg**2) + (alt**2))**(1/2)
                        distancia = ((box[2][0] - box[1][0])**2 + (box[2][1] - box[1][1])**2)**(1/2)
                        frame[box[2][1]][box[2][0]] = (0, 0, 0)
                        
                        print(h/distancia)
                        
                        #print("{0:3}".format(str(dif1)))
                        #print(h)
                        
                        if dif1 == dif2 or dif1 <= 0.01:
                            #desenharAngulo(frame, cAlto, cBaixo)
                            mostrar(frame, "angulo", media)
                            break
                        
                        elif tg > tgM:
                            mi = media
                        else:
                            fi = media
                            
                        dif2 = dif1
                else:
                    mostrar(frame, "angulo", 90)
                #cv2.drawContours(frame, [box],0 ,(0, 255, 0), 2)
                
        cv2.imshow('máscara', mascara)
        cv2.imshow('imagem', frame)
        cv2.imshow('imagem mesma coisa', frame)
        #out.write(frame)
        
cap.release()
#out.release()
cv2.destroyAllWindows()
