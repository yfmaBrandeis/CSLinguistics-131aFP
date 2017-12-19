import re
from normalization import Normalizer

normalizer = Normalizer()


def regex_find_currency(s):

    # compose re from keys in normalizer's currency dictionaries
    symbols = '\$|£|€|¥|fr|fr\.|krusd|gbp|eur|jpy|aud|cad|chf|sek|hkd'
    scales = 'hundred\\b|thousand\\b|million\\b|billion\\b|trillion\\b|' \
             'mn\\b|bn\\b|tn\\b|m\\b|b\\b|t\\b'
    re_currency = re.compile(r'(?i)'               # ignore case
                             r'(%s)'               # Group1: currency symbols
                             r'\s?'                # optional space
                             r'([\d\,\s]*\d)'      # Group2: non-decimal number
                             r'\.?'                # decimal space
                             r'(\d+)?'              # Group3: decimal number
                             r'\s?'                # optional space
                             r'(%s)?'              # Group4: option scale
                             % (symbols, scales), re.X)

    # divided into four groups: (currency symbol, integer, decimal, scale)
    return re.sub(re_currency, normalizer.normalize_currency, s)


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

    s = '$1.010 ' \
        '$2.02 ' \
        '$100.40 ' \
        '$100 millionnare ' \
        '$100.45 m'

    res = regex_find_currency(s)
    print(res)
