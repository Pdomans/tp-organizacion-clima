
from cargar_datos import cargar_dataset

df = cargar_dataset()

print("ESTADISTICAS GENERALES")
print(df.describe())

print("\nMES MAS CALIENTE")
print(df.loc[df['Mean'].idxmax()])

print("\nMES MAS FRIO")
print(df.loc[df['Mean'].idxmin()])
