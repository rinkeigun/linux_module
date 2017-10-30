import math
import numpy as np
from matplotlib import pyplot


x = np.random.randn(30)
sin_y = np.sin(x) + np.random.randn(30)

#pyplot.rcParams['font.family'] = 'IPAPGothic'
pyplot.rcParams['font.family'] = 'IPAMincho'
pyplot.rcParams['font.size'] = 20
pyplot.rcParams["figure.figsize"] = [20,12]
pyplot.rcParams['xtick.labelsize'] = 15
pyplot.rcParams['ytick.labelsize']=15
pyplot.plot( x, sin_y, "o" )
pyplot.title(u'散布図')
#pyplot.title(u'fengbutu')

#pyplot.xlabel('X-Axis')
#pyplot.ylabel('Y-Axis')

#pyplot.legend()
pyplot.show()
