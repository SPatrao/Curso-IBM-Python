###Recicle###
from collections import namedtuple

CrateData = namedtuple('CrateData', ['houses', 'crates'])

def max_recycling(crates):
    """Devuelve la casa con la mayor cantidad de reciclaje y la cantidad de cajas."""
    if crates is None or len(crates) == 0:
        raise ValueError('Se requiere una lista con al menos un elemento.')
    
    max_houses = []
    max_crates = crates[0]
    
    for crate in crates:
        if crate > max_crates:
            max_crates = crate
    
    for house, crates in zip(range(len(crates)), crates):
        if crates == max_crates:
            max_houses.append(house)
    
    return CrateData(max_houses, max_crates)

# Funciones similares para min_recycling y otras operaciones...

def main():
    print('Programa de camión de reciclaje')
    houses = positive_int_input('¿Cuántas casas?')
    crates = get_crate_quantities(houses)
    
    maximums = max_recycling(crates)
    minimums = min_recycling(crates)
    total = total_crates(crates)
    
    print(f'El número total de cajas en la calle es {total}')
    print(f'La máxima cantidad de cajas de cualquier casa es {maximums.crates}')
    print(f'La casa(s) con más reciclaje es {maximums.houses}')
    print(f'La mínima cantidad de cajas de cualquier casa es {minimums.crates}')
    print(f'La casa(s) con menos reciclaje es {minimums.houses}')