import datetime

def dia_del_programador(year):
    # Creo una fecha para el día 256 del año dado
    fecha_programador = datetime.date(year, 1, 1) + datetime.timedelta(days=255)
    
    # Obtengo el día, el nombre del mes, el año y el nombre del día de la semana
    dia = fecha_programador.day
    nombre_mes = fecha_programador.strftime('%B')
    nombre_dia_semana = fecha_programador.strftime('%A')
    
    # Creo la lista con los elementos requeridos
    resultado = [dia, nombre_mes, year, nombre_dia_semana, 'celebrará']
    
    return resultado

# Ejemplo de uso:
year = 2023
resultado = dia_programador(year)
print(resultado)
