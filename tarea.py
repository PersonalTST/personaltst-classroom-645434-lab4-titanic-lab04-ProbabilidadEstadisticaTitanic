
import pandas as pd

def cargar_datos():
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    df = pd.read_csv(url)
    return df

def calcular_probabilidad_total(df, columna, valor):
    """ Calcula la probabilidad de un valor específico en una columna. """
    raise NotImplementedError()

def calcular_probabilidad_condicional(df, condicion_col, condicion_valor, target_col, target_valor):
    """ Calcula P(target=valor | condicion=valor). """
    raise NotImplementedError()

def calcular_medidas_tendencia_central(df, columna):
    """ Devuelve un diccionario con media, mediana y moda. """
    return {
        "media": None,
        "mediana": None,
        "moda": None
    }

def calcular_medidas_dispersion(df, columna):
    """ Devuelve un diccionario con varianza y desviación estándar. """
    return {
        "varianza": df[columna].var(ddof=0),
        "desviacion_estandar": df[columna].std()
    }

def distribucion_por_categoria(df, columna):
    """ Devuelve un DataFrame con la distribución de valores en una columna, (Columna 1 Pclass y Columna 2 proporcion)"""
    raise NotImplementedError()