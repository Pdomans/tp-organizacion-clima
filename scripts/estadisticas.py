
# importar libreria pandas
import pandas as pd

# cargar dataset climático
df = pd.read_csv('datos/monthly.csv')

# mostrar estadísticas generales
print("ESTADISTICAS GENERALES")
print(df.describe())

# buscar mes más caliente
print("\nMES MAS CALIENTE")
print(df.loc[df['Mean'].idxmax()])

# buscar mes más frío
print("\nMES MAS FRIO")
print(df.loc[df['Mean'].idxmin()])
