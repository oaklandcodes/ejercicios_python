import sys

# Escribe un programa que muestre, en orden creciente, 
# todas las combinaciones posibles de tres dígitos distintos 
# en orden creciente -sí, la repetición es voluntaria.

def print_comb():
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if i < j < k:
                    print(f"{i}{j}{k}", end=" ")
        

def main():
   print_comb() 
    
if __name__ == "__main__":
    main()