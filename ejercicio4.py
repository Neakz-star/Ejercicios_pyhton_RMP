import tkinter as tk
from tkinter import ttk, messagebox


class AbrirEjercicio4:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 4: Validación de Número < 10")
        self.ventana.geometry("500x400")
        self.ventana.configure(bg="#f0f0f0")
        self.intentos = 0
        self.numero_valido = None
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 4"""
        titulo = tk.Label(self.ventana, text="VALIDACIÓN: NÚMERO MENOR QUE 10",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=20)
        frame_entrada = ttk.LabelFrame(self.ventana, text="Ingresa un número menor que 10")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Número:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=10)
        self.entrada_numero = tk.Entry(frame_entrada, width=20, font=("Arial", 12))
        self.entrada_numero.grid(row=0, column=1, padx=5, pady=10)
        self.entrada_numero.bind("<Return>", lambda e: self.validar_numero())
        btn_validar = tk.Button(frame_entrada, text="Validar",
                               command=self.validar_numero,
                               bg="#4CAF50", fg="white", width=15)
        btn_validar.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        frame_resultados = ttk.LabelFrame(self.ventana, text="Resultado")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.label_intentos = tk.Label(frame_resultados, text="Intentos: 0",
                                      font=("Arial", 12), bg="white", relief=tk.SUNKEN)
        self.label_intentos.pack(fill=tk.X, padx=5, pady=5)
        
        self.label_resultado = tk.Label(frame_resultados, text="",
                                       font=("Arial", 12), bg="white", relief=tk.SUNKEN)
        self.label_resultado.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_botones.pack(padx=20, pady=10, fill=tk.X)
        
        btn_reiniciar = tk.Button(frame_botones, text="Reiniciar", command=self.reiniciar,
                                 bg="#2196F3", fg="white", width=15)
        btn_reiniciar.pack(side=tk.LEFT, padx=5)
        
        btn_regreso = tk.Button(frame_botones, text="Regresar al Menú",
                               command=self.ventana.destroy,
                               bg="#FF9800", fg="white", width=15)
        btn_regreso.pack(side=tk.RIGHT, padx=5)
    
    def validar_numero(self):
        numero_str = self.entrada_numero.get().strip()
        
        if not numero_str:
            messagebox.showerror("Error", "Por favor ingresa un número")
            return
        
        try:
            numero = int(numero_str)
            self.intentos += 1
            
            if numero < 10:
                self.numero_valido = numero
                self.label_resultado.config(text=f"Correcto\nNúmero: {numero}\nIntentos: {self.intentos}",
                                           fg="green")
                self.entrada_numero.config(state=tk.DISABLED)
            else:
                self.label_resultado.config(text=f"Error: debe ser menor que 10\nIntento: {self.intentos}",
                                           fg="red")
            
            self.label_intentos.config(text=f"Intentos: {self.intentos}")
            self.entrada_numero.delete(0, tk.END)
            self.entrada_numero.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido")
    
    def reiniciar(self):
        self.intentos = 0
        self.numero_valido = None
        self.entrada_numero.config(state=tk.NORMAL)
        self.entrada_numero.delete(0, tk.END)
        self.label_intentos.config(text="Intentos: 0")
        self.label_resultado.config(text="")
        self.entrada_numero.focus()


