import matplotlib.pyplot as plt
import pandas
import numpy as np
import weibull

data = pandas.read_csv("data3_noeditedit.csv")
data = data.T
data = data.values.tolist()

analysis = weibull.Analysis(data[0], unit='hour')
analysis.fit(method='mle')
analysis.fr()
