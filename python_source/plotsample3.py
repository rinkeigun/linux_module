#%matplotlib inline
import math
import numpy as np
from matplotlib import pyplot


x = np.random.randn(30)
sin_y = np.sin(x) + np.random.randn(30)

pyplot.rcParams['font.family'] = 'IPAPGothic'
pyplot.rcParams['figure.figsize'] = [20, 12]
pyplot.rcParams['font.size'] = 20 
pyplot.rcParams['xtick.labelsize'] = 15
pyplot.rcParams['ytick.labelsize'] = 15

#DataFrameが未定義エラー
df =DataFrame( np.arange(0,12).reshape(6, -1), columns = ['初め', '終わり'])
df.plot(kind = 'bar', x = '初め', y = '終わり').set(xlabel = '初め', ylabel = '終わり')
#pyplot.plot( x, sin_y, "o" )
#pyplot.title(u'散布図')
#pyplot.title(u'fengbutu')
#pyplot.xlabel('X-Axis')
#pyplot.ylabel('Y-Axis')
#pyplot.legend()
pyplot.show()
