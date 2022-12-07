#Escribir una función que reciba una muestra de números en una lista y
#devuelva su media, varianza y desviación típica en un diccionario.
def mean(sample):
    return sum(sample)/len(sample)
    print(mean([1, 2, 3, 4, 5]))
    print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))