import weibull
# import csv
import pandas
# from weibull.weibull import Analysis

# with open('data1.csv', newline='') as f:
#    g = csv.reader(f)
#    fail_times = next(g)
data = pandas.read_csv("data1.csv", )
data = pandas.DataFrame(index=[10])
print(data)
# data2 = (data)
# print(data)
# data1 = pandas.DataFrame(data)
# print(data1)
# bool(data1)
# fail_times = [data]
# fail_times = [40, 540, 639, 660, 765, 812, 845, 943, 1419, 2188, 3389, 4265, 4320, 4404, 5580, 7368, 10480, 14370, 21120, 35650, 37806, 38640, 50470]
analysis = weibull.Analysis(data, unit='hour')
analysis.fit(method='mle')
analysis.probplot()
