import re
import os
import sys

window = [ 0.0 , 0.0 , 0.0 , 0.0 ] # x_izq , y_inf , x_der , y_sup 
lineas = [] # x_i , y_i , x_f , y_f
line_number = 0
patron_punto_inferior = re.compile('\(? *\d+\.?\d* *, *\d+\.?\d* *\)?')
patron_coordenanda = re.compile(' *\d+\.?\d* *')
patron_linea = re.compile('\d+\.?\d* \d+\.?\d* \d+\.?\d* \d+\.?\d*')

def inicio():
	print("ESTE PROGRAMA REALIZA EL ALGORITMO DE LIANG-BARSKY PARA EL RECORTE DE LÍNEAS")

def termina_programa():
	print("El programa terminará")
	sys.exit()

def obtener_lineas():
	global lineas

	if (os.path.isfile('lineas.txt')):
		if(os.stat("lineas.txt").st_size != 0):
			lines = [line.rstrip('\n') for line in open('lineas.txt')]
			for i in lines:
				if (patron_linea.match(i)):
					lineas_tmp = i.replace("\r","").split()
					lineas_tmp[0] = float(lineas_tmp[0])
					lineas_tmp[1] = float(lineas_tmp[1])
					lineas_tmp[2] = float(lineas_tmp[2])
					lineas_tmp[3] = float(lineas_tmp[3])
					lineas.append(lineas_tmp)
				else:
					print("Una o más lineas en el archivo no cumplen con el formato")
					termina_programa()
			#print(lineas)
		else:
			print("El archivo lineas.txt se encuentra vacío")
			termina_programa()
	else:
		print("No se encontró el archivo lineas.txt")
		termina_programa()

def obtener_ventana():
	global window

	punto_inferior = input("Ingresa el punto inferior izquierdo de la ventana. Solo se aceptan valores positivos (x,y): ")
	while (not patron_punto_inferior.match(punto_inferior)):
		punto_inferior = input("No es un valor valido. Ingrese nuevamente: ")

	tmp_window = punto_inferior.split(',')
	window[0] = float(tmp_window[0].replace(" ","").replace("(",""))
	window[1] = float(tmp_window[1].replace(" ","").replace(")",""))

	largo_ventana = input("Introduce el valor del largo de la ventana: ")
	while (not patron_coordenanda.match(largo_ventana)):
		largo_ventana = input("No es un valor valido. Ingrese nuevamente: ")
	window[2] = float(largo_ventana.replace(" ","")) + window[0]

	alto_ventana = input("Introduce el valor de alto de la ventana: ")	
	while (not patron_coordenanda.match(alto_ventana)):
		alto_ventana = input("No es un valor valido. Ingrese nuevamente: ")
	window[3] = float(alto_ventana.replace(" ","")) + window[1]

	print ("\n   VENTANA:\n   punto inferior izquierdo ( " + str(window[0]) + " , " + str(window[1]) +" )\n   punto superior derecho ( " + str(window[2]) + " , " + str(window[3]) + " )")


def isInWindow( x , y ): #Determina si el punto se encuentra en la ventana
	if window[0] <= x and x <= window[2] and window[1] <= y and y <= window[3]:
		return True
	else:
		return False

def clip_point( x , y):
	cadena = "  punto de recorte en ( " + str(x) + " , " + str(y) + " )"
	return cadena

def no_clip_point():
	cadena = "  no tiene punto de recorte"
	return cadena

def analisis_inferior( linea ):
	con_limite = "   Con límite inferior  :"
	u = (window[1] - linea[1] ) / ( linea[3] - linea[1] )
	if u >= 0 and u <= 1:
		x_clip = linea[0] + u * ( linea[2] - linea[0] )
		if isInWindow( x_clip , window[1] ):
			print(con_limite + clip_point( x_clip , window[1] )) 
		else:
			print(con_limite + no_clip_point())
	else:
		print(con_limite + no_clip_point())

def analisis_superior( linea ):
	con_limite = "   Con límite superior  :"
	u = (window[3] - linea[1] ) / ( linea[3] - linea[1] )
	if u >= 0 and u <= 1:
		x_clip = linea[0] + u * ( linea[2] - linea[0] )
		if isInWindow( x_clip , window[3] ):
			print(con_limite + clip_point( x_clip , window[3] ))
		else:
			print(con_limite + no_clip_point())
	else:
		print(con_limite + no_clip_point())

def analisis_izquierdo( linea ):
	con_limite = "   Con límite izquierdo :"
	u = (window[0] - linea[0] ) / ( linea[2] - linea[0] )
	if u >= 0 and u <= 1:
		y_clip = linea[1] + u * ( linea[3] - linea[1] )
		if isInWindow( window[0] , y_clip ):
			print(con_limite + clip_point(window[0],y_clip))
		else:
			print(con_limite + no_clip_point())
	else:
		print(con_limite + no_clip_point())

def analisis_derecho( linea ):
	con_limite = "   Con límite derecho   :"
	u = (window[2] - linea[0] ) / ( linea[2] - linea[0] )
	if u >= 0 and u <= 1:
		y_clip = linea[1] + u * ( linea[3] - linea[1] )
		if isInWindow( window[2] , y_clip ):
			print(con_limite + clip_point(window[2],y_clip))
		else:
			print(con_limite + no_clip_point())
	else:
		print(con_limite + no_clip_point())

def analisis_de_linea( linea ):
	analisis_inferior( linea )
	analisis_superior( linea )
	analisis_izquierdo( linea )
	analisis_derecho( linea )

#############################################################

inicio()
obtener_lineas()
obtener_ventana()

for i in lineas:
	line_number+=1
	print("\nPara linea " + str(line_number) + ": " + str(i))
	analisis_de_linea(i)
	print("")


