import cv2
import numpy as np
from math import sqrt
import Mouse_simulator as ms
import keyboard
import screen_capture_cv2 as cap

def mask():
  # filtro para bolas azuis
  low =  np.array([88,133,0])
  high = np.array([97,255,255])
  frame = cap.captura_de_tela()
  frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(frame_HSV, low, high)
  return mask

def bound_detection(mask):
  
  # achando, de fato, as bolas
  _, thresh = cv2.threshold(mask, 127, 255, 0)
  contorno , _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  for c in contorno:
    momento = cv2.moments(c)
    
    if momento["m00"] != 0:
      Xcenter = int(momento["m10"]/momento["m00"])
      Ycenter = int(momento["m01"]/momento["m00"]) 
      distance = int(find_distance(Xcenter, Ycenter))
      return distance, Xcenter, Ycenter
    
  return 0, 0, 0

# distancia entre as bolas
def find_distance(x, y):
  h = sqrt((400-x)**2 + (310-y)**2)
  return h

while True:
  
  start_aim=0
  
  if keyboard.is_pressed('c'):
    start_aim=1
    
  while start_aim:
    distance, pontoX, pontoY = bound_detection(mask()) 
    
    if distance != pontoY:
      pontoX = pontoX - 400
      pontoY = pontoY - 310
      pontoY = pontoY*-1
      ms.Mouse_moviment(pontoX*0.9,pontoY*0.9,1)
      
      if distance <= 22:
        keyboard.send('ctrl')
        
      if keyboard.is_pressed('m'):
        start_aim=0
        
    if keyboard.is_pressed('b'):
      break  
