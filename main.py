import tkinter as tk
from ejercicio1 import AbrirEjercicio1
from ejercicio2 import AbrirEjercicio2
from ejercicio3 import AbrirEjercicio3
from ejercicio4 import AbrirEjercicio4
from ejercicio5 import AbrirEjercicio5
from ejercicio6 import AbrirEjercicio6
from ejercicio7 import AbrirEjercicio7
from ejercicio8 import AbrirEjercicio8
from ejercicio9 import AbrirEjercicio9
from ejercicio10 import AbrirEjercicio10


class MenuPrincipal:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Ejercicios de Programación - Interfaz Gráfica")
        self.ventana_principal.geometry("600x700")
        self.ventana_principal.configure(bg="#f0f0f0")
        
        self.mostrar_menu()
    
    def mostrar_menu(self):
        """Muestra el menú principal con 10 botones"""
        for widget in self.ventana_principal.winfo_children():
            widget.destroy()
        titulo = tk.Label(self.ventana_principal, text="MENÚ PRINCIPAL", 
                         font=("Arial", 18, "bold"), bg="#f0f0f0")
        titulo.pack(pady=20)
        
        subtitulo = tk.Label(self.ventana_principal, 
                            text="Selecciona un ejercicio para ejecutar",
                            font=("Arial", 12), bg="#f0f0f0")
        subtitulo.pack(pady=10)
        frame_botones = tk.Frame(self.ventana_principal, bg="#f0f0f0")
        frame_botones.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        ejercicios = [
            ("1. Sistema de Aumento de Sueldos", AbrirEjercicio1),
            ("2. Sistema de Pago en Parque", AbrirEjercicio2),
            ("3. Sistema de Descuentos por Mes", AbrirEjercicio3),
            ("4. Validación de Número < 10", AbrirEjercicio4),
            ("5. Validación de Número en Rango", AbrirEjercicio5),
            ("6. Registro de Intentos", AbrirEjercicio6),
            ("7. Suma de Números Enteros", AbrirEjercicio7),
            ("8. Sistema de Suma Acumulativa", AbrirEjercicio8),
            ("9. Suma hasta Superar Límite", AbrirEjercicio9),
            ("10. Sistema de Pago de Trabajadores", AbrirEjercicio10),
        ]
        
        for texto, clase_ejercicio in ejercicios:
            btn = tk.Button(frame_botones, text=texto, 
                           command=lambda c=clase_ejercicio: self.abrir_ejercicio(c),
                           width=40, height=2, font=("Arial", 10),
                           bg="#4CAF50", fg="white", relief=tk.RAISED,
                           cursor="hand2")
            btn.pack(pady=8, fill=tk.X)
        btn_salida = tk.Button(self.ventana_principal, text="Salir",
                              command=self.ventana_principal.quit,
                              width=40, height=2, font=("Arial", 10),
                              bg="#f44336", fg="white", relief=tk.RAISED)
        btn_salida.pack(pady=20)
    
    def abrir_ejercicio(self, clase_ejercicio):
        """Abre un ejercicio en una ventana nueva"""
        ventana = tk.Toplevel(self.ventana_principal)
        clase_ejercicio(ventana)
    
    def volver_al_menu(self):
        """Vuelve a mostrar el menú principal"""
        self.mostrar_menu()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = MenuPrincipal(ventana)
    ventana.mainloop()


