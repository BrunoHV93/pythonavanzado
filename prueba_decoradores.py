#This is a decorator test

# Definition of the decorator
def mayusculas(func):
    # Wrapper
    def envoltura(texto):
        # Execution of the function wrapped
        return func(texto).upper()
    return envoltura

# This is how we tell Python we want to decorate a function
@mayusculas
def mensajes(nombre):
    return f'{nombre}, recibiste un mensaje'

def run():
    print(mensajes('Cesar'))

if __name__ == '__main__':
    run()
    