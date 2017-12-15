import re
import currency_table

def regexfind():
    f = open('./test_data/blog.txt', 'r', encoding='utf8')
    raw = f.read()
    currency = re.findall(r'(\$|USD)\s?(\d[\d\,\.\s]*\d)(?:\s?)'
                          r'(million|billion|trillion)?', raw)
    return currency


if __name__ == '__main__':

    fout = open('./out/result.txt', 'w', encoding='utf8')
    currency_dict = currency_table.CurrencyTable

    words = regexfind()
    for w in words:
        fout.write(str(w))
        fout.write('\n')
