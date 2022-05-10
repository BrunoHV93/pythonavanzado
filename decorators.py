# Averigua cuánto tarda un programa en ejecutarse

# Importamos módulos de fechas
from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        # El método now regresa fecha y hora en el momento en que es llamado
        initial_time = datetime.now()
        func(*args, **kwargs   )
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        # Total seconds permite obtener los segundos
        print(f'Pasaron  {time_elapse.total_seconds()}  segundos')
    return wrapper

@execution_time
def random_func():
    # Cuando tenemos ciclo for pero no nos interesan los valors recorridos se pone _ 
    # por convenio en la industria
    for _ in range (1, 10000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

#random_func()
suma(5,5)