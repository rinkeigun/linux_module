# -*- coding: utf-8 -*-
import pyautogui
import time
from datetime import datetime
import numpy as np
import pandas as pd
import seaborn as sns

def get_now():
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return now

def get_cursor_loop(loop_second):
    """
    0.1秒ずつ、指定秒数分カーソル位置を取得

    args
    ----
    loop_second:int
    データを取得する秒数
    """
    times = []
    positions = []

    for _ in range(0, loop_second*10):
        # 時刻とカーソル位置の取得
        now = get_now()
        x, y = pyautogui.position()

        # リストに情報を追加
        times.append(now)
        positions.append([x, y])
        # sleep
        time.sleep(0.1)

    return times, positions

def get_window_size():
    window_size = pyautogui.size()
    return window_size

if __name__ == '__main__':
    times, positions = get_cursor_loop(6)
    print(positions)
    window_size = get_window_size()
    print(window_size)
    data = np.array(positions)
    df = pd.DataFrame(data, columns=['x', 'y'])

    # (0,0)座標が画面の左上なのでy軸のみ順番を反転
    sns.jointplot(data=df, x='x', y='y', xlim=(0, window_size[0]), ylim=(window_size[1], 0))