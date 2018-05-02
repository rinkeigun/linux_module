import numpy as np
import pandas as pd
import seaborn as sns

data = np.array(positions)
df = pd.DataFrame(data, columns=['x', 'y'])

# (0,0)座標が画面の左上なのでy軸のみ順番を反転
sns.jointplot(data=df, x='x', y='y', xlim=(0, window_size[0]), ylim=(window_size[1], 0))