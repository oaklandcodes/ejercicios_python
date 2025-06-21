import sys 

#Escribe un programa que muestre,en una sola línea
# y en orden creciente, todos los dígitos.

def print_numbers():
    for i in range (0,10):
        print(i, end = "")

def main():
    print_numbers()
    
if __name__ == "__main__":
    main()