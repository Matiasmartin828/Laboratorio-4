# LABORATORIO 4
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-4.git

import tkinter as tk
import numpy as np

def calcular_determinante_a():
    try:
        d = dimension.get()                                                                         #Consulto el valor de la dimensión de la matriz A
        A = np.zeros((d, d))
        
        for i in range(d):                                                                          #Cargo la matriz A con los valores ingresados
            for j in range(d):
                A[i][j] = float(matrizA[i][j].get())
        resultado = np.linalg.det(A)
        
        valor_determinante.config(state="normal") 
        valor_determinante.delete(0, tk.END)                                                     
        valor_determinante.insert(0, str(round(resultado, 4)))                                                                      
        valor_determinante.config(state="readonly")

    except ValueError:
        print("Error: Ingrese solo números en la matriz A.")
    except:
        print("Error al calcular el determinante.")

def calcular_x():
    try:
        d = dimension.get()
        A = np.zeros((d, d))                                                                            #Creo una matriz A de ceros de tamaño d x d
        b = np.zeros(d)                                                                                 #Creo un vector b de ceros de tamaño d
        for i in range(d):                                                                              #Cargo los valores de la matriz A y el vector b 
            for j in range(d):
                A[i][j] = float(matrizA[i][j].get())
            b[i] = float(matrizB[i].get())
            
        det_A = np.linalg.det(A)                                                                        #Calculo el determinante de la matriz A
        
        if np.isclose(det_A, 0):                                                                        #Si el determinante es 0, el sistema no tiene solución única
            print("El determinante es 0. El sistema no tiene solución única.")
            return
            
        for col in range(d):                                                                            #Recorro las columnas de la matriz A para calcular los valores de x usando la Regla de Cramer
            matriz = A.copy()                                                                               
            matriz[:, col] = b                                                                          #Reemplazo la columna en posición col de la matriz A por el vector b         
            
            det_matriz = np.linalg.det(matriz)      
            valor_x = det_matriz / det_A                                                                #Calculo el valor de x en la posición col usando la Regla de Cramer
            
            matrizResultado[col].config(state="normal")
            matrizResultado[col].delete(0, tk.END)
            matrizResultado[col].insert(0, str(round(valor_x, 4)))
            matrizResultado[col].config(state="readonly")
    except ValueError:
        print("Error: Ingrese solo números.")
    except:
        print("Error al calcular el vector x.")

def lugares_innecesarios():
    try:
        d = dimension.get()                                                                         #Consulto el valor de la dimensión de la matriz A
        for i in range(4):                                                                          #Recorro las filas de la matriz A y el vector b
            for j in range(4):                                                                      #Recorro las columnas de la matriz A
                if i >= d or j >= d:                                                                #Si la fila o columna es mayor o igual a la dimensión, deshabilito el campo de entrada
                    matrizA[i][j].delete(0, tk.END)
                    matrizA[i][j].config(state="readonly")
                else:                                                                               #Si no, habilito el campo de entrada
                    matrizA[i][j].config(state="normal")

            if i >= d:                                                                              #Si la fila es mayor o igual a la dimensión, deshabilito el campo de entrada del vector b
                matrizB[i].config(state="readonly")
                matrizB[i].delete(0, tk.END)
            else:                                                                                   #Si no, habilito el campo de entrada del vector b
                matrizB[i].config(state="normal")
    except:
        print("Error al desabilitar los lugares no utilizados.")

def borrar_valores():
    try:
        for i in range(4):                                                                          #Recorro la matriz A, el vector b y el vector x para borrar los valores ingresados
            for j in range(4):
                matrizA[i][j].config(state="normal")                                                
                matrizA[i][j].delete(0, tk.END)
            
            matrizB[i].config(state="normal")
            matrizB[i].delete(0, tk.END)
            
            matrizResultado[i].config(state="normal")
            matrizResultado[i].delete(0, tk.END)
            matrizResultado[i].config(state="readonly")
            
        valor_determinante.config(state="normal")
        valor_determinante.delete(0, tk.END)
        valor_determinante.config(state="readonly")
        lugares_innecesarios()                                                                                 #Llamo a la función para deshabilitar los lugares no utilizados
    except:
        print("Error al eliminar los valores.")

ventana = tk.Tk()                                                                                   #Creo la ventana principal
matrizA = []                                                                                        #Creo una lista vacía para almacenar los campos de las matrices                          
matrizB = []
matrizResultado = []
ventana.title("Resolución de sistemas de ecuaciones lineales mediante la Regla de Cramer")
ventana.geometry("500x300")
marco_principal = tk.Frame(ventana, padx=10, pady=20)                                       
marco_principal.pack()
frame_dimension = tk.LabelFrame(marco_principal, text="Dimensión", padx=10, pady=10)
frame_dimension.grid(row=0, column=0, sticky="we", padx=(0, 10))                                    #Creo un marco para los botones de la dimensión de la matriz
dimension = tk.IntVar()                                                                             #Creo la variable de control para los botones de la dimensión de la matriz
dimension.set(3)
tk.Radiobutton(frame_dimension, text="2 x 2", variable=dimension, value=2, command=lugares_innecesarios).pack(anchor="w")         #Creo los botones para seleccionar la dimensión de la matriz alineados a la izquierda
tk.Radiobutton(frame_dimension, text="3 x 3", variable=dimension, value=3, command=lugares_innecesarios).pack(anchor="w")
tk.Radiobutton(frame_dimension, text="4 x 4", variable=dimension, value=4, command=lugares_innecesarios).pack(anchor="w")
texto_matrices = tk.Frame(marco_principal)                                                          #Creo un marco para los textos de las matrices y los campos de entrada
texto_matrices.grid(row=0, column=1, padx=(0, 10))

tk.Label(texto_matrices, text="A", font=("Arial", 12, "bold")).grid(row=0, column=1, columnspan=4)  #Creo los textos de las matrices A, b y x en arial 12 y en negrita
tk.Label(texto_matrices, text="b", font=("Arial", 12, "bold")).grid(row=0, column=6)
tk.Label(texto_matrices, text="x", font=("Arial", 12, "bold")).grid(row=0, column=8)

for i in range(4):                                                                                  #Creo los textos de las columnas de la matriz A y el vector b
    tk.Label(texto_matrices, text=str(i)).grid(row=1, column=i+1)

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

frame_inferior = tk.Frame(marco_principal)                                                                #Creo un marco para los botones de calcular y borrar valores
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
boton_determinante_label = tk.Label(frame_determinante, text="Determinante: ").grid(row=0, column=0, padx=10)             #Creo el texto para el botón de calcular el determinante de la matriz A
valor_determinante = tk.Entry(frame_determinante, width=10, justify="left", state="readonly")                 #Creo el campo de entrada para mostrar el valor del determinante de la matriz A
valor_determinante.grid(row=0, column=1)
boton_calcular_determinante = tk.Button(frame_determinante, text="Calcular det.", command=calcular_determinante_a)        #Creo el botón para calcular el determinante de la matriz A
boton_calcular_determinante.grid(row=0, column=2, padx=10)

lugares_innecesarios()
ventana.mainloop()
