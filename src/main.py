import numpy as np
import matplotlib.pyplot as plt
import random

membrana = {
    'area': 1.0,  # área de la membrana en m^2
    'densidad_membrana': 1000.0,  # densidad de la membrana en kg/m^3
    'lipidos': {
        'fosfatidilcolina': {
            'tipo_lipido': 'fosfatidilcolina',
            'coef_particion': 1.0,  # coeficiente de partición del soluto en el lípido
            'densidad': 1000.0,  # densidad del lípido en kg/m^3
            # ...otras propiedades del lípido...
        },
        # ...otro tipo de lípidos...
    },
    # ...otra información sobre la membrana... no le entiendo a esto xd
}

tiempo = 10 # segundos
paso_tiempo = 0.1 # segundos
concentracion_interna = 100 # mol/m^3
concentracion_externa = 50 # mol/m^3
densidad_celular = 1.05 # kg/m^3

def permeabilidad(posicion, membrana):
    # Calcula la permeabilidad para una posición específica en la membrana
    # y un componente de la membrana específico
    # Utiliza la información molecular de la membrana para determinar la permeabilidad

    # Obtener el tipo de lípido del componente de membrana
    tipo_lipido = membrana['lipidos']['fosfatidilcolina']['tipo_lipido']

    # Obtener el coeficiente de partición del soluto en el tipo de lípido
    coef_particion = membrana['lipidos'][tipo_lipido]['coef_particion']

    # Obtener la densidad de los lípidos en la posición de la membrana
    densidad_lipidos = membrana['lipidos'][tipo_lipido]['densidad'] * membrana['densidad_membrana']

    # Obtener el área de la membrana en la posición dada
    area_membrana = membrana['area']

    # Calcular la permeabilidad utilizando la ecuación de Krogh y la teoría de la bicapa lipídica
    perm = coef_particion * densidad_lipidos * area_membrana

    return perm

def simulacion_microgravedad(tiempo, paso_tiempo, permeabilidad, concentracion_interna, concentracion_externa, densidad_celular):
    # Definir variables
    num_pasos = int(tiempo / paso_tiempo)
    volumen_celular = 1 # Volumen inicial de la célula
    resultados = np.zeros(num_pasos)

    # Realizar la simulación
    for i in range(num_pasos):
        # Calcular la permeabilidad de la membrana
        perm = permeabilidad * densidad_celular

        # Calcular la difusión de los solutos
        difusion = perm * (concentracion_externa - concentracion_interna)

        # Actualizar la concentración de solutos dentro de la célula
        concentracion_interna += difusion * paso_tiempo / volumen_celular

        # Calcular los cambios en la densidad celular debido a la microgravedad
        densidad_celular += np.random.normal(0, 0.01)

        # Actualizar el volumen celular
        volumen_celular = densidad_celular / 1.05

        # Guardar los resultados
        resultados[i] = concentracion_interna

    return resultados

num_simulaciones = 10
permeabilidad = permeabilidad(0, membrana)
print(permeabilidad)
resultados = simulacion_microgravedad(tiempo, paso_tiempo, permeabilidad, concentracion_interna, concentracion_externa, densidad_celular)
plt.plot(resultados)
plt.title('Efectos de la microgravedad en la membrana celular')
plt.xlabel('Tiempo')
plt.ylabel('Concentración interna')
plt.show()