def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Strings must be the same length!")

    # counter_list --- list that contains true/false values. True if elements are not equal

    counter_list = list(i != j for i, j in zip(strand_a, strand_b))

    return sum(counter_list)

