import sys
# Escribe un programa que muestre, “N” o “P” en función del signo del entero que se haya usado como parámetro.
# Si n es negativo muestra “N”. Si n es positivo o nulo muestra “P”

def is_negative(n):
        if (n > 0):
            print("P")
        else:
            print("N")
def main():
    if len(sys.argv) != 2:
        print("Error: Debes proporcionar un número como argumento.")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: El argumento debe ser un número entero.")
        sys.exit(1)
    is_negative(n)
    
if __name__ == "__main__":
    main()