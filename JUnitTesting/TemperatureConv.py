def far_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def cel_far(celsius):
    fahrenheit = (celsius * 9/5) - 32
    return fahrenheit


option = int(input("Enter Value:\n1.Celsius to Fahrenheit\t2.Fahrenheit to Celsius\n"))
if option == 1:
    temp_c = float(input("Enter Temperature:"))
    print(cel_far(temp_c))
if option == 2:
    temp_f = float(input("Enter Temperature:"))
    print(far_cel(temp_f))
else:
    print("Enter Right Value")
