
'''
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 '''



def es_anagrama(string1, string2):
    if string1!=string2:
        string1_sorted=sorted(string1.lower())
        string2_sorted=sorted(string2.lower())

        if string1_sorted==string2_sorted:
            return True
        else:
            return False
    else:
        print("No son anagramas")


if __name__=="__main__":
    string1="iman"
    string2="mani"
    print(es_anagrama(string1, string2))