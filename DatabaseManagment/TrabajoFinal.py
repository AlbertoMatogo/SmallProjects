from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import sqlite3


##---------------Función conectar con la base de datos-----------
def conexionBBDD():
	#Creación de la conexión con SQlite
	miConexion=sqlite3.connect("Usuarios")
	#Creación del cursor
	miCursor=miConexion.cursor()
	try:
		miCursor.execute(''' 
			CREATE TABLE DATOSUSUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(10),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		#Mensage que avisa que la base de datos ha sido creada
		messagebox.showinfo("BBDD", "Se ha creado la base de datos con exito")

	except:
		messagebox.showwarning("¡Atención!", "La BBDD ya existe")

def SalirAplicacion():

	valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miNombre.set("")
	miApellido.set("")
	miPassword.set("")
	miDireccion.set("")
	textoComentario.delete(1.0, END)

def crearRegistro():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+ miNombre.get()+
		"', '"+miPassword.get()+
		"', '"+miApellido.get()+
		"','"+miDireccion.get()+
		"','"+textoComentario.get("1.0", END)+ "' )")

	miConexion.commit()
	messagebox.showinfo("BBDD","El registro se ha realizado con exito")

def leerRegistro():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+miId.get())
	Datos=miCursor.fetchall()
	for usuario in Datos:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPassword.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

def ActualizarRegistro():

	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='" + miPassword.get() +
		"', APELLIDO='" + miApellido.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0",END) + 
		"' WHERE ID=" + miId.get())

	miConexion.commit()
	messagebox.showinfo("BBDD","El registro se ha actualizado con exito")

def BorrarRegisto():

	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

	miConexion.commit()
	messagebox.showinfo("BBDD","El registro ha sido eliminado con exito")


root=Tk()
#Ícono de la aplicación
root.iconbitmap("bbdd1.ico")
root.title("Gestión BBDD")

#Creación del menu e incluir los elementos que debe de incluir la barra
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)
BBDDMenu=Menu(barraMenu, tearoff=0)
BBDDMenu.add_command(label="Conectar", command=conexionBBDD)
BBDDMenu.add_command(label="Salir", command=SalirAplicacion)

BorrarMenu=Menu(barraMenu, tearoff=0)
BorrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

CRUDMenu=Menu(barraMenu, tearoff=0)
CRUDMenu.add_command(label="Crear", command=crearRegistro)
CRUDMenu.add_command(label="Leer", command=leerRegistro)
CRUDMenu.add_command(label="Actualizar", command=ActualizarRegistro)
CRUDMenu.add_command(label="Borrar", command=BorrarRegisto)

AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=BBDDMenu)
barraMenu.add_cascade(label="Borrar", menu=BorrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

#---------Creación del primer frame--------------------- 

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPassword=StringVar()
miDireccion=StringVar()

miFrame=Frame(root)
miFrame.pack()
#Se procede a crear los cuadros donde se introduciran los respectivos valores
cuadroId=Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, padx=10, pady=10)
Idlabel=Label(miFrame, text="ID:")
Idlabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="left")
Nombrelabel=Label(miFrame, text="Nombre:")
Nombrelabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroPassword=Entry(miFrame, textvariable=miPassword)
cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")
PasswordLabel=Label(miFrame, text="Password:")
PasswordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)
DireccionLabel=Label(miFrame, text="Dirección:")
DireccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)
textoLabel=Label(miFrame, text="Comentarios:")
textoLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#----------Creación del segundo frame------
miFrame1=Frame(root)
miFrame1.pack()

botonCrear=Button(miFrame1, text="Crear", command=crearRegistro)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame1, text="Leer", command=leerRegistro)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame1, text="Actualizar", command=ActualizarRegistro)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame1, text="Borrar",command=BorrarRegisto)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)
root.mainloop()
