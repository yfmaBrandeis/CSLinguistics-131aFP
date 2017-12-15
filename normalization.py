from collections import defaultdict


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



    def get_currency(self, token, is_single, is_cent=False):
        # case abbreviation
        if token in self.abbreviationDict:
            if not is_cent:
                return self.abbreviationDict.get(token)[0][0] if is_single else\
                       self.abbreviationDict.get(token)[0][1]
            else:
                return self.abbreviationDict.get(token)[1][0] if is_single else\
                       self.abbreviationDict.get(token)[1][1]
        # case symbol
        elif token in self.symbolDict:
            if not is_cent:
                return self.symbolDict.get(token)[0][0] if is_single else\
                       self.symbolDict.get(token)[0][1]
            else:
                return self.symbolDict.get(token)[1][0] if is_single else\
                       self.symbolDict.get(token)[1][1]

    def normalize_number(self, number):
        pass

if __name__ == '__main__':
    normalizer = Normalizer()
    print(normalizer.get_currency("$", True))
    print(normalizer.get_currency("usd", True, True))
    print(normalizer.get_currency("usd", False))
    print(normalizer.get_currency("jpy", False))
