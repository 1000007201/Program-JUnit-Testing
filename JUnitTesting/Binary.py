
def decimal_to_binary(number):
    if number >= 1:
        # recursive function call
        decimal_to_binary(number // 2)

    # printing remainder from each function call
    print(number % 2, end='')


# Driver Code
if __name__ == '__main__':
    # decimal value
    number = 24

    # Calling special function
    decimal_to_binary(number)
