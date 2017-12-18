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

def regex_find_date():
    f = open('./test_data/date.txt', 'r', encoding='utf8')
    raw = f.read()
    re_date_space = re.compile(r"""(?i)                       # ignore case
                                   ([a-z.]+|[12]?\d)          # month in either word or digit format
                                   [\s,]+                     # separator
                                   ([123]?\d)[thrdstn]{2}     # date possibly follow by st/nd/rd/th
                                   [\s,]?                     # separator
                                   ([12]\d{3})?               # match year (1000~2999) optional
                             """, re.X)             # verbose
    re_date_slash = re.compile(r"""(1[0-2]|0?[1-9])           # month
                                   \/                         # '/'
                                   (3[01]|[12]?[0-9]|0[1-9])  # date
                                   \/([12]\d{3}|[0-9]{2})     # year 'yy' or 'yyyy'
                                   """, re.X)
    date = re.findall(re_date_space, raw) + re.findall(re_date_slash, raw)
    return date

if __name__ == '__main__':

    fout = open('./out/result.txt', 'w', encoding='utf8')
    normalizer = Normalizer()

    words = regexfind()
    dates = regex_find_date()
    for w in words:
        normalizer.normalize_currency(w)
        fout.write(str(w))
        fout.write('\n')
