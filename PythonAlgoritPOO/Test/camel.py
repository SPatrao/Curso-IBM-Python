###Camel Case###
import re

def capitalize(word):
    """Convierte la palabra para que tenga la primera letra en mayúscula, el resto en minúsculas."""
    return word[0:1].upper() + word[1:].lower()

def lowercase(word):
    """Convierte una palabra a minúsculas."""
    return word.lower()

def camel_case(sentence):
    # Elimina espacios múltiples y espacios alrededor
    remove_multiple_spaces = re.sub(r'\s+', '', sentence)
    remove_surrounding_space = remove_multiple_spaces.strip()
    
    words = remove_surrounding_space.split(' ')
    first_word = lowercase(words[0])  # Pasa la primera palabra a minúsculas
    capitalized_words = [capitalize(word) for word in words[1:]]  # Capitaliza las demás palabras
    
    camel_cased_words = [first_word] + capitalized_words
    camel_cased_sentence = ''.join(camel_cased_words)
    
    return camel_cased_sentence

def main():
    sentence = input('Introduzca la frase:')
    camelcased = camel_case(sentence)
    print(camelcased)