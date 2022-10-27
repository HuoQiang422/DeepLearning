# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/23 19:14
@Auth ： 霍强
@File ：jieba_1.py
@IDE ：PyCharm
@Motto:清枫寒漓
"""
import wordcloud
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import PIL.Image as Image
import os
with open('log.txt','r',encoding='utf-8')as f:
    content = f.read()

# print(content)
# content=content.replace('我','').replace('了','').replace('的','').replace('\n','')
# split = jieba.lcut(content)
# word_cloud = ' '.join(split)
cloud = wordcloud.WordCloud(background_color="white", width=1600, height=800, max_words=4000,font_path='C:\Windows\Fonts\HGXK_CNKI.TTF'
                            ,stopwords={'这','的','就','也','是','怪小兀'})
cloud.generate(content)
cloud.to_file('result1.png')