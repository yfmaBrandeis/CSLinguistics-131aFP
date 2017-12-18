import re
from normalization import Normalizer
import json


def regexfind(s):

    # compose re from keys in normalizer's currency dictionaries
    symbols = '\$|£|€|¥|fr|fr\.|krusd|gbp|eur|jpy|aud|cad|chf|sek|hkd'
    scales = 'hundred|thousand|million|billion|trillion'
    re_currency = re.compile(r'((?i)%s)\s?([\d\,\s]*\d)\.?(\d*)\s?((?i)%s)?'
                             % (symbols, scales))

    # divided into four groups: (currency symbol, integer, decimal, scale)
    return re.findall(re_currency, s)


if __name__ == '__main__':

    f_in = open('./bloomberg/data/bloomberg.json', 'r', encoding='utf8')
    f_out = open('./out/result.txt', 'w', encoding='utf8')
    bloomberg_data = json.load(f_in)
    normalizer = Normalizer()

    result = []
    for js in bloomberg_data:
        temp = regexfind(str(js["news_body"]))
        if temp is not None:
            result.append(temp)
        else:
            result.append([('', '', '', '')])

    for ls in result:
        f_out.write('============================================\n')
        for cur_tuple in ls:
            f_out.write(str(cur_tuple) + '\t\t' + normalizer.normalize_currency(cur_tuple))
            f_out.write('\n')
        f_out.write('\n')


