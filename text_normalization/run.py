"""
Run normalizer against data scrapped from Bloomberg
"""

import json
from regex import regex_find_currency

def run(bloomberg):
    if bloomberg:
        f_in = open('../bloomberg/data/bloombergDec.json', 'r', encoding='utf8')
        f_out = open('../out/normalized_bloombergDec.txt', 'w', encoding='utf8')
        bloomberg_data = json.load(f_in)

        result = []
        for article in bloomberg_data:
            f_out.write('=============Start of Article============\n')
            f_out.write('Title: ' + article["news_title"][0] + '\n\n')
            for line in article["news_body"]:
                f_out.write(regex_find_currency(line) + '\n')
            f_out.write('==============End of Article=============\n\n')

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
