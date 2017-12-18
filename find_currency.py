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


if __name__ == '__main__':

    fout = open('./out/result.txt', 'w', encoding='utf8')

    res = regexfind()

    for ls in res:
        fout.write('============================================\n')
        for found in ls:
            fout.write(str(found))
            fout.write('\n')
        fout.write('\n')


