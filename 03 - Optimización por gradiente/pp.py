import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros
bits = "00001011001001"  # ASCII 'P' => 0000101, 'I' => 1001001
bps = 1200  # Bits por segundo
f_carrier = 1200  # Frecuencia de la portadora en Hz
Tb = 1 / bps  # Tiempo de bit
amplitude_0 = 0  # Amplitud para bit 0 en ASK
amplitude_1 = 5  # Amplitud para bit 1 en ASK

# Crear el vector de tiempo
t = np.linspace(0, len(bits) * Tb, 100000)  # Asumiendo una alta resolución para la gráfica

# Crear la señal ASK
signal = np.zeros_like(t)
for i, bit in enumerate(bits):
    start = i * Tb
    end = (i + 1) * Tb
    t_bit = t[(t >= start) & (t < end)]
    if bit == '1':
        signal[(t >= start) & (t < end)] = amplitude_1 * np.sin(2 * np.pi * f_carrier * t_bit)
    else:
        signal[(t >= start) & (t < end)] = amplitude_0 * np.sin(2 * np.pi * f_carrier * t_bit)

# Graficar la señal
plt.figure(figsize=(10, 4))
plt.plot(t, signal, label='ASK Signal')
plt.title('ASK Modulation for ASCII "PI"')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

