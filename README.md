PROGRAMA QUE EJECUTA EL ALGORITMO DE LIANG-BARSKY DE RECORTE DE LINEAS
AUTOR: NOE MARTINEZ NAREDO

ESTE PROGRAMA FUE ESCRITO EN PYTHON 3.6, Si se tiene una versión 2.X se deberán sustituir las funciones "input" por "raw_input"

	INSTALACIÓN
		WINDOWS:
			•	Ingresar a la página https://www.python.org/downloads/ y descargar la versión 3.7
			•	Ejecutar el archivo descargado y seguir las indicaciones del asistente de instalación.
			•	Una vez instalado se deberá modificar la variable de entorno Path. Para esto se deberá ingresar al panel de control y seguir la ruta Sistema y Seguridad -> Sistema -> Configuración avanzada del sistema -> Variables de entorno. Ahí se deberá editar la variable Path, preferentemene en la sección de la Variables del sistema. Una vez que se encuentra en la ventana de edición, se añade la ruta en la cual se encuentra el ejecutable de python, por ejemplo: C:\Users\Francisco\AppData\Local\Programs\Python\Python36-32
		MACOS X:
			Para fines de facilitar la intalación haremos uso de un manejador de paquetes.
			•	Abrir la terminal. Pegar y ejecutar la siguiente línea
					/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
					brew install python3.7
				Puede pedir contraseña para hacer la instalación
		DEBIAN/UBUNTU:
			•	Abrir la terminal. Pegar y ejecutar las siguientes líneas
					sudo apt-get update
					sudo apt-get install python3.7
				Puede pedir contraseña para hacer la instalación
		RED HAT:
			•	Abrir la terminal. Pegar y ejecutar la siguiente línea
					sudo yum install python
				Puede pedir contraseña para hacer la instalación

CONSIDERACIONES PREVIAS:
	Antes de la ejecución es importante considerar la sintaxis del archivo "lineas.txt", el cual se debe mantener siempre en la misma carpeta. cada línea del archivo representará una línea (geométrica). El archivo contendrá cuatro columnas representado la x inicial, y inicial, x final, y y final, respectivamente, separadas por un espacio. Ejemplo:

		3 5 9 6
		9 45 56 9
		9 12 4 78

	Si el archivo lineas.txt no existe, está vacío o no cumple con el formato, el programa terminará. El archivo puede contener n número de líneas.

FUNCIONAMIENTO:
	•	Abrir una interfaz de comandos (CMD o Terminal).
	•	Navegar (comando cd) hasta posicionarnos en la la carpeta donde se encuentra el archvo liang_barsky.py.
	•	Escribir el siguiente comando:
			python liang_barsky.python
	•	Se pedirá el punto inferior izquierdo de la ventana que se va a considerar para el recorte. El formato es (x,y) ó x,y (el programa no avanzará si el formato es incorrecto).
	•	Se pedirá también los valores de largo y alto (el programa no avanzará si el formato es incorrecto).
	(el programa no avanzará si el formato es incorrecto).
	•	El programa leerá las líneas del archivo lineas.txt y analizará si hay puntos de recorte.
	•	El programa desplegará los resultados del análisis, sus intersecciciones con la ventana línea por línea.