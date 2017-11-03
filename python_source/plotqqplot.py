# probplotの使い方が間違っている？

from numpy.random import *
import numpy as np 
import scipy.stats as stats
import pandas
import matplotlib.pyplot as plt

normal = randn(1000) # 標準正規分布に従う乱数を1000個生成
comparison = rand(1000) #比較のため乱数を1000個生成

#plt.hist( comparison, bins=100 )
#plt.hist( normal, bins=100 )
#stats.probplot(normal, dist="norm", fit=True, plot=pylab)
#stats.probplot(normal, dist="norm", plot=plt)
stats.probplot(comparison, dist="norm", plot=plt)
#stats.probplot(normal, dist="norm")
plt.show()
