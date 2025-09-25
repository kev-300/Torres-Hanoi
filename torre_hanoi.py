def torres_de_hanoi(n, origen, destino, auxiliar, contador, movimientos):#creamos una funcion para los movimientos
    if n == 1:
        contador[0] += 1#permite contar los movimientos
        print(f"{contador[0]}. Mover disco 1 de {origen} a {destino}")#imprime el movimiento del primer disco
        movimientos.append((1, origen, destino))#almacena los movimientos
        return
    torres_de_hanoi(n - 1, origen, auxiliar, destino, contador, movimientos)
    contador[0] += 1
    print(f"{contador[0]}. Mover disco {n} de {origen} a {destino}")#imprime el movimiento del disco n
    movimientos.append((n, origen, destino))
    torres_de_hanoi(n - 1, auxiliar, destino, origen, contador, movimientos)

def main():
    try:
        n = int(input("Ingrese el número de discos (1 a 20): "))
        if not (1 <= n <= 20):#agregaremos un limite de numeros ya que son los requisitos
            print("Por favor ingrese un número entre 1 y 20.")
            return
    except ValueError:#demostracion de errores
        print("Entrada inválida. Por favor ingrese un número entero.")
        return

    print("\n Personalización de nombres de torres  ")#un requisito es que el usuario pueda agregar el nombre a las torres
    origen = input("Nombre de la torre de origen (por defecto A): ") or "A"
    auxiliar = input("Nombre de la torre auxiliar (por defecto B): ") or "B"
    destino = input("Nombre de la torre de destino (por defecto C): ") or "C"

    print(f"\nResolviendo Torre de Hanoi para {n} discos...\n")

    contador = [0] 
    movimientos = []

    torres_de_hanoi(n, origen, destino, auxiliar, contador, movimientos)

    total = 2 ** n - 1
    print(f"\nTotal de movimientos esperados: {total}")#demostramos el numero total de movimientos

if __name__ == "__main__":#ejecutamos el archivo
    main()
