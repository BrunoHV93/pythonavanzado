#Programa que define si un número es primo o no. Se implementa tipado estático

def is_prime(numero : int) -> str:
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        resp = 'Es primo'
    else:
        resp = 'No es primo'

    return resp

def run():
    numero = 2
    print(is_prime(numero))



if __name__ == '__main__':
    run()