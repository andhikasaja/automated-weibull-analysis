import weibull 
import csv
import pandas
from weibull.weibull import Analysis

data = pandas.read_csv(r'data1.csv')
data1 = pandas.Series(data, index="TBF")
bool(data1)
fail_times = [data1]
#fail_times = [40, 540, 639, 660, 765, 812, 845, 943, 1419, 2188, 3389, 4265, 4320, 4404, 5580, 7368, 10480, 14370, 21120, 35650, 37806, 38640, 50470]
analysis = weibull.Analysis(fail_times, unit='hour')
analysis.fit(method='mle')
analysis.probplot()