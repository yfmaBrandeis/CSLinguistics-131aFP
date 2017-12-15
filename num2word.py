
"""Convert an integer number n into a list of english words. input number as a
 string, break the string into groups of 3 digits, convert each part recursively
 """


def num2word(num):
    if len(num) == 1:
        return [ones[int(num)]]
    elif len(num) == 2:
        if int(num[0]) == 0:
            return num2word(num[1:])
        elif int(num[0]) < 2:
            return [ones[int(num)]]
        else:
            return [tens[int(num[0])], ones[int(num[1])]]
    elif len(num) == 3:
        if int(num[0]) == 0:
            return num2word(num[1:])
        elif num[1:] == '00':
            return [ones[int(num[0])], 'hundred']
        else:
            return [ones[int(num[0])], 'hundred', 'and'] + num2word(num[1:3])
    else:
        sc = (len(num)-1) // 3   # decide the index of scales list
        mod = len(num) % 3       # handle if the length cannot be divided by 3
        if mod != 0:
            return num2word(num[:mod]) + [scales[sc], ''] + num2word(num[mod:])
        elif num[:3] == '000':
            return num2word(num[3:])
        else:
            return num2word(num[:3]) + [scales[sc], ''] + num2word(num[3:])


"""convert digits of the input number(string type) to list of english words"""


def digit2word(num):
    return [digits[int(d)] for d in num]


ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']
scales = ['', 'thousand', 'million', 'billion', 'trillion']
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine']


if __name__ == '__main__':

    print(num2word('15'))
    print(num2word('65'))
    print(num2word('500'))
    print(num2word('530'))
    print(num2word('1500'))
    print(num2word('100000'))
    print(num2word('110500'))
    print(num2word('10000'))
    print(num2word('100100000'))
    print(num2word('100000000000'))
    print(digit2word('530'))

    # TODO(1): replace all '' in the list with 'and', except trailing ones
