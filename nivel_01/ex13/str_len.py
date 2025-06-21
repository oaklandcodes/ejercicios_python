"""
Escribe un programa que cuente el número de caracteres de un string 
y que devuelva el número encontrado.
"""
import sys
def str_len(string):
    i = 0
    for _ in string:
        i += 1
    print(f"El número de caracteres en el string es: {i}")
        
        
def main():
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar un string como argumento.")
        sys.exit(1)
    string = sys.argv[1]
    str_len(string)
 
if __name__ == "__main__":
    main()
    
