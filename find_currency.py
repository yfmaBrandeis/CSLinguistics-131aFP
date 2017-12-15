import re
import currency_table

def regexfind():
    f = open('./test_data/blog.txt', 'r', encoding='utf8')
    raw = f.read()
    # divided into four groups: (currency symbol, integer, decimal, scale)
    currency = re.findall(r'((?i)\$|USD)\s?([\d\,\s]*\d)\.?(\d*)\s?((?i)million|billion|trillion)?', raw)
    return currency


if __name__ == '__main__':

    fout = open('./out/result.txt', 'w', encoding='utf8')
    currency_dict = currency_table.CurrencyTable

    words = regexfind()
    for w in words:
        fout.write(str(w))
        fout.write('\n')

    """
    if len(scale) != 0:
         currency_dict[(integer.decimal) + scale + symbol]
    else:
        if len(decimal) == 0:
            currency_dict[integer + symbol]
        else if len(decimal) == 1:
            decimal append '0'
        else if len(decimal) == 2:
            currency_dict[integer + symbol + decimal + symbol]
        else
            currency_dict[(integer.decimal) + symbol]
    """
