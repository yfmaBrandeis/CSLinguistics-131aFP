# **Run regex on scrapped data and get normalized result**

## run.py
Run normalizer against scraped data from Bloomberg website. Change directory to text_normalization and run following command:
```
python3 run.py <filename>
```
<filename\> options:

- 2010-2017.json
- BiggerData.json
- bloombergDec.json
- outputYear2017.json

Output results are dumped in [../out](../out)

## regexfinder.py
Provide functions that can fetch currency units in given text, or replace these units with normalized English words.

## normalization.py
Provide functions that can normalize given currency units

## num2word.py
Provide functions that can normalize positive integers, digits and real numbers.
