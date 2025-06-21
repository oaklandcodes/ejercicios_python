"""
Escribe un programa que intercambie el contenido y las direcciones de memoria de dos enteros
"""
def swap_int(a, b):
    # Intercambia los valores de a y b
    temp = a
    a = b
    b = temp
    return a, b

def main():
    a = 20
    b = 15
    new_a, new_b = swap_int(a, b)
    print(f"final_swap: a = {new_a}, b = {new_b}")
    
if __name__ == "__main__":
    main()