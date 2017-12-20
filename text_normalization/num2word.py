

def num2word(num):
    """Normalize positive integer number and return a list of english words.
    Input number as a string, break the string into groups of 3 digits, convert
    each part recursively. RANGE: * ~ ***,***,***,***,***
    :param num: input positive integer number, string type
    :return: a list of normalized english words, list type
    """
    if num == '':
        return []
    elif num[0] == '0':
        return num2word(num[1:])
    else:
        if len(num) == 1:
            return [ones[int(num)]]
        elif len(num) == 2:
            if int(num[0]) < 2:
                return [ones[int(num)]]
            else:
                return [tens[int(num[0])]] + num2word(num[1])
        elif len(num) == 3:
            return [ones[int(num[0])], 'hundred'] + num2word(num[1:3])
        else:
            # decide the scale of current group
            sc = (len(num)-1) // 3
            # handle if the length cannot be divided by 3
            group = 3 if len(num) % 3 == 0 else len(num) % 3
            return num2word(num[:group]) + [scales[sc]] + num2word(num[group:])


def digit2word(num):
    """Normalize each digit of the input number(string type) and return a list
    of english words
    :param num: sequence of digits, string type
    :return: a list of normalized english words, list type
    """
    return [ones[int(d)] for d in num]


def realnum2word(num):
    """Normalize real number and return a list of english words
    :param num: input real number, string type
    :return: a list of normalized english words, list type
    """
    if num == '0':
        return ['zero']
    elif num[0] == '-':
        return ['minus'] + realnum2word(num[1:])
    else:
        dot_index = num.find('.')
        if dot_index > 0:
            return realnum2word(num[:dot_index]) + ['point'] + \
                   digit2word(num[dot_index+1:])
        else:
            return num2word(num)


ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']
scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']


if __name__ == '__main__':

    """Doctest with some simple cases"""
    test_str = ['0.1', '-1.078', '-17', '20', '100', '100189', '90000000000000']
    for s in test_str:
        print(realnum2word(s))
