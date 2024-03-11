"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    #
    # Inserte su código aquí
    #
  
    # Tratar datos faltantes
    df.dropna(inplace=True)

    # Convertir todas las columnas a cadenas (str)
    df = df.apply(lambda x: x.astype(str))

    # Reemplazar símbolos de dólar ($) por cadena vacía ("")
    df = df.apply(lambda x: x.str.replace("$", ""))

    # Reemplazar comas (,) por cadena vacía ("")
    df = df.apply(lambda x: x.str.replace(",", ""))

    # Reemplazar guiones bajos (_) por guiones (-)
    df = df.apply(lambda x: x.str.replace("_", "-"))

    # Reemplazar guiones (-) por espacios
    df = df.apply(lambda x: x.str.replace("-", " "))

    # Convertir todas las cadenas a minúsculas
    df = df.apply(lambda x: x.str.lower())

    # # Eliminar los espacios en blanco al principio y al final de cada cadena
    # df = df.apply(lambda x: x.str.strip())  # no da para la variable barrio 

    # Convierte el monto del crédito a float
    df.monto_del_credito = df.monto_del_credito.astype(float)

    #Convierte la columna fecha de beneficio a fecha donde el primer elemento es el día, formato AAAA-MM-DD
    df.fecha_de_beneficio = pd.to_datetime(df["fecha_de_beneficio"], dayfirst = True, format='mixed')
    
    # Eliminar duplicados
    df.drop_duplicates(inplace=True)
    
    return df

# # Llamar a la función clean_data() para obtener el DataFrame limpio
# df_cleaned = clean_data()

# # Imprimir el DataFrame limpio
# print(df_cleaned)



