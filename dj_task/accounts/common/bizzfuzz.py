def bizzfuzz(number):
    """
    Function for bizzfuzz check
    :param number: user random number
    :return: string with result
    """
    if number % 3 == number % 5 == 0:
        return 'BizzFuzz'
    elif number % 3 == 0:
        return 'Bizz'
    elif number % 5 == 0:
        return 'Fuzz'
    else:
        return 'Nothing'