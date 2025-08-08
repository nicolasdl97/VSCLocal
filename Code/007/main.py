from modulo import sumar

def main():
    # Solicita al usuario ingresar dos números
    num1 = 5
    num2 =3
    
    # Llama a la función sumar y muestra el resultado
    resultado = sumar(num1, num2)
    print("La suma es:", resultado)

if __name__ == "__main__":
    main()