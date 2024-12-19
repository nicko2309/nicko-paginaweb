import customtkinter as ctk
from tkinter import filedialog, messagebox
from pln import normalizar_texto, analizar_sentimientos
from rv import preprocesar_imagen, detectar_rostros

def iniciar_aplicacion():
    # Configuración de la ventana principal
    app = ctk.CTk()
    app.title("Proyecto PLN y RV")
    app.geometry("800x600")

    # Entrada para texto
    texto_entrada = ctk.CTkTextbox(app, width=600, height=100)
    texto_entrada.pack(pady=10)

    def procesar_pln():
        texto = texto_entrada.get("1.0", "end").strip()
        if not texto:
            messagebox.showerror("Error", "Por favor, ingresa un texto.")
            return
        
        # Llamar funciones de PLN
        texto_normalizado = normalizar_texto(texto)
        sentimiento = analizar_sentimientos(texto)
        
        # Mostrar resultados
        messagebox.showinfo("Resultados PLN", f"Texto normalizado: {texto_normalizado}\nSentimiento: {sentimiento}")

    # Botón para procesar texto
    boton_pln = ctk.CTkButton(app, text="Procesar PLN", command=procesar_pln)
    boton_pln.pack(pady=10)

    def cargar_imagen():
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.jpeg")])
        if not ruta:
            return
        
        # Procesar imagen
        _, rostros_detectados = detectar_rostros(ruta)
        messagebox.showinfo("Resultados RV", f"Rostros detectados: {rostros_detectados}")

    # Botón para cargar imagen
    boton_rv = ctk.CTkButton(app, text="Cargar Imagen y Procesar", command=cargar_imagen)
    boton_rv.pack(pady=10)

    app.mainloop()
