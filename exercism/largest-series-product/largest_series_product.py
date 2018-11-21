def largest_product(size, series):

    if size == "" and series == 0:
        return 1

    if series > len(size) or size.isdigit() is False or series < 0:
        raise ValueError('Please check the input data')

    result = 0

    for j in range(0, len(size) - series + 1):
        temp = 1

        for i in range(j, j + series):
            temp *= int(size[i])

        if temp > result:
            result = temp

    return result

