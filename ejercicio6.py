import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio6:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 6: Registro de Intentos")
        self.ventana.geometry("700x600")
        self.ventana.configure(bg="#f0f0f0")
        self.intentos = []
        self.numero_valido = None
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 6"""
        # Título
        titulo = tk.Label(self.ventana, text="REGISTRO DE INTENTOS DE VALIDACIÓN",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=10)
        
        # Frame entrada
        frame_entrada = ttk.LabelFrame(self.ventana, text="Ingresa un número entre 0 y 20")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Número:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=10)
        self.entrada_numero = tk.Entry(frame_entrada, width=20, font=("Arial", 12))
        self.entrada_numero.grid(row=0, column=1, padx=5, pady=10)
        self.entrada_numero.bind("<Return>", lambda e: self.validar_numero())
        
        # Botón validar
        btn_validar = tk.Button(frame_entrada, text="Validar",
                               command=self.validar_numero,
                               bg="#4CAF50", fg="white", width=15)
        btn_validar.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        
        # Frame resultados
        frame_resultados = ttk.LabelFrame(self.ventana, text="Historial de Intentos")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=15)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Estadísticas
        frame_stats = tk.Frame(self.ventana, bg="#e8f5e9")
        frame_stats.pack(padx=20, pady=5, fill=tk.X)
        
        self.label_stats = tk.Label(frame_stats, text="Incorrectos: 0 | Válido: No encontrado",
                                    font=("Arial", 11, "bold"), bg="#e8f5e9", justify=tk.LEFT)
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
    
    def validar_numero(self):
        numero_str = self.entrada_numero.get().strip()
        
        if not numero_str:
            messagebox.showerror("Error", "Por favor ingresa un número")
            return
        
        try:
            numero = int(numero_str)
            valido = 0 < numero < 20
            
            self.intentos.append({
                'numero': numero,
                'valido': valido
            })
            
            if valido:
                self.numero_valido = numero
                self.entrada_numero.config(state=tk.DISABLED)
            
            self.mostrar_historial()
            self.entrada_numero.delete(0, tk.END)
            self.entrada_numero.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido")
    
    def mostrar_historial(self):
        self.texto_resultado.delete(1.0, tk.END)
        texto = "=== HISTORIAL DE INTENTOS ===\n\n"
        incorrectos = 0
        
        for i, intento in enumerate(self.intentos, 1):
            estado = "✓ VÁLIDO" if intento['valido'] else "✗ INVÁLIDO"
            texto += f"{i}. Número: {intento['numero']:3} - {estado}\n"
            if not intento['valido']:
                incorrectos += 1
        
        self.texto_resultado.insert(tk.END, texto)
        
        # Actualizar estadísticas
        valid_text = f"Válido: {self.numero_valido}" if self.numero_valido else "Válido: No encontrado"
        self.label_stats.config(text=f"Incorrectos: {incorrectos} | {valid_text}")
    
    def limpiar(self):
        self.intentos = []
        self.numero_valido = None
        self.texto_resultado.delete(1.0, tk.END)
        self.label_stats.config(text="Incorrectos: 0 | Válido: No encontrado")
        self.entrada_numero.config(state=tk.NORMAL)
        self.entrada_numero.delete(0, tk.END)
        self.entrada_numero.focus()
