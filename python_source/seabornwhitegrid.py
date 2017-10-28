import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

x = np.random.normal(size=100)
sns.distplot(x);

plt.show()
