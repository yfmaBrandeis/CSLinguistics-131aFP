from collections import defaultdict


class CurrencyTable:
    def __init__(self):
        abbrevationDict = defaultdict(list())
        abbrevationDict["usd"] = (["u.s. dollar", "cent"], ["u.s. dollars", "cents"])
        abbrevationDict["gbp"] = (["pound", "penny"], ["pounds", "pence"])
        abbrevationDict["eur"] = (["euro", "cent"], ["euros", "cents"])
        abbrevationDict["yen"] = (["yen", "sen", "rin"], ["yens", "sens", "rins"])
        abbrevationDict["aud"] = (["australian dollar", "cent"], ["australian dollars", "cents"])
        abbrevationDict["cad"] = (["canadian dollar", "cent"], ["canadian dollars", "cents"])
        abbrevationDict["chf"] = (["swiss franc", "rappen"], "swiss francs")
        abbrevationDict["sek"] = (["swedish krona", "ore"], ["swedish kronor", "ore"])
        abbrevationDict["hkd"] = (["hong kong dollar", "cent"], ["hong kong dollars", "cents"])
        symbolDict = defaultdict[list()]
        symbolDict["$"] = ["dollar", "cent"]

        # symbolDict["￥"] = ["yen", "sen"]
