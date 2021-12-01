import weibull 
import csv
import pandas
from weibull.weibull import Analysis

data = pandas.read_csv(r'data1.csv', delimiter=',')
data1 = pandas.DataFrame(data, columns=['TBF'])
fail_times = data1
analysis = weibull.Analysis(fail_times, unit='hour')
analysis.fit(method='mle')
analysis.probplot()