
from cargar_datos import cargar_dataset
import matplotlib.pyplot as plt

# cargar datos
df = cargar_dataset()

# obtener fila del maximo y minimo
maximo = df.loc[df['Mean'].idxmax()]
minimo = df.loc[df['Mean'].idxmin()]

# obtener posiciones
indice_max = df['Mean'].idxmax()
indice_min = df['Mean'].idxmin()

# crear grafico
plt.figure(figsize=(15,5))

# linea principal
plt.plot(df['Mean'])

# punto maximo
plt.scatter(indice_max, maximo['Mean'], label='Mes más caliente')

# punto minimo
plt.scatter(indice_min, minimo['Mean'], label='Mes más frío')

# titulos
plt.title('Evolución de anomalías de temperatura global')
plt.xlabel('Registro mensual')
plt.ylabel('Anomalía de temperatura')
