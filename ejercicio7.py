import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio7:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 7: Suma de Números Enteros")
        self.ventana.geometry("600x500")
        self.ventana.configure(bg="#f0f0f0")
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 7"""
        titulo = tk.Label(self.ventana, text="SUMA DE LOS PRIMEROS N NÚMEROS",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=20)
        frame_entrada = ttk.LabelFrame(self.ventana, text="Ingresa un número positivo")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Número (n):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=10)
        self.entrada_n = tk.Entry(frame_entrada, width=20, font=("Arial", 12))
        self.entrada_n.grid(row=0, column=1, padx=5, pady=10)
        self.entrada_n.bind("<Return>", lambda e: self.calcular_suma())
        btn_calcular = tk.Button(frame_entrada, text="Calcular",
                                command=self.calcular_suma,
                                bg="#4CAF50", fg="white", width=15)
        btn_calcular.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        frame_resultados = ttk.LabelFrame(self.ventana, text="Resultado")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=15)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        frame_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_botones.pack(padx=20, pady=10, fill=tk.X)
        
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar,
                               bg="#2196F3", fg="white", width=15)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        btn_regreso = tk.Button(frame_botones, text="Regresar al Menú",
                               command=self.ventana.destroy,
                               bg="#FF9800", fg="white", width=15)
        btn_regreso.pack(side=tk.RIGHT, padx=5)
    
    def calcular_suma(self):
        n_str = self.entrada_n.get().strip()
        
        if not n_str:
            messagebox.showerror("Error", "Por favor ingresa un número")
            return
        
        try:
            n = int(n_str)
            
            if n <= 0:
                messagebox.showerror("Error", "El número debe ser positivo")
                return
            numeros = list(range(1, n + 1))
            suma_total = sum(numeros)
            texto = f"Suma de los primeros {n} números enteros:\n\n"
            texto += "Números: " + " + ".join(map(str, numeros)) + "\n\n"
            texto += f"Fórmula: n(n+1)/2 = {n}×{n+1}/2 = {suma_total}\n\n"
            texto += f"SUMA TOTAL: {suma_total}"
            
            self.texto_resultado.delete(1.0, tk.END)
            self.texto_resultado.insert(tk.END, texto)
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido")
    
    def limpiar(self):
        self.entrada_n.delete(0, tk.END)
        self.texto_resultado.delete(1.0, tk.END)
        self.entrada_n.focus()


