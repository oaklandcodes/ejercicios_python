import sys

# Escribe un programa que divide los dos parámetros a y b 
# y luego le aplique un módulo de c

def div_mod(a, b, c):
    div_num_mod= a / b % c
    return div_num_mod
   
    
def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    if b == 0:
        print("Error: División por cero no permitida.")
        sys.exit(1)
    if c == 0:
        print("Error: Módulo por cero no permitido.")
        sys.exit(1)
    
    result = div_mod(a, b, c)
    print(f"El resultado de ({a} / {b}) % {c} es: {result}")
 

if __name__ == "__main__":
    main()