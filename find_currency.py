import re
from normalization import Normalizer

def regexfind():
    f = open('./test_data/blog.txt', 'r', encoding='utf8')
    raw = f.read()
    # compose re from keys in normalizer's currency dictionaries
    normalizer = Normalizer()
    symbols = "|".join(normalizer.symbolDict.keys())
    abbreviations =  "|".join(normalizer.abbreviationDict.keys())
    re_currency = re.compile(r'((?i)%s|%s)\s?([\d\,\s]*\d)\.?(\d*)\s?((?i)million|billion|trillion)?' % (symbols, abbreviations))
    # divided into four groups: (currency symbol, integer, decimal, scale)
    currency = re.findall(re_currency, raw)
    return currency


if __name__ == '__main__':

    fout = open('./out/result.txt', 'w', encoding='utf8')
    normalizer = Normalizer()

    words = regexfind()
    for w in words:
        normalizer.normalize_currency(w)
        fout.write(str(w))
        fout.write('\n')
