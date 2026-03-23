import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio10:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 10: Sistema de Pago de Trabajadores")
        self.ventana.geometry("800x700")
        self.ventana.configure(bg="#f0f0f0")
        self.trabajadores = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 10"""
        titulo = tk.Label(self.ventana, text="SISTEMA DE PAGO DE TRABAJADORES",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=10)
        frame_entrada = ttk.LabelFrame(self.ventana, text="Registro de Trabajador")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_nombre = tk.Entry(frame_entrada, width=25)
        self.entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Horas Normales:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_horas_normales = tk.Entry(frame_entrada, width=25)
        self.entrada_horas_normales.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Pago/Hora Normal:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_pago_hora = tk.Entry(frame_entrada, width=25)
        self.entrada_pago_hora.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Horas Extras:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.entrada_horas_extras = tk.Entry(frame_entrada, width=25)
        self.entrada_horas_extras.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Número de Hijos:").grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        self.entrada_hijos = tk.Entry(frame_entrada, width=25)
        self.entrada_hijos.grid(row=1, column=3, padx=5, pady=5)
        btn_agregar = tk.Button(frame_entrada, text="Calcular y Registrar",
                               command=self.calcular_pago_trabajador,
                               bg="#4CAF50", fg="white", width=25)
        btn_agregar.grid(row=2, column=2, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        frame_resultados = ttk.LabelFrame(self.ventana, text="Reporte de Pagos")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=15)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        frame_info = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_info.pack(padx=20, pady=5, fill=tk.X)
        
        tk.Label(frame_info, text="Hora Extra: 50% más | Bonificación por hijo: S/. 0.50",
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
    
    def calcular_pago_trabajador(self):
        nombre = self.entrada_nombre.get().strip()
        horas_normales_str = self.entrada_horas_normales.get().strip()
        pago_hora_str = self.entrada_pago_hora.get().strip()
        horas_extras_str = self.entrada_horas_extras.get().strip()
        hijos_str = self.entrada_hijos.get().strip()
        
        if not all([nombre, horas_normales_str, pago_hora_str, horas_extras_str, hijos_str]):
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            horas_normales = float(horas_normales_str)
            pago_hora = float(pago_hora_str)
            horas_extras = float(horas_extras_str)
            hijos = int(hijos_str)
            
            if horas_normales < 0 or pago_hora < 0 or horas_extras < 0 or hijos < 0:
                raise ValueError("Los valores deben ser positivos")
            pago_normal = horas_normales * pago_hora
            pago_extra_hora = pago_hora * 1.5
            pago_extras = horas_extras * pago_extra_hora
            bonificacion = hijos * 0.50
            pago_total = pago_normal + pago_extras + bonificacion
            
            self.trabajadores.append({
                'nombre': nombre,
                'horas_normales': horas_normales,
                'pago_hora': pago_hora,
                'pago_normal': pago_normal,
                'horas_extras': horas_extras,
                'pago_extra_hora': pago_extra_hora,
                'pago_extras': pago_extras,
                'hijos': hijos,
                'bonificacion': bonificacion,
                'pago_total': pago_total
            })
            
            self.mostrar_reporte()
            self.entrada_nombre.delete(0, tk.END)
            self.entrada_horas_normales.delete(0, tk.END)
            self.entrada_pago_hora.delete(0, tk.END)
            self.entrada_horas_extras.delete(0, tk.END)
            self.entrada_hijos.delete(0, tk.END)
            self.entrada_nombre.focus()
            
        except ValueError as e:
            messagebox.showerror("Error", "Ingresa valores válidos")
    
    def mostrar_reporte(self):
        self.texto_resultado.delete(1.0, tk.END)
        texto = "=== REPORTE DE PAGOS ===\n\n"
        total_general = 0
        
        for i, trabajador in enumerate(self.trabajadores, 1):
            texto += f"{i}. {trabajador['nombre']}\n"
            texto += f"   Horas Normales: {trabajador['horas_normales']:.2f} × S/. {trabajador['pago_hora']:.2f} = S/. {trabajador['pago_normal']:.2f}\n"
            texto += f"   Horas Extras: {trabajador['horas_extras']:.2f} × S/. {trabajador['pago_extra_hora']:.2f} = S/. {trabajador['pago_extras']:.2f}\n"
            texto += f"   Bonificación ({trabajador['hijos']} hijo(s)): S/. {trabajador['bonificacion']:.2f}\n"
            texto += f"   PAGO TOTAL: S/. {trabajador['pago_total']:.2f}\n"
            texto += "-" * 60 + "\n\n"
            total_general += trabajador['pago_total']
        
        texto += f"\nTOTAL A PAGAR A TODOS LOS TRABAJADORES: S/. {total_general:.2f}"
        self.texto_resultado.insert(tk.END, texto)
    
    def limpiar(self):
        self.trabajadores = []
        self.texto_resultado.delete(1.0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_horas_normales.delete(0, tk.END)
        self.entrada_pago_hora.delete(0, tk.END)
        self.entrada_horas_extras.delete(0, tk.END)
        self.entrada_hijos.delete(0, tk.END)
        self.entrada_nombre.focus()


