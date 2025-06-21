import sys 
# Escribe un programa que muestre un carácter usado como argumento.
def print_char(char):
    print(char)

def main():
    char = sys.argv[1]
    if len(char) != 1:
        print("Error: Debes proporcionar un único carácter.")
        sys.exit(1)
    pr int_char(char)
    
if __name__ == "__main__":
    main()
