import numpy as np
import matplotlib.pyplot as plt

# 折れ線グラフを出力
left = np.array([1, 2, 3, 4, 5])
height = np.array([100, 300, 200, 500, 400])
plt.plot(left, height)

bar_height = np.array([100, 200, 300, 400, 500])
line_height = np.array([100, 300, 200, 500, 400])
 
# 棒グラフを出力
fig, ax1 = plt.subplots()
ax1.bar(left, bar_height, align="center", color="royalblue", linewidth=0)
ax1.set_ylabel('Axis for bar')
 
# 折れ線グラフを出力
ax2 = ax1.twinx()
ax2.plot(left, line_height, linewidth=4, color="crimson")
ax2.set_ylabel('Axis for line')
plt.show()
