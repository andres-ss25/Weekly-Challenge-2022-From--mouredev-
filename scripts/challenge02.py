'''
 Reto #2
 * LA SUCESIÓN DE FIBONACCI
 * Fecha publicación enunciado: 10/01/22
 * Fecha publicación resolución: 17/01/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
   
   f_n = f_n-1 + f_n-2

'''

def fibonacci(cant_numeros):
    fibonacci_n_menos_1=1
    fibonacci_n_menos_2=0

    for i in range(cant_numeros):

        print(i, fibonacci_n_menos_2)

        fibonacci_n = fibonacci_n_menos_1+fibonacci_n_menos_2

        fibonacci_n_menos_2 =fibonacci_n_menos_1
        fibonacci_n_menos_1 = fibonacci_n



if __name__=="__main__":
    fibonacci(51)