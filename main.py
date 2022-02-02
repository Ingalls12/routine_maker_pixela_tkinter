try:
    from tkinter import *
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
import requests
import os
from tkcalendar import Calendar, DateEntry
import datetime as dt
fecha_actual = dt.datetime.now()
fc_dia = fecha_actual.day
fc_mes = fecha_actual.month
fc_año = fecha_actual.year
#Mis datos
username = "sundae"
TOKEN = os.environ.get("TOKEN_PIXELA")
graph_id ="studygraph"
header = {
    "X-USER-TOKEN":TOKEN
}
fecha = ""

#Funciones
def escogerFecha():
    def fecha_escogida():
        global fecha
        fecha = cal.selection_get()
        lbl_fecha_escogida.config(text=cal.selection_get(),bg="white")




    top = tk.Toplevel(ventana)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=fc_año, month=fc_mes, day=fc_dia)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=fecha_escogida).pack()

def subir_info():

    actual = fecha.strftime("%Y%m%d")
    tiempo_estudiado = entry_minutos.get()

    enpoint_grafica = f"https://pixe.la/v1/users/sundae/graphs/studygraph/{actual}"
    post_params = {
        "quantity": str(tiempo_estudiado),
    }
    response=requests.put(url=enpoint_grafica,json=post_params,headers=header)
    response.raise_for_status()
#UI--------------------------------------------------------------------------------------------------------------------
ventana = Tk()
ventana.title("Mi proyecto")
ventana.config(padx=10,pady=10,bg="green")

canvas = Canvas(width=500,height=500,bg="blue")
foto_r = PhotoImage(file="images/routine.png")
canvas.create_image(250,250,image=foto_r)
canvas.grid(column=0,row=0,columnspan=3)

lbl_fecha=Label()
lbl_fecha.config(text="Ingresa Fecha",font=("Ariel",16,"italic"))
lbl_fecha.grid(column=0,row=1)

lbl_fecha_escogida= Label(bg="green")
lbl_fecha_escogida.grid(column=1,row=1)

btn_hoy = Button(text="Escoger fecha",command=escogerFecha)
btn_hoy.grid(column=2,row=1)

lbl_minutos = Label()
lbl_minutos.config(text="Ingresa minutos estudiados",font=("Ariel",16,"italic"))
lbl_minutos.grid(column=0,row=2)

entry_minutos = Entry()
entry_minutos.grid(column=1,row=2)

btn_subir = Button(text="Subir información",command=subir_info)
btn_subir.grid(column=2,row=3)
ventana.mainloop()