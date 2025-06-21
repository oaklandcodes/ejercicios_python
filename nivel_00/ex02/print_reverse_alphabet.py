import sys

# Escribe un programa que muestre el alfabeto en Mayúsculas en una sola línea,
# en orden decreciente, empezando en la letra “z”.

def print_reverse_alphabet():
    for i in range (90,64,-1):
         print(chr(i), end = " ")
        
def main():
    print_reverse_alphabet()

if __name__ == "__main__":
    main()
