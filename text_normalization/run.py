
import json
from regexfinder import RegexFinder
from normalization import CurrencyNormalizer


def run(filename):
    """Run normalizer against data scrapped from Bloomberg website"""
    rfinder = RegexFinder()
    normalizer = CurrencyNormalizer()
    f_in = open('../bloomberg/data/%s' % filename, 'r', encoding='utf8')
    f_normalized = open('../out/normalized_%s.txt' % filename, 'w', encoding='utf8')
    f_original = open('../out/original_%s.txt' % filename, 'w', encoding='utf8')
    f_extract = open('../out/currency_extract_%s.txt' % filename, 'w', encoding='utf8')
    bloomberg_data = json.load(f_in)

    for article in bloomberg_data:
        f_normalized.write(
            '\n=== Title: ' + article["news_title"][0] + ' ===\n\n')
        f_original.write(
            '\n=== Title: ' + article["news_title"][0] + ' ===\n\n')
        if 'news_body' in article.keys():
            for line in article["news_body"]:
                f_normalized.write(rfinder.replace_currency(line) + '\n')
                f_original.write(str(line) + '\n')

        f_extract.write('\n================================================\n\n')
        result = []
        if 'news_body' in article.keys():
            temp = rfinder.fetch_currency(str(article["news_body"]))
        if temp is not None:
            result.extend(temp)
        else:
            result.extend([('', '', '', '')])

        for t in result:
            f_extract.write(str(t) + '\t\t' + normalizer.normalize_currency(t) + '\n')


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str,
                        help="run normalizer against data scrapped\n"
                             "filename options:\t"
                             "2010-2017.json\t"
                             "BiggerData.json\t"
                             "bloombergDec.json\t"
                             "outputYear2017.json\t"
                        )
    args = parser.parse_args()
    try:
        run(args.filename)
    except FileNotFoundError:
        print("No such file found in ../bloomberg/data/")
