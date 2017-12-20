import re
from normalization import CurrencyNormalizer


class RegexFinder:

    def __init__(self):
        """Initialize regex matching currency units and corresponding
        normalization functions from normalization module
        """
        self.normalizer = CurrencyNormalizer()
        self.regex = self.compile_currency_regex()

    def compile_currency_regex(self):
        """Compose and return regex using keys in currency dictionary
        :return: regex obj for matching currency units
        """
        symbols = '\$|£|€|¥|fr|fr\.|krusd|gbp|eur|jpy|aud|cad|chf|sek|hkd'
        scales = 'hundred\\b|thousand\\b|million\\b|billion\\b|trillion\\b|' \
                 'mn\\b|bn\\b|tn\\b|m\\b|b\\b|t\\b'

        # divided into four groups: (currency symbol, integer, decimal, scale)
        re_currency = re.compile(r'(?i)'            # ignore case
                                 r'(%s)'            # Group1: currency symbols
                                 r'\s?'             # optional space
                                 r'([\d\,\s]*\d)'   # Group2: non-decimal number
                                 r'\.?'             # decimal space
                                 r'(\d+)?'          # Group3: decimal number
                                 r'\s?'             # optional space
                                 r'(%s)?'           # Group4: option scale
                                 % (symbols, scales), re.X)
        return re_currency

    def fetch_currency(self, s):
        """Fetch all currency tokens from a text and return a list of tuples
        :param s: text that regex testing on, string type
        :return: a list of matched part, as a tuple of matched groups
        """
        return re.findall(self.regex, s)

    def replace_currency(self, s):
        """Replace all currency tokens in text with normalized english words
        :param s: text that regex testing on, string type
        :return: text with matched part replaced with normalized english words,
        string type
        """
        return re.sub(self.regex, self.normalizer.normalize_currency, s)


    def regex_find_date(self):
        # f = open('./test_data/date.txt', 'r', encoding='utf8')
        # raw = f.read()
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
        # date = re.findall(re_date_space, raw) + re.findall(re_date_slash, raw)
        return


if __name__ == '__main__':

    """Doctest with some simple cases"""
    test_str = '$1.010 \n' \
               '$2.02 \n' \
               '$100.40 \n' \
               '$100 millionnare \n' \
               '$100.45 m \n' \
               '$ 435 tn \n' \
               '$300billion \n'

    rfinder = RegexFinder()
    print(rfinder.fetch_currency(test_str))
    print(rfinder.replace_currency(test_str))

