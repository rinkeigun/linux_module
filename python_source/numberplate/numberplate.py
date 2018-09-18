import cv2
import numpy as np
from matplotlib import pyplot as plt

minPlateRatio = 0.5 # ナンバープレートの幅/高さの最小比
maxPlateRatio = 6   # ナンバープレートの幅/高さの最大比

# colorpicker.py による値
lower_blue1 = np.array([40, 0, 179])
higher_blue1 = np.array([60, 13, 255])
lower_blue2 = np.array([110, 10, 115])
higher_blue2 = np.array([130, 30, 195])



def findPlateNumberRegion(img):
    """ナンバープレートの四角形領域を探し出し
    """
    
    # 四角形領域
    region = []
    
    # 外枠の輪郭
    contours_img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # 最小領域を抽出
    list_rate = []
    for i in range(len(contours)):
        cnt = contours[i]
        
        # 領域の計算
        area = cv2.contourArea(cnt)

        # 小さい面積の領域を対象外
        if area < 1000:
            continue
        
        # 最小矩形に変換
        rect = cv2.minAreaRect(cnt)
        
        # 矩形からBox化、更にint化
        box = np.int32(cv2.boxPoints(rect))
        
        # 高さ、幅の算出
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        
        # 幅、高さの比
        ratio = float(width) / float(height)
        rate = getxyRate(cnt)
        
        # 比率が不適合のを除外
        if ratio > maxPlateRatio or ratio < minPlateRatio:
            continue

        # 適合のを領域リストに追加
        region.append(box)
        list_rate.append(ratio)
    index = getSatifiestBox(list_rate)
    return region[index]
        
    
def getSatifiestBox(list_rate):
    """ナンバープレートである可能性が一番高いのを探す
    """
    
    for index, key in enumerate(list_rate):
        list_rate[index] = abs(key - 3)
    index = list_rate.index(min(list_rate))
    return index
    
def getxyRate(cnt):
    """XY比率の算出
    """

    x_height = 0
    y_height = 0
    x_list = []
    y_list = []
    for location_value in cnt:
        location = location_value[0]
        x_list.append(location[0])
        y_list.append(location[1])
    x_height = max(x_list) - min(x_list)
    y_height = max(y_list) - min(y_list)
    return x_height * (1.0) / y_height * (1.0)

def location(file):
    # イメージの読込
    img = cv2.imread(file)
    
    # 読み込んだイメージのHSV化
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 背景色の２値化
    # 白、これらの色を複数指定することは可能、今後も各色を拡張
    mask1 = cv2.inRange(hsv_img, lower_blue1, higher_blue1)
    mask2 = cv2.inRange(hsv_img, lower_blue2, higher_blue2)
    mask = mask1+mask2
    
    # ２値化
    res = cv2.bitwise_and(img, img, mask=mask)
    
    # グレースケール
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    
    # ガウシアンぼかし、平滑化、ノイズ除去
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
    
    # sobel、エッジ―検出、ナンバープレートの検出
    sobel = cv2.convertScaleAbs(cv2.Sobel(gaussian, cv2.CV_16S, 1, 0, ksize=3))
    
    # 標的をより明確化（強弱をつける）
    ret, binary = cv2.threshold(sobel, 150, 255, cv2.THRESH_BINARY)
    
    
    # 閉じた領域
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 5))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, element)
    
    # 適合領域を検索
    region = findPlateNumberRegion(closed)
    x = [tmpa[0] for tmpa in region]
    minx = min(x)
    maxx = max(x)
    y = [tmpa[1] for tmpa in region]
    miny = min(y)
    maxy = max(y)
    #cv2.drawContours(img, [region], 0, (0, 255, 0), 2)
    minusx = 0
    hw = [maxx-minx-2*minusx,maxy-miny]
    return(img[miny:maxy, minx+minusx:maxx-minusx], hw, region-[minx+minusx, miny])

    #cv2.imshow("img", img[miny:maxy, minx:maxx])
    #cv2.waitKey(0)
    

