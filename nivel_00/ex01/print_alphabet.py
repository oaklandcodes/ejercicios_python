import sys 

# Escribe un programa que muestre el alfabeto en minúsculas en una sola línea, en orden creciente, 
# empezando en la letra “a”.

def print_alphabet():
    for i in range(97,123):
        print(chr(i), end = " ")
    
def main():
    print_alphabet()

if __name__ == "__main__":
    main()


