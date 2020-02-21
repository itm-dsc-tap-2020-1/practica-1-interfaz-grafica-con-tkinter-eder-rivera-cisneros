import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import random

window = tk.Tk()
window.title("Registros")

barraMenu = Menu(window)
window.configure(menu = barraMenu)
opcionesMenu = Menu(barraMenu)
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
lista = ["Leer", "Ver peliculas", "Redes sociales"]
lista2 = ["Soltero", "Casado", "Viudo"]
style = ttk.Style()

def main():
    bari()
    pestañitas()

def sal():
    window.quit()
    window.destroy() 
    exit()

def bari():
    opcionesMenu.add_command(label = "Imprimir", command = imprimeTodo)
    opcionesMenu.add_separator()
    opcionesMenu.add_command(label = "Salir", command = sal)
    barraMenu.add_cascade(label = "Sistema", menu = opcionesMenu)

    menuAyuda = Menu(barraMenu, tearoff = 0)
    menuAyuda.add_command(label = "Acerca de ", command = informacion)
    barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

def pestañitas(): 
    tabControl.add(tab1, text = "Datos personales")
    tabControl.pack(expand = 1, fill = 'both')

    tabControl.add(tab2, text = "Datos extras")
    tabControl.pack(expand = 1, fill = 'both')

def llenado1(tab, labelito, row, col, x, y):
    if tab == 'tab1':
        return ttk.Label(tab1, text = labelito).grid(row = row, column = col, padx = 
        x, pady = y)
    else:
        return ttk.Label(tab2, text = labelito).grid(row = row, column = col, padx = 
        x, pady = y)

"""def llenEntry1(tab, row, col, px, py):
    if tab == 'tab1':
        return ttk.Entry(tab1, width = 50).grid(row = row, column = col, padx = px, pady = py)
    else:
        return ttk.Entry(tab2, width = 50).grid(row = row, column = col, padx = px, pady = py)"""

def llenCombo(tab, var):
    if tab == 'tab1':
        return ttk.Combobox(tab1, width = 50, textvariable = var, state = 
        'readonly')
    else:
        return ttk.Combobox(tab2, width = 50, textvariable = var, state = 
        'readonly')

def defBoton(tab, text, row, col, comando):
    if tab == 'tab1':
        return ttk.Button(tab1, text = text, command = comando).grid(row = row, column = col)
    else:
        return ttk.Button(tab2, text = text, command = comando).grid(row = row, column = col)

def cajita(texto):
    mBox.showinfo("INFORMACION", texto)

def chBoton(tab, texto, variable, x ,y, px, py):
    return ttk.Checkbutton(tab, text = texto, variable = variable).grid(row = x, 
    column = y, padx = px, pady = py)

def radBoton(tab, texto, variable, value, x, y, px, py):
    return ttk.Radiobutton(tab2, text = texto, variable = variable, value = 
    value).grid(row = x, column = y, padx = px, pady = py)

def informacion():
    mBox.showinfo("INFORMACION", "Programa creado por Eder Rivera Cisneros" +  
    " el dia 19 de febrero del 2020.")

def colorCambia():
    color = 'red','blue','purple','black','gray','white','green', 'yellow'
    style.configure('TFrame', background = random.choice(color))

def imprimeTodo():
    if entry_nombre.get() == '':
        cajita("LOS DATOS NO ESTAN COMPLETOS")
        return
    if entry_objetivo.get() == '':
        cajita("LOS DATOS EXTRAS NO ESTAN COMPLETOS")
        return
    else:
        cajita("LOS DATOS PERSONALES SON\n\n"+ "Nombre: " + entry_nombre.get() + 
        "\n\nApellido paterno: " + entry_Pat.get() + "\n\nApellido materno: " + entry_Mat.get() +
        "\n\nDireccion: " + entry_direccion.get() + "\n\nColonia: " + colonia_var.get() +
        "\n\nCiudad: " + ciudad_var.get() + "\n\nMunicipio: " + municipio_var.get() + 
        "\n\nLOS DATOS EXTRAS SON:\n\n" + "Te gusta: " + str(lista) + "\n\nEstado civil: " +
        str(lista2))     

def comando():
    dic = {}
    dic["nombre"] = entry_nombre.get()
    dic["apMat"] = entry_Mat.get()
    dic["apPat"] = entry_Pat.get()
    dic["dir"] = entry_direccion.get()
    dic["colonia"] = colonia_var.get()
    dic["ciudad"] = ciudad_var.get()
    dic["municipio"] = municipio_var.get()

    for k, v in dic.items():
        if not v:
            cajita("TUS DATOS NO ESTAN COMPLETOS")
            break
    else:
        cajita("Tus datos son:\n\n"+ "Nombre: " + entry_nombre.get() + "\n\nApellido paterno: "
        + entry_Pat.get() + "\n\nApellido materno: " + entry_Mat.get() + "\n\nDireccion: " +
        entry_direccion.get() + "\n\nColonia: " + colonia_var.get() + "\n\nCiudad: " + 
        ciudad_var.get() + "\n\nMunicipio: " + municipio_var.get())
        

