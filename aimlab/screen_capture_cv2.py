import mss
import numpy
import cv2

with mss.mss() as sct:
    monitor = {"top": 240, "left": 560, "width": 800, "height": 600}

def captura_de_tela():
    global monitor
    frame = numpy.array(sct.grab(monitor))
    return frame

















   
