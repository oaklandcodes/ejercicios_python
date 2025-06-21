import sys 

def print_str(string):
    for i in string:
        print(i)
        
        
def main():
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar una cadena de texto como argumento.")
        sys.exit(1)
    string = sys.argv[1]
    print_str(string)
 
if __name__ == "__main__":
    main()

