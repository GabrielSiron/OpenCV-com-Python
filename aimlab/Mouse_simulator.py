import serial
 
com_port = serial.Serial('COM48', 115200)

def Mouse_moviment(x,y,sens_ingame):
	x = x*sens_ingame/4
	y = -y*sens_ingame/4
	Xstr="move/X"+str(x)
	Ystr="|move/Y"+str(y)+"!"
	message = Xstr + Ystr
	com_port.write(message.encode())
  
def Mouse_click():
    com_port.write(b"c")

