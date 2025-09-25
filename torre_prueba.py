def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    torres_de_hanoi(n - 1, auxiliar, destino, origen)


n= int(input("ingrese el numero de discos: "))
torres_de_hanoi(n, 'A', 'C', 'B')
