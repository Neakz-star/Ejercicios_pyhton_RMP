import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio1:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 1: Sistema de Aumento de Sueldos")
        self.ventana.geometry("700x600")
        self.ventana.configure(bg="#f0f0f0")
        self.trabajadores = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 1"""
        # Título
        titulo = tk.Label(self.ventana, text="SISTEMA DE AUMENTO DE SUELDOS",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=10)
        
        # Frame entrada
        frame_entrada = ttk.LabelFrame(self.ventana, text="Registro de Trabajador")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_nombre = tk.Entry(frame_entrada, width=30)
        self.entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Sueldo Básico:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_sueldo = tk.Entry(frame_entrada, width=30)
        self.entrada_sueldo.grid(row=1, column=1, padx=5, pady=5)
        
        # Botón agregar
        btn_agregar = tk.Button(frame_entrada, text="Agregar Trabajador",
                               command=self.agregar_trabajador,
                               bg="#4CAF50", fg="white")
        btn_agregar.grid(row=2, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        
        # Frame resultados
        frame_resultados = ttk.LabelFrame(self.ventana, text="Historial de Trabajadores")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=15, width=80)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Botones inferiores
        frame_info = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_info.pack(padx=20, pady=5, fill=tk.X)
        
        tk.Label(frame_info, text="Reglas: <4000 (15%), 4000-7000 (10%), >7000 (8%)",
                font=("Arial", 9), bg="#f0f0f0").pack()
        
        frame_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_botones.pack(padx=20, pady=10, fill=tk.X)
        
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar,
                               bg="#2196F3", fg="white", width=15)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        btn_regreso = tk.Button(frame_botones, text="Regresar al Menú",
                               command=self.ventana.destroy,
                               bg="#FF9800", fg="white", width=15)
        btn_regreso.pack(side=tk.RIGHT, padx=5)
    
    def calcular_aumento(self, sueldo):
        """Calcula el aumento según el sueldo"""
        if sueldo < 4000:
            porcentaje = 0.15
        elif sueldo <= 7000:
            porcentaje = 0.10
        else:
            porcentaje = 0.08
        
        aumento = sueldo * porcentaje
        nuevo_sueldo = sueldo + aumento
        return nuevo_sueldo, aumento, porcentaje
    
    def agregar_trabajador(self):
        nombre = self.entrada_nombre.get().strip()
        sueldo_str = self.entrada_sueldo.get().strip()
        
        if not nombre or not sueldo_str:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            sueldo = float(sueldo_str)
            if sueldo < 0:
                raise ValueError("El sueldo debe ser positivo")
            
            nuevo_sueldo, aumento, porcentaje = self.calcular_aumento(sueldo)
            
            self.trabajadores.append({
                'nombre': nombre,
                'sueldo_basico': sueldo,
                'nuevo_sueldo': nuevo_sueldo,
                'aumento': aumento,
                'porcentaje': porcentaje * 100
            })
            
            self.mostrar_historial()
            self.entrada_nombre.delete(0, tk.END)
            self.entrada_sueldo.delete(0, tk.END)
            self.entrada_nombre.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un sueldo válido")
    
    def mostrar_historial(self):
        self.texto_resultado.delete(1.0, tk.END)
        texto = "=== HISTORIAL DE TRABAJADORES ===\n\n"
        for i, trabajador in enumerate(self.trabajadores, 1):
            texto += f"{i}. {trabajador['nombre']}\n"
            texto += f"   Sueldo Básico: ${trabajador['sueldo_basico']:.2f}\n"
            texto += f"   Aumento ({trabajador['porcentaje']:.0f}%): ${trabajador['aumento']:.2f}\n"
            texto += f"   Nuevo Sueldo: ${trabajador['nuevo_sueldo']:.2f}\n"
            texto += "-" * 50 + "\n\n"
        self.texto_resultado.insert(tk.END, texto)
    
    def limpiar(self):
        self.trabajadores = []
        self.texto_resultado.delete(1.0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_sueldo.delete(0, tk.END)
