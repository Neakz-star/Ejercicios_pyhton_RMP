import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio8:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 8: Suma Acumulativa")
        self.ventana.geometry("600x600")
        self.ventana.configure(bg="#f0f0f0")
        self.numeros = []
        self.suma_acumulada = 0
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 8"""
        # Título
        titulo = tk.Label(self.ventana, text="SUMA ACUMULATIVA DE NÚMEROS",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=10)
        
        # Instrucción
        instruccion = tk.Label(self.ventana, text="Ingresa números (0 para detener)",
                              font=("Arial", 10), bg="#f0f0f0")
        instruccion.pack()
        
        # Frame entrada
        frame_entrada = ttk.LabelFrame(self.ventana, text="Ingresa un número")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Número:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=10)
        self.entrada_numero = tk.Entry(frame_entrada, width=20, font=("Arial", 12))
        self.entrada_numero.grid(row=0, column=1, padx=5, pady=10)
        self.entrada_numero.bind("<Return>", lambda e: self.agregar_numero())
        
        # Botón agregar
        btn_agregar = tk.Button(frame_entrada, text="Agregar",
                               command=self.agregar_numero,
                               bg="#4CAF50", fg="white", width=15)
        btn_agregar.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        
        # Frame resultados
        frame_resultados = ttk.LabelFrame(self.ventana, text="Números y Suma Acumulada")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=12)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Frame estadísticas
        frame_stats = tk.Frame(self.ventana, bg="#e8f5e9")
        frame_stats.pack(padx=20, pady=5, fill=tk.X)
        
        self.label_stats = tk.Label(frame_stats, text="Cantidad: 0 | Suma Total: 0",
                                    font=("Arial", 11, "bold"), bg="#e8f5e9")
        self.label_stats.pack(pady=5)
        
        # Botones inferiores
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
            numero = float(numero_str)
            
            if numero == 0:
                # Mostrar resumen final
                if self.numeros:
                    messagebox.showinfo("Resumen Final",
                                      f"Números ingresados: {len(self.numeros)}\n"
                                      f"Suma total: {self.suma_acumulada:.2f}")
                else:
                    messagebox.showinfo("Información", "No hay números registrados")
                return
            
            self.numeros.append(numero)
            self.suma_acumulada += numero
            
            self.mostrar_acumulado()
            self.entrada_numero.delete(0, tk.END)
            self.entrada_numero.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")
    
    def mostrar_acumulado(self):
        self.texto_resultado.delete(1.0, tk.END)
        texto = "Número | Suma Acumulada\n"
        texto += "-" * 35 + "\n"
        
        acumulado = 0
        for numero in self.numeros:
            acumulado += numero
            texto += f"{numero:7.2f} | {acumulado:14.2f}\n"
        
        self.texto_resultado.insert(tk.END, texto)
        self.label_stats.config(text=f"Cantidad: {len(self.numeros)} | Suma Total: {self.suma_acumulada:.2f}")
    
    def limpiar(self):
        self.numeros = []
        self.suma_acumulada = 0
        self.entrada_numero.delete(0, tk.END)
        self.texto_resultado.delete(1.0, tk.END)
        self.label_stats.config(text="Cantidad: 0 | Suma Total: 0")
        self.entrada_numero.focus()
