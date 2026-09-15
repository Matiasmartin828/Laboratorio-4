### LABORATORIO 4
### LABORATORIO 4
### AUTORES MATÍAS MARTIN E IVO DI MARCO
### AUTORES MATÍAS MARTIN E IVO DI MARCO
### LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-4.git
### LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-4.git

import tkinter as tk

def calcular_determinante_a():
    try:
        asd=0
    except ValueError:
        print("Error")

def calcular_x():
    try:
        asd=0
    except ValueError:
        print("Error")

def borrar_valores():
    try:
        asd=0
    except ValueError:
        print("Error")

ventana = tk.Tk()                                                                                   #Creo la ventana principal
ventana.title("Resolución de sistemas de ecuaciones lineales mediante la Regla de Cramer")
ventana.geometry("500x300")
marco_principal = tk.Frame(ventana, padx=20, pady=20)                                       
marco_principal.pack()
frame_dimension = tk.LabelFrame(marco_principal, text="Dimensión", padx=10, pady=10)
frame_dimension.grid(row=0, column=0, sticky="we", padx=(0, 20))                                    #Creo un marco para los botones de la dimensión de la matriz
dimension = tk.IntVar()                                                                             #Creo la variable de control para los botones de la dimensión de la matriz
dimension.set(3)
tk.Radiobutton(frame_dimension, text="2 x 2", variable=dimension, value=2).pack(anchor="w")         #Creo los botones para seleccionar la dimensión de la matriz alineados a la izquierda
tk.Radiobutton(frame_dimension, text="3 x 3", variable=dimension, value=3).pack(anchor="w")
tk.Radiobutton(frame_dimension, text="4 x 4", variable=dimension, value=4).pack(anchor="w")
texto_matrices = tk.Frame(marco_principal)                                                          #Creo un marco para los textos de las matrices y los campos de entrada
texto_matrices.grid(row=0, column=1)

tk.Label(texto_matrices, text="A", font=("Arial", 12, "bold")).grid(row=0, column=1, columnspan=4)  #Creo los textos de las matrices A, b y x en arial 12 y en negrita
tk.Label(texto_matrices, text="b", font=("Arial", 12, "bold")).grid(row=0, column=6)
tk.Label(texto_matrices, text="x", font=("Arial", 12, "bold")).grid(row=0, column=8)

for i in range(4):                                                                                  #Creo los textos de las columnas de la matriz A y el vector b
    tk.Label(texto_matrices, text=str(i)).grid(row=1, column=i+1)

matrizA = []                                                                                        #Creo una lista vacía para almacenar los campos de las matrices                          
matrizB = []
matrizResultado = []

for i in range(4):                                                                                  #Creo los campos de entrada para la matriz A, el vector b y el vector x
    tk.Label(texto_matrices, text=str(i)).grid(row=i+2, column=0)
    fila_A = []

    for j in range(4):                                                                              #Creo los campos de entrada para la matriz A
        valor_a = tk.Entry(texto_matrices, width=5, justify="center")
        valor_a.grid(row=i+2, column=j+1, padx=2, pady=2)
        fila_A.append(valor_a)
    matrizA.append(fila_A)                                                                          #Apendo los valores ingresados a la lista de la matriz A
    tk.Label(texto_matrices, text="   ").grid(row=i+2, column=5)                                           

    valor_b = tk.Entry(texto_matrices, width=5, justify="center")                                   #Creo los campos de entrada para el vector b
    valor_b.grid(row=i+2, column=6, padx=2, pady=2) 
    matrizB.append(valor_b)
    tk.Label(texto_matrices, text="   ").grid(row=i+2, column=7)

    valor_x = tk.Entry(texto_matrices, width=8, justify="center", state="readonly")                 #Creo los campos de entrada para el vector x, que serán de solo lectura
    valor_x.grid(row=i+2, column=8, padx=2, pady=2)
    matrizResultado.append(valor_x)                                                                 #Apendo los valores ingresados a la lista del vector x

frame_inferior = tk.Frame(marco_principal, pady=10)
frame_inferior.grid(row=1, column=0, columnspan=2)                                                                           

tk.Label(frame_inferior, text="Ayuda: el sistema de ecuaciones permite calcular A.x = b\nSe deben cargar los valores de A y b y luego,\nal calcular, se obtienen los valores de x", justify="center").pack(pady=10)
frame_botones = tk.Frame(frame_inferior)
frame_botones.pack()

boton_borrar = tk.Button(frame_botones, text="Borrar valores", command=borrar_valores)              #Creo el botón para borrar los valores de entrada
boton_borrar.grid(row=0, column=0, padx=10)
boton_calcular_x = tk.Button(frame_botones, text="Calcular", command=calcular_x)                    #Creo el botón para calcular el vector x
boton_calcular_x.grid(row=0, column=1, padx=10)
frame_determinante = tk.Frame(frame_inferior, pady=10)
frame_determinante.pack()
boton_calcular_determinante = tk.Button(frame_determinante, text="Calcular det.", command=calcular_determinante_a)        #Creo el botón para calcular el determinante de la matriz A
boton_calcular_determinante.grid(row=0, column=2, padx=10)

ventana.mainloop()
