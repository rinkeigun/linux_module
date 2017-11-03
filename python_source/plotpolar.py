import numpy as np
import matplotlib.pyplot as plt
"""
極方程式
例:アルキメデスの渦巻線
"""

theta = np.arange(0.0, 4*2*np.pi, 0.01) #θの範囲を 0-8π ラジアン(4周分)とする
r = 0.5*theta   ## 極方程式を指定する。
plt.polar(theta,r) # 極座標グラフのプロット

plt.show()
