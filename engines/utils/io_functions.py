# -*- coding: utf-8 -*-
# @Time : 2020/9/9 6:14 下午
# @Author : lishouxian
# @Email : gzlishouxian@gmail.com
# @File : io_functions.py
# @Software: PyCharm
import csv
import pandas as pd


def read_csv(file_name, names, delimiter='t'):
    if delimiter == 't':
        sep = '\t'
    elif delimiter == 'b':
        sep = ' '
    else:
        sep = delimiter
    return pd.read_csv(file_name, sep=sep, quoting=csv.QUOTE_NONE, skip_blank_lines=False, header=None, names=names)


def save_csv(df, file_name, names, delimiter='t'):
    if delimiter == 't':
        sep = '\t'
    elif delimiter == 'b':
        sep = ' '
    else:
        sep = delimiter
    df.to_csv(file_name, quoting=csv.QUOTE_NONE, columns=names, sep=sep, header=False, index=False)
