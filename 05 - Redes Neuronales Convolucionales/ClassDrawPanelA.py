import tkinter as tk
from PIL import Image, ImageOps, ImageGrab
import numpy as np
from keras.models import load_model
import time

class DrawPanel(tk.Tk):
    def __init__(self, width=200, height=200, line_width=3):
        super().__init__()

        self.width = width
        self.height = height
        self.line_width = line_width
        self.old_x = None
        self.old_y = None

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        self.button = tk.Button(self, text="Finalizar Dibujo", command=self.save_image)
        self.button.pack()

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.image = Image.new("RGB", (self.width, self.height), "white")
        self.draw = ImageOps.grayscale(self.image)

    def paint(self, event):
        paint_color = 'black'
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.line_width, fill=paint_color, capstyle=tk.ROUND, smooth=True)
            # Dibuja en el objeto PIL Image para guardar más tarde
            self.draw.line([self.old_x, self.old_y, event.x, event.y], fill=0, width=self.line_width)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def save_image(self):
        # Capturar el canvas como imagen
        self.update()  # Actualizar la ventana antes de capturar
        x = self.winfo_rootx() + self.canvas.winfo_x()
        y = self.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        
        # Guardar la imagen capturada
        image = ImageGrab.grab().crop((x, y, x1, y1)).convert("L").resize((28, 28))
        image.show()

        # Normalizar la imagen para el modelo
        image_array = np.array(image).reshape(1, 28, 28, 1) / 255.0

        # Cargar el modelo y predecir el dígito
        model = load_model('ruta_al_modelo.h5')
        prediccion = model.predict(image_array)
        digito = np.argmax(prediccion)
        
        print(f"El dígito dibujado corresponde al número: {digito}")
        return digito


# Ejecutar la aplicación
if __name__ == "__main__":
    app = DrawPanel(width=200, height=200, line_width=5)
    app.mainloop()
