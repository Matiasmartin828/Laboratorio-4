
import customtkinter as ctk
import numpy as np
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Labo_IV(ctk.CTk): #Clase de la libreria ctk para construir la interfaz grafica
    def __init__(self): #constructor
        super().__init__()
        self.title("Determinantes y Sistema de Cramer")
        self.geometry("700x620")

        self.n = 3  # tamaño inicial de la matriz
        self.entries_a = []  # entries de la matriz A
        self.entries_b = []  # entries del vector b

        #ventanas de la interfaz
        self.build_size_selector()
        self.build_matrix_grid()
        self.build_buttons()
        self.build_result_area()

    #Interfaz gráfica
    def build_size_selector(self):
        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)
        ctk.CTkLabel(frame, text="Tamaño de la matriz (n x n):").pack(side="left", padx=5)
        self.size_var = ctk.StringVar(value=str(self.n))
        menu = ctk.CTkOptionMenu(
            frame, values=["2", "3", "4"],
            variable=self.size_var, command=self.on_size_change
        )
        menu.pack(side="left", padx=5)

    def on_size_change(self, value):
        self.n = int(value)
        self.matrix_frame.destroy()
        self.build_matrix_grid()

    def build_matrix_grid(self):
        self.matrix_frame = ctk.CTkFrame(self)
        self.matrix_frame.pack(pady=10)

        # Encabezados de la matriz y el vector
        ctk.CTkLabel(self.matrix_frame, text="Matriz A", font=("Arial", 13, "bold")).grid(
            row=0, column=0, columnspan=self.n, pady=(0, 6))
        ctk.CTkLabel(self.matrix_frame, text="x", font=("Arial", 13, "bold")).grid(
            row=0, column=self.n, pady=(0, 6))
        ctk.CTkLabel(self.matrix_frame, text="b", font=("Arial", 13, "bold"),
                     text_color="#afee04").grid(
            row=0, column=self.n + 2, pady=(0, 6))

        self.entries_a = []
        self.entries_b = []
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                e = ctk.CTkEntry(self.matrix_frame, width=50, justify="center")
                e.grid(row=i + 1, column=j, padx=3, pady=3)
                e.insert(0, "0")
                fila.append(e)
            self.entries_a.append(fila)

            # columna "x"
            ctk.CTkLabel(self.matrix_frame, text=f"x{i + 1}", width=40,
                         fg_color="gray25", corner_radius=6).grid(
                row=i + 1, column=self.n, padx=(15, 5), pady=3)

            eb = ctk.CTkEntry(self.matrix_frame, width=50, justify="center",
                               fg_color="#2b7a4b")
            eb.grid(row=i + 1, column=self.n + 2, padx=3, pady=3)
            eb.insert(0, "0")
            self.entries_b.append(eb)

        ctk.CTkLabel(self.matrix_frame, text="=", font=("Arial", 16)).grid(
            row=self.n // 2 + 1, column=self.n + 1, padx=5)

    def build_buttons(self):
        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)
        ctk.CTkButton(frame, text="Calcular Determinante",
                      command=self.calcular_determinante).pack(side="left", padx=5)
        ctk.CTkButton(frame, text="Resolver por Cramer",
                      command=self.resolver_cramer).pack(side="left", padx=5)
        ctk.CTkButton(frame, text="Limpiar", fg_color="gray40",
                      command=self.limpiar).pack(side="left", padx=5)

    def build_result_area(self):
        self.result_box = ctk.CTkTextbox(self, width=650, height=250, font=("Courier", 13))
        self.result_box.pack(pady=10)

    #Logica matematica con numpy

    def get_matrix(self):
        try:
            A = np.array([[float(self.entries_a[i][j].get()) for j in range(self.n)]
                          for i in range(self.n)])
            b = np.array([float(self.entries_b[i].get()) for i in range(self.n)])
            return A, b
        except ValueError:
            messagebox.showerror("Error", "Todos los valores deben ser números")
            return None, None

    def calcular_determinante(self):
        A, _ = self.get_matrix()
        if A is None:
            return
        det = np.linalg.det(A)
        self.result_box.delete("1.0", "end")
        self.result_box.insert("end", f"Matriz A:\n{A}\n\nDeterminante: {det:.4f}\n")

    def resolver_cramer(self):
        A, b = self.get_matrix()
        if A is None:
            return

        det_A = np.linalg.det(A)
        self.result_box.delete("1.0", "end")

        if abs(det_A) < 1e-10:
            self.result_box.insert(
                "end", "El sistema NO tiene solución única (det(A) = 0)\n"
            )
            return

        self.result_box.insert("end", f"det(A) = {det_A:.4f}\n\n")
        for i in range(self.n):
            Ai = A.copy()
            Ai[:, i] = b  # reemplaza la columna i por el vector b
            det_Ai = np.linalg.det(Ai)
            xi = det_Ai / det_A
            self.result_box.insert(
                "end", f"det(A_{i+1}) = {det_Ai:.4f}   ->   x{i+1} = {xi:.4f}\n"
            )

    def limpiar(self):
        for fila in self.entries_a:
            for e in fila:
                e.delete(0, "end")
                e.insert(0, "0")
        for e in self.entries_b:
            e.delete(0, "end")
            e.insert(0, "0")
        self.result_box.delete("1.0", "end")


if __name__ == "__main__":
    app = Labo_IV()
    app.mainloop()