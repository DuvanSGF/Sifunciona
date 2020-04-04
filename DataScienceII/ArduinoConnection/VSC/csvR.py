# -*- coding: utf-8 -*-

import csv

lista = [1,2,3]


file = open("eggs.csv", "w", newline='')
spamreader = csv.writer(file)
spamreader.writerow(lista)
file.close()