import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio9:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 9: Suma hasta Superar Límite")
        self.ventana.geometry("600x600")
        self.ventana.configure(bg="#f0f0f0")
        self.numeros = []
        self.suma_actual = 0
        self.limite = 100
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 9"""
        titulo = tk.Label(self.ventana, text="SUMA HASTA SUPERAR LÍMITE (100)",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=10)
        instruccion = tk.Label(self.ventana, text="Ingresa números enteros positivos",
                              font=("Arial", 10), bg="#f0f0f0")
        instruccion.pack()
        frame_entrada = ttk.LabelFrame(self.ventana, text="Ingresa un número")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Número:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=10)
        self.entrada_numero = tk.Entry(frame_entrada, width=20, font=("Arial", 12))
        self.entrada_numero.grid(row=0, column=1, padx=5, pady=10)
        self.entrada_numero.bind("<Return>", lambda e: self.agregar_numero())
        btn_agregar = tk.Button(frame_entrada, text="Agregar",
                               command=self.agregar_numero,
                               bg="#4CAF50", fg="white", width=15)
        btn_agregar.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        frame_progreso = tk.Frame(self.ventana, bg="#e3f2fd")
        frame_progreso.pack(padx=20, pady=5, fill=tk.X)
        
        tk.Label(frame_progreso, text="Suma Actual: ", bg="#e3f2fd").pack(side=tk.LEFT)
        self.label_suma = tk.Label(frame_progreso, text="0", font=("Arial", 12, "bold"),
                                  bg="#e3f2fd", fg="#1976D2")
        self.label_suma.pack(side=tk.LEFT)
        frame_resultados = ttk.LabelFrame(self.ventana, text="Números Ingresados")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=12)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        frame_stats = tk.Frame(self.ventana, bg="#f3e5f5")
        frame_stats.pack(padx=20, pady=5, fill=tk.X)
        
        self.label_stats = tk.Label(frame_stats, text="Cantidad: 0",
                                   font=("Arial", 11, "bold"), bg="#f3e5f5")
        self.label_stats.pack(pady=5)
        frame_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_botones.pack(padx=20, pady=10, fill=tk.X)
        
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar,
                               bg="#2196F3", fg="white", width=15)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        btn_regreso = tk.Button(frame_botones, text="Regresar al Menú",
                               command=self.ventana.destroy,
                               bg="#FF9800", fg="white", width=15)
        btn_regreso.pack(side=tk.RIGHT, padx=5)
    
    def agregar_numero(self):
        numero_str = self.entrada_numero.get().strip()
        
        if not numero_str:
            messagebox.showerror("Error", "Por favor ingresa un número")
            return
        
        try:
            numero = int(numero_str)
            
            if numero <= 0:
                messagebox.showerror("Error", "Ingresa un número positivo")
                return
            
            self.numeros.append(numero)
            self.suma_actual += numero
            
            self.mostrar_numeros()
            
            if self.suma_actual > self.limite:
                messagebox.showinfo("¡Límite Superado!",
                                  f"La suma ({self.suma_actual}) ha superado el límite de {self.limite}\n\n"
                                  f"Cantidad de números: {len(self.numeros)}\n"
                                  f"Suma final: {self.suma_actual}")
                self.entrada_numero.config(state=tk.DISABLED)
            
            self.entrada_numero.delete(0, tk.END)
            self.entrada_numero.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido")
    
    def mostrar_numeros(self):
        self.texto_resultado.delete(1.0, tk.END)
        texto = "Números ingresados:\n"
        texto += "-" * 30 + "\n"
        
        for i, numero in enumerate(self.numeros, 1):
            texto += f"{i}. {numero}\n"
        
        self.texto_resultado.insert(tk.END, texto)
        self.label_suma.config(text=str(self.suma_actual))
        self.label_stats.config(text=f"Cantidad: {len(self.numeros)} | Suma: {self.suma_actual}")
    
    def limpiar(self):
        self.numeros = []
        self.suma_actual = 0
        self.entrada_numero.config(state=tk.NORMAL)
        self.entrada_numero.delete(0, tk.END)
        self.texto_resultado.delete(1.0, tk.END)
        self.label_suma.config(text="0")
        self.label_stats.config(text="Cantidad: 0")
        self.entrada_numero.focus()


