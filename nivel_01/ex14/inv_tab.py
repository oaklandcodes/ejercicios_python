import sys

def inv_int_tab(tab):
    """Invierte un array de enteros.
    :param tab: Lista de enteros a invertir.
    """
    inv_new_list = []
    i = len(tab) - 1
    while i >= 0:
        inv_new_list.append(tab[i]) 
        i -= 1
    return inv_new_list

def main():
    if len(sys.argv) < 2:
        print("Uso: python inv_tab.py <lista_de_enteros>")
        sys.exit(1)

    try:
        tab = [int(x) for x in sys.argv[1:]]
    except ValueError:
        print("Todos los argumentos deben ser enteros.")
        sys.exit(1)

    inv_tab = inv_int_tab(tab)
    print(f"Array original: {tab}")
    print(f"Array invertido: {inv_tab}")
    
if __name__ == "__main__":
    main()