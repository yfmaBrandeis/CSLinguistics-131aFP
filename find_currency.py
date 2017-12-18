import re
from normalization import Normalizer
import json


def regexfind():
    f = open('./bloomberg/data/bloomberg.json', 'r', encoding='utf8')
    data = json.load(f)

    # compose re from keys in normalizer's currency dictionaries
    symbols = '\$|£|€|¥|fr|fr\.|krusd|gbp|eur|jpy|aud|cad|chf|sek|hkd'
    scales = 'hundred|thousand|million|billion|trillion'
    re_currency = re.compile(r'((?i)%s)\s?([\d\,\s]*\d)\.?(\d*)\s?((?i)%s)?' % (symbols, scales))

    # divided into four groups: (currency symbol, integer, decimal, scale)
    result = []
    for js in data:
        temp = re.findall(re_currency, str(js["news_body"]))
        if temp is not None:
            result.append(temp)
        else:
            result.append([('', '', '', '')])
    return result

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

    res = regexfind()

    for ls in res:
        fout.write('============================================\n')
        for found in ls:
            fout.write(str(found))
            fout.write('\n')
        fout.write('\n')


