# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/23 17:37
@Auth ： 霍强
@File ：JiebaLearn.py
@IDE ：PyCharm
@Motto:清枫寒漓
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import os
import numpy as np
import PIL.Image as Image
import re

new_texts=[]
regex1="2022.*"
regex2="消息.*"
for word in open('打击盗版.txt','r',encoding='utf-8'):
    word = word.replace('[图片]', '').replace('[表情]', '').replace('=','').replace('\n','').replace(' ','')
    if word==''or re.search(regex1,word) is not None or re.search(regex2,word) is not None:
        continue
    new_texts.append(word)
with open('log.txt','w',encoding='utf-8') as f:
    for word in new_texts:
        f.write(word+'\n')


