import sys

#Escribe un programa que muestre, todas las combinaciones posibles 
# de dos números (XX XX) entre 0 y 99, en orden creciente.

def print_comb2():
    for i in range(0, 99):
        for j in range(1, 100):
            if i == 98 and j == 99:
                print(f"{i:02d} {j:02d}", end="")
            else:
                print(f"{i:02d} {j:02d}, ", end=" ")
          
                   
def main():
   print_comb2() 
    
if __name__ == "__main__":
    main()