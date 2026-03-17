# This function adds only the positive numbers in a list.
def calculate_total(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
        else:
            total += 0
    return total


# This function finds the maximum number in a list.
def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


# This function checks whether a number is even.
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
