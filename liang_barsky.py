window = [ 1 , 1 , 7 , 6 ] # x_izq , y_inf , x_der , y_sup 
lineas = [ [ 0 , 3 , 4 , 5 ] , [ 0 , 3 , 4 , 5 ]  , [ 0 , 3 , 4 , 5 ] ] # x_i , y_i , x_f , y_f
line_number = 0

def isInWindow( x , y ):
	if window[0] <= x and x <= window[2] and window[1] <= y and y <= window[3]:
		return True
	else:
		return False

def analisis_superior( linea ):
	print("    Analisis superior")
	u = (window[3] - linea[1] ) / ( linea[3] - linea[1] )
	if u >= 0 and u <= 1:
		x_clip = linea[0] + u * ( linea[2] - linea[0] )
		if isInWindow( x_clip , window[3] ):
			print("\tPunto de recorte: (" + str(window[3]) + "," + str(x_clip) + ")" )
		else:
			print("\tEl punto se encuentra fuera de la ventana")
	else:
		print("\tNo cumple con condiciones")

def analisis_inferior( linea ):
	print("    Analisis inferior")
	u = (window[1] - linea[1] ) / ( linea[3] - linea[1] )
	if u >= 0 and u <= 1:
		x_clip = linea[0] + u * ( linea[2] - linea[0] )
		if isInWindow( x_clip , window[1] ):
			print("\tPunto de recorte: (" + str(window[3]) + "," + str(x_clip) + ")" )
		else:
			print("\tEl punto se encuentra fuera de la ventana")
	else:
		print("\tNo cumple con condiciones")

def analisis_izquierdo( linea ):
	print("    Analisis izquierdo")
	u = (window[0] - linea[0] ) / ( linea[2] - linea[0] )
	if u >= 0 and u <= 1:
		y_clip = linea[1] + u * ( linea[3] - linea[1] )
		if isInWindow( window[0] , y_clip ):
			print("\tPunto de recorte: (" + str(window[0]) + "," + str(y_clip) + ")" )
		else:
			print("\tEl punto se encuentra fuera de la ventana")
	else:
		print("\tNo cumple con condiciones")

def analisis_derecho( linea ):
	print("    Analisis derecho")
	u = (window[2] - linea[0] ) / ( linea[2] - linea[0] )
	if u >= 0 and u <= 1:
		y_clip = linea[1] + u * ( linea[3] - linea[1] )
		if isInWindow( window[2] , y_clip ):
			print("\tPunto de recorte: (" + str(window[2]) + "," + str(y_clip) + ")" )
		else:
			print("\tEl punto se encuentra fuera de la ventana")
	else:
		print("\tNo cumple con condiciones")

def analisis_de_linea( linea ):
	print("")
	analisis_superior( linea )
	analisis_inferior( linea )
	analisis_izquierdo( linea )
	analisis_derecho( linea )

for i in lineas:
	line_number+=1
	print("\nLinea " + str(line_number) + ":")
	analisis_de_linea(i)

print("")
