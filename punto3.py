opcion = 1
i = 1
numeros = []
print('Digitar 1 para recibir 5 números enteros')
print('Digitar 2 para calcular la suma de los números')
print('Digitar 3 para ingresar un número adicional')
print('Digitar 4 para salir')

while (opcion != 0):
    opcion = int(input('Digite una opción: '))
    if(opcion == 1):
        while i <= 5:
            numero = int(input('Digite un número: '))
            i += 1
            numeros.append(numero)
    elif(opcion == 2):
        suma = sum(numeros)
        print(f'La suma los números es: {suma}')
    elif(opcion == 3):
        numadicional = int(input('Digite un número adicional entero: '))
        numeros.append(numadicional)
    elif(opcion == 4):
        print('Has salido del menú')
        break
else:
    print('Has salido del menú')