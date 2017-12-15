import re
from normalization import Normalizer

def regexfind():
    f = open('./test_data/blog.txt', 'r', encoding='utf8')
    raw = f.read()
    # divided into four groups: (currency symbol, integer, decimal, scale)
    currency = re.findall(r'((?i)\$|USD)\s?([\d\,\s]*\d)\.?(\d*)\s?((?i)million|billion|trillion)?', raw)
    return currency


if __name__ == '__main__':

    fout = open('./out/result.txt', 'w', encoding='utf8')
    normalizer = Normalizer()

    words = regexfind()
    for w in words:
        normalizer.normalize_currency(w)
        fout.write(str(w))
        fout.write('\n')
