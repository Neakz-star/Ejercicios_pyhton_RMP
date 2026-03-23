import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio2:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 2: Sistema de Pago en Parque")
        self.ventana.geometry("700x600")
        self.ventana.configure(bg="#f0f0f0")
        self.visitantes = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 2"""
        # Título
        titulo = tk.Label(self.ventana, text="SISTEMA DE PAGO EN PARQUE",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=10)
        
        # Frame entrada
        frame_entrada = ttk.LabelFrame(self.ventana, text="Registro de Visitante")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_nombre = tk.Entry(frame_entrada, width=30)
        self.entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Edad:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_edad = tk.Entry(frame_entrada, width=30)
        self.entrada_edad.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Cantidad de Juegos:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_juegos = tk.Entry(frame_entrada, width=30)
        self.entrada_juegos.grid(row=2, column=1, padx=5, pady=5)
        
        # Botón agregar
        btn_agregar = tk.Button(frame_entrada, text="Registrar Visitante",
                               command=self.registrar_visitante,
                               bg="#4CAF50", fg="white")
        btn_agregar.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        
        # Frame resultados
        frame_resultados = ttk.LabelFrame(self.ventana, text="Registro de Visitantes")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=12, width=80)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Frame total
        frame_total = tk.Frame(self.ventana, bg="#e8f5e9")
        frame_total.pack(padx=20, pady=5, fill=tk.X)
        
        tk.Label(frame_total, text="Costo por juego: S/. 50", bg="#e8f5e9").pack(side=tk.LEFT, padx=5)
        self.label_total = tk.Label(frame_total, text="Total Recaudado: S/. 0.00",
                                    font=("Arial", 12, "bold"), bg="#e8f5e9")
        self.label_total.pack(side=tk.RIGHT, padx=5)
        
        # Frame info
        frame_info = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_info.pack(padx=20, pady=5, fill=tk.X)
        
        tk.Label(frame_info, text="Descuentos: <10 años (25%), 10-17 años (10%), Adultos (0%)",
                font=("Arial", 9), bg="#f0f0f0").pack()
        
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
    
    def calcular_pago(self, edad, juegos):
        """Calcula el pago con descuento según edad"""
        costo_unitario = 50
        total_sin_descuento = juegos * costo_unitario
        
        if edad < 10:
            descuento = 0.25
        elif edad <= 17:
            descuento = 0.10
        else:
            descuento = 0.0
        
        descuento_monto = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - descuento_monto
        
        return total_sin_descuento, descuento, descuento_monto, total_a_pagar
    
    def registrar_visitante(self):
        nombre = self.entrada_nombre.get().strip()
        edad_str = self.entrada_edad.get().strip()
        juegos_str = self.entrada_juegos.get().strip()
        
        if not nombre or not edad_str or not juegos_str:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            edad = int(edad_str)
            juegos = int(juegos_str)
            
            if edad < 0 or juegos < 0:
                raise ValueError("Los valores deben ser positivos")
            
            subtotal, descuento, monto_desc, total = self.calcular_pago(edad, juegos)
            
            self.visitantes.append({
                'nombre': nombre,
                'edad': edad,
                'juegos': juegos,
                'subtotal': subtotal,
                'descuento_pct': descuento * 100,
                'descuento_monto': monto_desc,
                'total': total
            })
            
            self.mostrar_visitantes()
            self.entrada_nombre.delete(0, tk.END)
            self.entrada_edad.delete(0, tk.END)
            self.entrada_juegos.delete(0, tk.END)
            self.entrada_nombre.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos")
    
    def mostrar_visitantes(self):
        self.texto_resultado.delete(1.0, tk.END)
        texto = "=== REGISTRO DE VISITANTES ===\n\n"
        total_recaudado = 0
        
        for i, visitante in enumerate(self.visitantes, 1):
            texto += f"{i}. {visitante['nombre']} ({visitante['edad']} años)\n"
            texto += f"   Juegos: {visitante['juegos']} × S/. 50 = S/. {visitante['subtotal']:.2f}\n"
            texto += f"   Descuento ({visitante['descuento_pct']:.0f}%): -S/. {visitante['descuento_monto']:.2f}\n"
            texto += f"   Total a Pagar: S/. {visitante['total']:.2f}\n"
            texto += "-" * 50 + "\n\n"
            total_recaudado += visitante['total']
        
        self.texto_resultado.insert(tk.END, texto)
        self.label_total.config(text=f"Total Recaudado: S/. {total_recaudado:.2f}")
    
    def limpiar(self):
        self.visitantes = []
        self.texto_resultado.delete(1.0, tk.END)
        self.label_total.config(text="Total Recaudado: S/. 0.00")
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_edad.delete(0, tk.END)
        self.entrada_juegos.delete(0, tk.END)
