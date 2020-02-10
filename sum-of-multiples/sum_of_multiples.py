def sum_of_multiples(limit, multiples):
    return sum({num for multiple in multiples if multiple
                for num in range(multiple, limit, multiple)})