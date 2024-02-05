# -*- coding: utf-8 -*-
from wordcloud import WordCloud

with open("key.txt",encoding='utf-8') as fp:    # 英文字的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud().generate(txt)      # 由txt文字產生WordCloud物件
imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
imageCloud.show()                   # 顯示詞雲影像檔

wd.to_file('辭庫檔.png')