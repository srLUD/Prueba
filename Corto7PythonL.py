import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#XD
archivo = 'c:\Users\ludwi\OneDrive\Visual Studio\Python\Corto7\Corto7.xlsx'  
hoja = 'Registro Temperatura'
df = pd.read_excel(archivo, sheet_name=hoja)

tiempo = df.iloc[:, 0].values
temperatura = df.iloc[:, 1].values

coef_pol = np.polyfit(tiempo, temperatura, 4)
polinomio_grado_4 = np.poly1d(coef_pol)

def func_exponencial(t, a, b, c):
    return a * np.exp(-b * t) + c

parametros_iniciales = [1, 1e-6, 1]  
coef_exp, _ = curve_fit(func_exponencial, tiempo, temperatura, p0=parametros_iniciales)

plt.figure(figsize=(10, 6))

plt.scatter(tiempo, temperatura, color='blue', label='Datos originales')

plt.plot(tiempo, polinomio_grado_4(tiempo), color='red', label='Ajuste Polinomial Grado 4')

plt.plot(tiempo, func_exponencial(tiempo, *coef_exp), color='green', label='Ajuste Exponencial')

plt.title('Ajuste de Datos de Enfriamiento')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura')
plt.legend()
plt.grid(True)
plt.show()

print("Coeficientes del polinomio de grado 4:", coef_pol)
print("Coeficientes del ajuste exponencial:", coef_exp)






























