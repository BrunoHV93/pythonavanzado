# This program calculates our Body Mass Index given height and weight.
# Using a decorator it tells us if our weight status (underweight, normal, overweight, obese)


def define_status(func):
    def wrapper(*args, **kwargs):

        # To catch the returned bmi valie from the ffunction
        bmi = func(*args, **kwargs)

        # Conditions to determine the status for a male
        if bmi <= 18.5:
            status = 'Underweight'
        elif bmi > 18.5 and bmi <= 24.9:
            status = 'Normal'
        elif bmi > 24.9 and bmi <= 29.9:
            status = 'Overweight'
        elif bmi > 29.9 and bmi <= 34.9:
            status = 'Obese'
        elif bmi > 29.9 and bmi <= 34.9:
            status = 'Extremly obese'

        # Printing the status
        print(f'Weight status: {status}')

    return wrapper

# With this function we calculate the bmi
@define_status
def bmi_calculator(height: float, weight:float) -> float:
    bmi = weight / (height**2)
    print (f'Your Body Mass Index is :{bmi}')
    return bmi


def run():
    # For the user to introduce it´s data
    height = float(input('Your height in meters: '))
    weight= float(input('Your weight in kilograms: '))

    bmi_calculator(height,weight)


if __name__ == '__main__':
    run()