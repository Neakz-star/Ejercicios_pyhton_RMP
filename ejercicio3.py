import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext


class AbrirEjercicio3:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 3: Sistema de Descuentos por Mes")
        self.ventana.geometry("700x600")
        self.ventana.configure(bg="#f0f0f0")
        self.compras = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz del ejercicio 3"""
        titulo = tk.Label(self.ventana, text="SISTEMA DE DESCUENTOS POR MES",
                         font=("Arial", 14, "bold"), bg="#f0f0f0")
        titulo.pack(pady=10)
        frame_entrada = ttk.LabelFrame(self.ventana, text="Registro de Compra")
        frame_entrada.pack(padx=20, pady=10, fill=tk.X)
        
        tk.Label(frame_entrada, text="Nombre del Cliente:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_cliente = tk.Entry(frame_entrada, width=30)
        self.entrada_cliente.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Mes (1-12):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_mes = tk.Entry(frame_entrada, width=30)
        self.entrada_mes.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_entrada, text="Importe de Compra:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entrada_importe = tk.Entry(frame_entrada, width=30)
        self.entrada_importe.grid(row=2, column=1, padx=5, pady=5)
        btn_agregar = tk.Button(frame_entrada, text="Registrar Compra",
                               command=self.registrar_compra,
                               bg="#4CAF50", fg="white")
        btn_agregar.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.EW, padx=5)
        frame_resultados = ttk.LabelFrame(self.ventana, text="Historial de Compras")
        frame_resultados.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, height=12, width=80)
        self.texto_resultado.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        frame_total = tk.Frame(self.ventana, bg="#e8f5e9")
        frame_total.pack(padx=20, pady=5, fill=tk.X)
        
        self.label_total = tk.Label(frame_total, text="Total Vendido: S/. 0.00",
                                    font=("Arial", 12, "bold"), bg="#e8f5e9")
        self.label_total.pack(pady=5)
        frame_info = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_info.pack(padx=20, pady=5, fill=tk.X)
        
        tk.Label(frame_info, text="Promociones: Octubre (15%), Diciembre (20%), Julio (10%), Otros (0%)",
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
    
    def calcular_descuento(self, mes):
        """Calcula el descuento según el mes"""
        if mes == 10:
            return 0.15
        elif mes == 12:
            return 0.20
        elif mes == 7:
            return 0.10
        else:
            return 0.0
    
    def registrar_compra(self):
        cliente = self.entrada_cliente.get().strip()
        mes_str = self.entrada_mes.get().strip()
        importe_str = self.entrada_importe.get().strip()
        
        if not cliente or not mes_str or not importe_str:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        try:
            mes = int(mes_str)
            importe = float(importe_str)
            
            if mes < 1 or mes > 12:
                raise ValueError("El mes debe estar entre 1 y 12")
            if importe < 0:
                raise ValueError("El importe debe ser positivo")
            
            descuento_pct = self.calcular_descuento(mes)
            descuento_monto = importe * descuento_pct
            total_final = importe - descuento_monto
            
            meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            
            self.compras.append({
                'cliente': cliente,
                'mes': mes,
                'mes_nombre': meses[mes],
                'importe': importe,
                'descuento_pct': descuento_pct * 100,
                'descuento_monto': descuento_monto,
                'total': total_final
            })
            
            self.mostrar_compras()
            self.entrada_cliente.delete(0, tk.END)
            self.entrada_mes.delete(0, tk.END)
            self.entrada_importe.delete(0, tk.END)
            self.entrada_cliente.focus()
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def mostrar_compras(self):
        self.texto_resultado.delete(1.0, tk.END)
        texto = "=== REGISTRO DE COMPRAS ===\n\n"
        total_vendido = 0
        
        for i, compra in enumerate(self.compras, 1):
            texto += f"{i}. {compra['cliente']} - {compra['mes_nombre']}\n"
            texto += f"   Importe: S/. {compra['importe']:.2f}\n"
            texto += f"   Descuento ({compra['descuento_pct']:.0f}%): -S/. {compra['descuento_monto']:.2f}\n"
            texto += f"   Total Final: S/. {compra['total']:.2f}\n"
            texto += "-" * 50 + "\n\n"
            total_vendido += compra['total']
        
        self.texto_resultado.insert(tk.END, texto)
        self.label_total.config(text=f"Total Vendido: S/. {total_vendido:.2f}")
    
    def limpiar(self):
        self.compras = []
        self.texto_resultado.delete(1.0, tk.END)
        self.label_total.config(text="Total Vendido: S/. 0.00")
        self.entrada_cliente.delete(0, tk.END)
        self.entrada_mes.delete(0, tk.END)
        self.entrada_importe.delete(0, tk.END)


