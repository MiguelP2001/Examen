import tkinter as tk
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", password="", db="torneo_baloncesto")
cursor = db.cursor()

cursor = db.cursor()


cursor = db.cursor()

cursor = db.cursor

cursor 

cursor
root = tk.Tk()
root.title("Control de Partido")

equipo_local_label = tk.Label(root, text="Equipo Local:")
equipo_local_entry = tk.Entry(root)
equipo_visitante_label = tk.Label(root, text="Equipo Visitante:")
equipo_visitante_entry = tk.Entry(root)
fecha_label = tk.Label(root, text="Fecha:")
fecha_entry = tk.Entry(root)
hora_label = tk.Label(root, text="Hora:")
hora_entry = tk.Entry(root)

equipo_local_label.grid(row=0, column=0)
equipo_local_entry.grid(row=0, column=1)
equipo_visitante_label.grid(row=1, column=0)
equipo_visitante_entry.grid(row=1, column=1)
fecha_label.grid(row=2, column=0)
fecha_entry.grid(row=2, column=1)
hora_label.grid(row=3, column=0)
hora_entry.grid(row=3, column=1)
