import cv2
import numpy as np #imports

cap = cv2.VideoCapture(0) #webcam

_, frame = cap.read() #pega o primeiro frame
frame = cv2.flip(frame, 1) #espelha a câmera 
canvas = np.zeros_like(frame) #tela pra pintar

bx, by = 0, 0
gx, gy = 0, 0 #pontos azuis e verdes

while True:
    _, frame = cap.read() #le a camera
    frame = cv2.flip(frame, 1) #espelha
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #joga pra HSV

    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue) #mascara pra cor azul
    contornos_azul, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #acha os contornos

    if len(contornos_azul) > 0: 
        maior_azul = max(contornos_azul, key = cv2.contourArea) #pega o maior 
        x, y, w, h = cv2.boundingRect(maior_azul) #cria o retangulo
        cx, cy = x + w//2, y + h//2  #o centro
        
        if bx == 0 and by == 0: 
            bx, by = cx, cy  #primeiro ponto

        cv2.line(canvas, (bx, by), (cx, cy), (255, 0, 0), 5) #desenha a linha pelos pontos
        bx, by = cx, cy
        
        cv2.circle(frame, (cx, cy), 10, (255, 0, 0), 2) #coloca um circulo no pincel
    else:
        bx, by = 0, 0 #zera quando nao tem mais o pincel azul

    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green) #intervalo de verde e a mascara
    contornos_verde, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #acha os contonros verdes

    if len(contornos_verde) > 0:
        maior_verde = max(contornos_verde, key=cv2.contourArea) #pega o maior contorno
        x, y, w, h = cv2.boundingRect(maior_verde) #retangulo
        cx, cy = x + w//2, y + h//2 #centro
        
        if gx == 0 and gy == 0: #se n tem ponto anterior
            gx, gy = cx, cy
            
        cv2.line(canvas, (gx, gy), (cx, cy), (0, 0, 0), 40) #vai apagando 
        gx, gy = cx, cy
        
        cv2.circle(frame, (cx, cy), 15, (0, 255, 0), -1) 
    else:
        gx, gy = 0, 0 

    result = cv2.add(frame, canvas) #junta a webcam e o desenho feito
    cv2.imshow('Pincel e borracha', result) #mostra

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows() #fecha as cameras abertas e os filtros