#!/usr/bin/env python
# coding=utf-8

import csv


TRAIN_FILE = './train.csv'

def load_data(file_name):

    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            if reader.line_num == 1:
                continue
            id = line[0]
            tmp = line[44]
            if tmp != '[]':
                print id, tmp
                break


def process():
    load_data(TRAIN_FILE)


if __name__ == '__main__':
    process()
