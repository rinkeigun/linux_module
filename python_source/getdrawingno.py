from PIL import Image


def getADrawingNo(drawingNo_list, today_str):
    """図番を取得
    """
    
    l_in = [s for s in drawingNo_list if today_str in s]
    # today_strのキーワードでdrawingNo_listから文字列を取得
    # 取得できた場合、最大値を取得し、＋１で文字列を生成
    if len(l_in) > 0:
        v = int(max(l_in).split("-")[2])+1
    # 取得できない場合、新規文字列かつリストをクリア
    else:
        v = 0
        drawingNo_list.clear()
    # 新しい図番の生成
    drawing_str = "ANT-{}-{:02}".format(today_str, v)
    # 文字列をリストに追加
    drawingNo_list.append(drawing_str)
    
    # 文字列を返す
    return( drawing_str)

def pasteImage(wi, img):
    """画像の張込み wi[width, height]
    """
    
    # 指定サイズの白画像生成
    white_img = Image.new("RGB", (wi))
    
    # white_img のwidth/heightの比率 rate_white
    rate_white = wi[0]/wi[1]
    
    # 画像の縦横サイズ、比率rate_img
    img = Image.open(img)
    width, height = img.size
    rate_img = width/height
    
    # 張込みサイズの決定
    x = 0
    y = 0
    if rate_white > rate_img:
        rate = wi[1]/height
        x = (wi[0]-rate*width)/2
    else:
        rate = wi[0]/width
        y = (wi[1]-rate*height)/2
        
    # img のサイズ調整
    size = img.size
    img = img.resize((int(size[0]*rate),int(size[1]*rate)))
    
    # 画像合成
    white_img.paste(img, (int(x),int(y)))
    
    # 合成画像を戻す
    return(white_img)
    


if __name__ =="__main__":
    #aa = ["ANT-180828-01", "ANT-180827-02"]
    #print(getADrawingNo(aa, "180829"))
    pasteImage((100,10), "D:\\path_to_symbol\\Symbol\\名村造船所\\D772.PNG")