def comando2():
    #result = "Tus gustos son:\n"
    if(leer_var.get() == 0 and peliculas_var.get() == 0 and 
    redes_var.get() == 0):
        cajita("TUS DATOS ESTAN INCOMPLETOS")
        return
    else:
        if entry_objetivo.get() == '':
            cajita("TUS DATOS ESTAN INCOMPLETOS")
            return
        if leer_var.get() == 0:
            lista.remove("Leer")
        if peliculas_var.get() == 0:
            lista.remove("Ver peliculas")
        if redes_var.get() == 0:
            lista.remove("Redes sociales")
        if option.get() != 1:
            lista2.remove("Soltero")
        if option.get() != 2:
            lista2.remove("Casado")
        if option.get() != 3:
            lista2.remove("Viudo")

    cajita('Te gusta: ' + str(lista) + '\n\nEstado civil: ' + str(lista2) + 
    "\n\nObjetivo de vida: " + entry_objetivo.get())  

lab_nombre = llenado1('tab1', "Nombre", 0, 0, 3, 3)
entry_nombre = ttk.Entry(tab1, width = 50)
entry_nombre.grid(row =0, column = 1)
#entry_nombre = llenEntry1('tab1', 0, 1, 3, 3)
#nombre = entry_nombre

lab_apellidoPat = llenado1('tab1', "Apellido Paterno", 1, 0, 3, 3)
entry_Pat = ttk.Entry(tab1, width = 50)
entry_Pat.grid(row =1, column = 1)
#entry_Pat = llenEntry1('tab1', 2, 1, 3, 3)

lab_apellidoMat = llenado1('tab1', "Apellido Materno", 2, 0, 3, 3)
entry_Mat = ttk.Entry(tab1, width = 50)
entry_Mat.grid(row =2, column = 1)
#entry_Mat = llenEntry1('tab1', 1, 1, 3, 3)

direccion = llenado1('tab1', "Direccion", 3, 0, 3, 3)
entry_direccion = ttk.Entry(tab1, width = 50)
entry_direccion.grid(row =3, column = 1)
#entry_direccion = llenEntry1('tab1', 3, 1, 3, 3)

colonia = llenado1('tab1', "Colonia", 4, 0, 3, 3)
colonia_var = tk.StringVar()
combo_one = llenCombo('tab1', colonia_var)
combo_one['values'] = ("Villas", "Periodo", "Fray")
combo_one.current(0)
combo_one.grid(row = 4, column = 1, padx = 3, pady = 3)

ciudad = llenado1('tab1', "Ciudad", 5, 0, 3, 3)
ciudad_var = tk.StringVar()
combo_two = llenCombo('tab1', ciudad_var)
combo_two['values'] = ("Morelia", "Morelos", "CD Mexico")
combo_two.current(0)
combo_two.grid(row = 5, column = 1, padx = 3, pady = 3)

municipio = llenado1('tab1', "Municipio", 6, 0, 3, 3)
municipio_var = tk.StringVar()
combo_three = llenCombo('tab1', municipio_var)
combo_three['values'] = ("Angeles", "Zinapecuaro", "Buenavista")
combo_three.current(0)
combo_three.grid(row = 6, column = 1, padx = 3, pady = 3)

boton = defBoton('tab1', "Imprimir datos personales", 7, 4, comando)
boton_color = defBoton('tab1', "Cambiar color", 8, 4, colorCambia)

#PESTAÑA 2

pasatiempos = llenado1('tab2', "Pasatiempos", 0, 0, 3, 3)
estado_civil = llenado1('tab2', "Estado Civil", 3, 0, 3, 3)
objetivo_vida = llenado1('tab2', "Objetivo de la vida", 5, 0, 3, 3)

leer_var = tk.IntVar()
check1 = chBoton(tab2, "Leer", leer_var, 1, 0, 5, 5)

peliculas_var = tk.IntVar()
check2 = chBoton(tab2, "Peliculas", peliculas_var, 1, 1, 5, 5)

redes_var = tk.IntVar()
check3 = chBoton(tab2, "Redes sociales", redes_var, 1, 2, 5, 5)

option = tk.IntVar()

rad1 = radBoton(tab2, 'Soltero', option, 1, 4, 0, 5, 5)
rad2 = radBoton(tab2, 'Casado', option, 2, 4, 1, 5, 5)
rad3 = radBoton(tab2, 'Viudo', option, 3, 4, 2, 5, 5)

entry_objetivo = ttk.Entry(tab2, width = 30)
entry_objetivo.grid(row = 6)

boton2 = defBoton('tab2', "Imprimir datos extras", 7, 3, comando2)
boton_color2 = defBoton('tab2', "Cambiar color", 8, 3, colorCambia)

main()

window.mainloop()