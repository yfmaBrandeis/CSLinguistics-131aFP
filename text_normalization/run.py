"""
Run normalizer against data scrapped from Bloomberg
"""

import json
from regexfinder import RegexFinder
from normalization import CurrencyNormalizer


def run(bloomberg):
    if bloomberg:
        rfinder = RegexFinder()
        normalizer = CurrencyNormalizer()
        f_in = open('../bloomberg/data/bloombergDec.json', 'r', encoding='utf8')
        f_out = open('../out/normalized_bloombergDec.txt', 'w', encoding='utf8')
        f_original = open('../out/original_bloombergDec.txt', 'w', encoding='utf8')
        f_extract = open('../out/currency_extract.txt', 'w', encoding='utf8')
        bloomberg_data = json.load(f_in)

        for article in bloomberg_data:
            f_out.write('============= Start of Article ============\n')
            f_out.write('Title: ' + article["news_title"][0] + '\n\n')
            for line in article["news_body"]:
                f_out.write(rfinder.replace_currency(line) + '\n')
            f_out.write('============== End of Article =============\n\n')

            f_original.write('============= Start of Article ============\n')
            f_original.write('Title: ' + article["news_title"][0] + '\n\n')
            for line in article["news_body"]:
                f_original.write(str(line) + '\n')
            f_original.write('============== End of Article =============\n\n')

            f_extract.write('============= Start of Article ============\n')
            f_extract.write('Title: ' + article["news_title"][0] + '\n\n')
            result = []
            if 'news_body' in article.keys():
                temp = rfinder.fetch_currency(str(article["news_body"]))
            if temp is not None:
                result.extend(temp)
            else:
                result.extend([('', '', '', '')])

            for t in result:
                f_extract.write(str(t) + '\t\t' + normalizer.normalize_currency(t))
                f_extract.write('\n')
            f_extract.write('============== End of Article =============\n\n')


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        '-b', '--bloomberg',
        action='store_true',
        help='bloomberg data.'
    )

    args = parser.parse_args()
    run(args.bloomberg)
