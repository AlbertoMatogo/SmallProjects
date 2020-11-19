
##Using basic knowledge of python to create a small calculator with a graphical interface
#the calculator has two screens. One of them shows the last operations and numbers that have been carried out
#Second screen shows results
#-The library used is Tkinter, for the creation of the graphical interface-#
'''Functions have been used instead of classes and objects. The challenge for beginners in python would be 
to make this calculator. with object-oriented programming. there are exceptions that are not handled. 
This calculator will be modified to achieve a more functional and elegant code'''

from tkinter import *
raiz=Tk()
raiz.title("Calculadora")
miFrame=Frame(raiz)
miFrame.pack()
operacion=" "
resultado=0
Boperacion=False
signo=""

##-------upper screen----------
#@Use of columnspan instruction, to determine a column number
numeroPantalla1=StringVar()
PantallaCalculadora1=Entry(miFrame, bg="white", textvariable=numeroPantalla1)
PantallaCalculadora1.grid(row=1, column=1, padx=2, pady=1,columnspan=4)
PantallaCalculadora1.config(bg="black",fg="#03f943", justify="right")

##--------lower screen---------
#@Use of columnspan instruction, to determine a column number
#@StringVar (valor reflejado en el entry) associated with the entry context variable
numeroPantalla=StringVar()
PantallaCalculadora=Entry(miFrame, bg="white", textvariable=numeroPantalla)
PantallaCalculadora.grid(row=2, column=1, padx=2, pady=5,columnspan=4)
PantallaCalculadora.config(bg="black",fg="#03f943", justify="right")

#@A function is created for the keystrokes
#@.set() send value to screen
#@.get() get the value on the screen + concatenation
#@Use of lambda functions, so that the function is not called without the user pressing the button
def numeroPulsado(num):

	global operacion
	global Boperacion
	global signo
	global contador_signo

	#Press some number or a concatenated number and you could see it in the screen
	#If some operation button is pressed, it's going to stop concatenating the number
	if Boperacion!=False:
		numeroPantalla.set(num)
		Boperacion=False
	
	else:

		numeroPantalla.set(numeroPantalla.get()+num)

	if operacion=="suma":
		signo="+"
	elif operacion=="resta":
		signo="-"
	elif operacion=="multiplicación":
		signo="x"
	elif operacion=="division":
		signo="/"

	if signo=="":
		numeroPantalla1.set(numeroPantalla.get())

	elif signo!="":
		numeroPantalla1.set(numeroPantalla1.get()+signo+numeroPantalla.get())	
		signo=""


		
def suma(num):

	global operacion
	global resultado
	global Boperacion

	resultado=float(resultado)+float(num)
	operacion="suma"
	Boperacion=True
	numeroPantalla.set(resultado)


contador_resta=0
num1=0
def resta(num):

	global operacion
	global resultado
	global contador_resta
	global num1
	global Boperacion

	if contador_resta==0:
		num1=float(num)	
		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-float(num)
		
		else:
			resultado=float(resultado)-float(num)

		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	
	contador_resta+=1
	operacion="resta"
	Boperacion=True
	
	
contador_multi=0
num1=0
def multiplicacion(num):

	global resultado
	global operacion
	global contador_multi
	global num1
	global Boperacion

	
	if contador_multi==0:
		num1=float(num)
		resultado=num1

	else:
		
		resultado=resultado*float(num)

	numeroPantalla.set(resultado)
	resultado=numeroPantalla.get()
	contador_multi+=1
	operacion="multiplicación"
	Boperacion=True
	

contador_divi=0
num1=0
def division(num):

	global resultado
	global operacion
	global contador_divi
	global num1
	global Boperacion

	
	if contador_divi==0:

		if num=="0":

			resultado="Error Zerodivision"
		else:
			print("contador igual a 0")
			num1=float(num)
			resultado=num1
			print(resultado)

	else:

		if num=="0":

			resultado="Error Zerodivision"

		else:
			resultado=resultado/float(num)

	numeroPantalla.set(resultado)
	resultado=numeroPantalla.get()
	contador_divi+=1
	operacion="division"
	Boperacion=True
	

def el_resultado():

	global resultado
	global operacion
	global contador_divi
	global contador_resta
	global contador_multi

	if operacion=="suma":

		numeroPantalla.set(float(resultado)+float(numeroPantalla.get()))
		resultado=0


	elif operacion=="resta":

		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))
		resultado=0
		contador_resta=0


	elif operacion=="multiplicación":

		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))
		resultado=0
		contador_multi=0

	elif operacion=="division":

		analisis=numeroPantalla.get()

		if analisis=="0":
			numeroPantalla.set("Error Zerodivision")

		else:
			numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))
		
		resultado=0
		contador_divi=0
	else:

		numeroPantalla.set("Error operation")

##---------row 1 buttons--------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)

boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)

boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)

botondividir=Button(miFrame, text="/", width=3, command=lambda:division(numeroPantalla.get()))
botondividir.grid(row=3, column=4)

##---------row 2 buttons--------------
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)

boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)

boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)

botonx=Button(miFrame, text="x", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
botonx.grid(row=4, column=4)

##---------row 3 buttons--------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)

boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)

botonmenos=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonmenos.grid(row=5, column=4)

##---------row 4 buttons--------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=1)

botoncoma=Button(miFrame, text=".", width=3, command=lambda:numeroPulsado("."))
botoncoma.grid(row=6, column=2)

botonigual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonigual.grid(row=6, column=3)

botonmas=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonmas.grid(row=6, column=4)

raiz.mainloop()