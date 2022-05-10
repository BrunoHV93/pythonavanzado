#Progrma para definir si una cadena de caracteres es un palíndromo

#Creamos la función que recibe el striny ponemos el tipo de dato que debe ser
#indicamos también el tipo de dato que será el resultado
def is_palindrome(string:str) -> bool:
    #Limpiamos los espacios bancos que pueda contener el string. También colocamos en minpusculas
    string = string.replace(" ", "").lower()
    print(string[::-1])
    return string == string[::-1]

def run():
    print(is_palindrome(1000))
    #print(is_palindrome("Anita lava la tina"))

if __name__ == '__main__':
    run()