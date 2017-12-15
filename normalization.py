from collections import defaultdict
from num2words import num2words

class Normalizer:
    def __init__(self):
        self.abbreviationDict = defaultdict(list)
        self.abbreviationDict["usd"] = (["u.s. dollar", "cent"], ["u.s. dollars", "cents"])
        self.abbreviationDict["gbp"] = (["pound", "penny"], ["pounds", "pence"])
        self.abbreviationDict["eur"] = (["euro", "cent"], ["euros", "cents"])
        self.abbreviationDict["yen"] = (["yen", "sen"], ["yens", "sens"])
        self.abbreviationDict["aud"] = (["australian dollar", "cent"], ["australian dollars", "cents"])
        self.abbreviationDict["cad"] = (["canadian dollar", "cent"], ["canadian dollars", "cents"])
        self.abbreviationDict["chf"] = (["swiss franc", "rappen"], "swiss francs")
        self.abbreviationDict["sek"] = (["swedish krona", "ore"], ["swedish kronor", "ore"])
        self.abbreviationDict["hkd"] = (["hong kong dollar", "cent"], ["hong kong dollars", "cents"])
        self.symbolDict = defaultdict(list)
        self.symbolDict["$"] = (["dollar", "cent"], ["dollars", "cents"])

        # symbolDict["￥"] = ["yen", "sen"]

    """"normalize a tokenized currency input into english words"""
    def normalize_currency(self, input):
        res, currency = [], None
        # append whole number
        whole_number = self.normalize_number[1]
        res.append(whole_number)
        # check singular/plural and append currency
        if whole_number == "one":
            res.extend([whole_number, self.get_currency(input[0], True)])
        else:
            res.extend([whole_number, self.get_currency(input[0], False)])

    """get the currency's english word.
    If is_single is true return singular form (ex: dollar). Otherwise return
    plural form (ex: dollars).
    Input token(currency toekn
    """
    def get_currency(self, currency_token, is_single, is_cent=False):
        # currency_token is abbreviation
        if currency_token in self.abbreviationDict:
            if not is_cent:
                return self.abbreviationDict.get(currency_token)[0][0] if is_single else\
                       self.abbreviationDict.get(currency_token)[0][1]
            else:
                return self.abbreviationDict.get(currency_token)[1][0] if is_single else\
                       self.abbreviationDict.get(currency_token)[1][1]
        # currency_token is symbol
        elif currency_token in self.symbolDict:
            if not is_cent:
                return self.symbolDict.get(currency_token)[0][0] if is_single else\
                       self.symbolDict.get(currency_token)[0][1]
            else:
                return self.symbolDict.get(currency_token)[1][0] if is_single else\
                       self.symbolDict.get(currency_token)[1][1]

    """normalize the numbers before the decimal points into english words using num2words module.
        whitespaces and non-digit char such as ',' are ignored
        ex: 1234 "one thousand, two hundred and thirty-four"
    """
    def normalize_number(self, number):
        digits = [char for char in number if char.isdigit()]
        digits.reverse()
        num = 0
        factor = 1
        for d in digits:
            num += int(d) * factor
            factor *= 10
        return num2words(num)

    """normalize the numbers after the decimal points into english words.
    ex: for 0.1234, the "1234" is passed as input and return "one two three four"
    """
    def normalize_decimal(self, decimal):
        digits = [char for char in decimal if char.isdigit()]
        nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        return " ".join([nums[int(d)] for d in digits])

if __name__ == '__main__':
    normalizer = Normalizer()
    print(normalizer.get_currency("$", True))
    print(normalizer.get_currency("usd", True, True))
    print(normalizer.get_currency("usd", False))
    print(normalizer.get_currency("jpy", False))
    print(normalizer.normalize_number('1234'))
    print(normalizer.normalize_decimal('12345'))