
# importar pandas
import pandas as pd

# funcion para cargar dataset
def cargar_dataset():
    
    # leer archivo csv
    df = pd.read_csv('datos/monthly.csv')
    
    return df
