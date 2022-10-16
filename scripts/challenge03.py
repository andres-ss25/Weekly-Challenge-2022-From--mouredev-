
'''
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''


from ast import Num, Return


def es_primo(number):
    '''
    This function detect if a number is a primo number
    '''

    if number <2:
        return False

    for i in range(2,number):
        if (number%i==0):
            return False
    
    return True



if __name__=="__main__":
    
    for i in range(1,100):
        if es_primo(i):
            print(i, "Es primo")