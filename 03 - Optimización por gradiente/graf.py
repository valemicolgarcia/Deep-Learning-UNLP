import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
B = 1  # Ancho del triángulo
T = 2  # Período de la señal

# Valores de k
k = np.arange(-20, 21)  # Valores de k desde -20 hasta 20 (incluye frecuencias negativas y positivas)

# Cálculo de los coeficientes de Fourier (módulo)
c_k = (B / T) * (np.sinc(k * B / T))**2

# Graficar el espectro de amplitud
plt.figure(figsize=(10, 6))
plt.stem(k, c_k, basefmt=" ", use_line_collection=True, linefmt='b-', markerfmt='bo')
plt.xlabel('k (Índice de la frecuencia armónica)')
plt.ylabel(r'$|c_k|$ (Amplitud de los coeficientes de Fourier)')
plt.title('Espectro de Amplitud de la Señal $x(t)$')
plt.grid(True)
plt.show()
