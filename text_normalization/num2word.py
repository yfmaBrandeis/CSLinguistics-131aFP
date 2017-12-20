
"""Convert an integer number to a list of english words. input number as a
 string, break the string into groups of 3 digits, convert each part recursively
 """


def num2word(num):
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
            # decide the scale
            sc = (len(num)-1) // 3
            # handle if the length cannot be divided by 3
            group = 3 if len(num) % 3 == 0 else len(num) % 3
            return num2word(num[:group]) + [scales[sc]] + num2word(num[group:])


"""convert digits of the input number(string type) to list of english words"""


def digit2word(num):
    return [digits[int(d)] for d in num]


ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']
scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine']


if __name__ == '__main__':

    pass
