def odd_even(number):
    if number == 0:
        return 'Please enter a non zero number.'
    elif number % 2 == 0:
        return 'Even!'
    return 'Odd!'

print(odd_even(0))
print(odd_even(5))
print(odd_even(4))
print(odd_even(2))
print(odd_even(5))