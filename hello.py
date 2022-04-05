#!/usr/bin/python
import sys

def main():
    if len(sys.argv) != 2:
        print('Error: solo puedes colocar un argumento')
    else:
        try:
            print(f'hola, {sys.argv[1]}')
        except IndexError:
            print('Error: debes colocar tu nombre como un argumento')

if __name__ == "__main__":
    main()