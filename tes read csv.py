from os import write
import pandas
import csv

data = pandas.read_csv(r'data1.csv')

data1 = csv.writer(data, )
data1.writerow(',')

data2 = pandas.DataFrame(data1, columns=['TBF'])

print (data2)