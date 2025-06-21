# Escribe un programa que ordene un array de int en orden ascendente.
import sys

def sort_tab(arr):
    arr.sort()
    return arr

def main():
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar al menos un número entero como argumento.")
        sys.exit(1)

    try:
        new_arr = [int(x) for x in sys.argv[1:]]
    except ValueError:
        print("Error: Todos los argumentos deben ser números enteros.")
        sys.exit(1)

    order_list = sort_tab(new_arr)
    print("Order list:", order_list)

if __name__ == "__main__":
    main()
