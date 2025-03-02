###Binario a Decimal###
def decimal(binary_str):
    """ Convierte cadenas binarias a sus equivalentes decimales.
    Lanzar ValueError si binary_str contiene caracteres distintos de 0 y 1"""
    remove_0_and_1 = binary_str.replace('0', '').replace('1', '')
    if len(remove_0_and_1) > 0:
        raise ValueError('La cadena binaria de entrada solo puede contener 0 y 1')
    
    place = 1  # Posición inicial
    dec = 0    # Valor decimal inicial
    
    for bit in binary_str[::-1]:  # Itera desde el final de la cadena hasta el principio
        if bit == '1':  # Si el dígito es un 1, suma el valor posicional
            dec += place
        place *= 2  # Multiplica la posición por 2 para el siguiente valor de posición
    
    return dec