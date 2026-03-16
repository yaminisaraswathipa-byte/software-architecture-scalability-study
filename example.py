def calculate_total(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
        else:
            total += 0
    return total


def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False