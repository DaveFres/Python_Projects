def prime_factors(natural_number):

    list_of_factors = []
    divider = 2

    while natural_number > 1:
        while natural_number % divider == 0:
            list_of_factors.append(divider)
            natural_number /= divider

        divider += 1

    return list_of_factors