def Change2Rect(img, hw, region):
    """斜め図形を矩形に変更
    """
    
    rows,cols,ch = img.shape
    pts1 = np.float32([region[0],region[1],region[2],region[3]])
    pts2 = np.float32([[0, hw[1]],[0,0],[hw[0],0],[hw[0],hw[1]]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(hw[0],hw[1]))
    #plt.subplot(121),plt.imshow(img),plt.title('Input')
    #plt.subplot(122),plt.imshow(dst),plt.title('Output')
    #plt.show()
    
    return( dst )

def find_end(start_, arg, height_or_width, black, white, black_max, white_max):
    end_ = start_+1
    for m in range(start_+1, height_or_width-1):
        if (black[m] if arg else white[m]) > (0.95 * black_max if arg else 0.95 * white_max):
            end_ = m
            break
    return end_


def div2onechar(img_thre, kernel):
    """文字の取り出し
    """
    dilation = cv2.dilate(img_thre,kernel,iterations = 1)
    img_thre = dilation
    white = []
    black = []
    height = img_thre.shape[0] 
    width = img_thre.shape[1] 
    white_max = 0
    black_max = 0
    #print(height, width)
    for i in range(width): 
        s = 0
        t = 0
        for j in range(height):
            if img_thre[j][i] == 255:
                s += 1
            if img_thre[j][i] == 0:
                t += 1
        white_max = max(white_max, s)
        black_max = max(black_max, t)
        white.append(s)
        black.append(t)
        #print("black", i, black_max, white_max)
    arg = False
    if black_max > white_max:
        arg = True

    #arg = True
    n = 1
    start = 1
    end = 2
    while n < width-2:
        n += 1
        if (white[n] if arg else black[n]) > (0.05 * white_max if arg else 0.05 * black_max):
            # 上面这些判断用来辨别是白底黑字还是黑底白字
            # 0.05这个参数请多调整，对应上面的0.95
            start = n 
            end = find_end(start, arg, width, black, white, black_max, white_max)
            n = end 
            
            if end-start > 5: 
                cj = img_thre[1:height, start:end] 
                cv2.imshow('caijian'+str(n), cj) 
                cv2.waitKey(0)


def div2Horizental(img):
    # イメージのグレースケール
    height = img.shape[0]
    width  = img.shape[1]
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img[1+2:height, 3:width-2], cv2.COLOR_BGR2GRAY)
    
    # ２値化
    img_thre = img_gray 
    cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV, img_thre)


    
    # 画像分割
    # 文字を太くする
    kernel = np.ones((1,1),np.uint8)
    dilation = cv2.dilate(img_thre,kernel,iterations = 1)
    img_thre = dilation
    cv2.imshow('caijian', img_thre)
    cv2.waitKey(0)

    white = []
    black = []
    height = img_thre.shape[0]
    width  = img_thre.shape[1]
    white_max = 0
    black_max = 0
    
    # 全画像の行単位で白黒を集計
    for i in range(height):
        s = 0
        t = 0
        for j in range(width):
            if img_thre[i][j] == 255:
                s += 1
            if img_thre[i][j] == 0:
                t += 1
        white_max = max(white_max, s)
        black_max = max(black_max, t)
        
        white.append(s)
        black.append(t)
    
    # 白地か黒地かの判定
    arg = False
    if black_max > white_max: 
        arg = True

    #print("black", arg, black_max, white_max)
    n = 1
    start = 1
    end = 2
    cnter = 0
    while n < height-2:
        n += 1
        #print(white[n] if arg else black[n])
        #print( 0.05 * white_max if arg else 0.05 * black_max)
        if (white[n] if arg else black[n]) > (0.05 * white_max if arg else 0.05 * black_max):
            start = n
            end = find_end(start, arg, height, black, white, black_max, white_max)
            n = end 
        
            if end-start > 5:
                cj = img_thre[start:end+1, 1:width]
                cv2.imshow('caijia'+str(n), cj)
                cv2.waitKey(0)
                # 文字を太くする
                size = 2 if cnter == 0 else 1
                print( "cnter and size " , cnter, size)
                kernel = np.ones((size,size),np.uint8)
                div2onechar(cj, kernel)
                cnter += 1
    
    
def main_process(file):
    img, hw, region = location(file)
    img = Change2Rect(img, hw, region)
    div2Horizental(img)


if __name__ == '__main__':
    file = "car_id\\20180729112549.jpg"
    main_process(file)
    