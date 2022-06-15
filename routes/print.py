# print.py 파일

# import requests
# URL = '127.0.0.1:3000:\\index\\result'
from hashlib import new
import os
from turtle import color
from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
import re
import pandas as pd
# word_path = '/Users/yunhyeon-ung/Downloads'
pos_word = open(os.path.join('./coef_pos_index1.txt'), 'r',encoding='utf-8').read()
neg_word = open(os.path.join('./coef_neg_index1.txt'), 'r',encoding='utf-8').read()
default_color = 'grey'
lottetext=[]
with open('몬드리안.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        lottetext.append(line)
    
with open('몬드리안부정.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        lottetext.append(line)
    

print(lottetext)

stopwords = pd.read_csv("https://raw.githubusercontent.com/yoonkt200/FastCampusDataset/master/korean_stopwords.txt").values.tolist()
stopwords[:10]

seoul_stopwords = ['JW매리어트','매리어트', '임형철','워커힐','시그니엘','신라스테이' ,'신라','호텔', '리뷰', '숙소', '여행', '트립', '덕분']
for word in seoul_stopwords:
    stopwords.append(word)

def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 정규 표현식 처리
    result = hangul.sub('', text)
    okt = Okt()  # 형태소 추출
    Nnouns = okt.nouns(result)
    Nnouns = [x for x in Nnouns if len(x) > 1]  # 한글자 키워드 제거
    Nnouns = [x for x in Nnouns if x not in stopwords]  # 불용어 제거
    return Nnouns

class SimpleGroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)

class GroupedColorFunc(object):
    """Create a color function object which assigns DIFFERENT SHADES of
       specified colors to certain words based on the color to words mapping.

       Uses wordcloud.get_single_color_func

       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.

       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

def color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(180,220),np.random.randint(95,110),np.random.randint(70,90)))


with open('coef_pos_index1.txt', 'r', encoding='utf-8') as f:
    atext = f.read()

okt = Okt()
nouns = okt.nouns(atext) # 명사만 추출
color_to_words={'#9CDFFF':nouns}

# print(color_to_words)
new_text = []
new_reviews = []
words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외
for i in range(len(lottetext)):
     new_text+=text_cleaning(lottetext[i])
for a in range(len(new_text)):
    if new_text[a] in words:
        new_reviews.append(new_text[a])
print(new_reviews)

c = Counter(new_reviews) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함

print(c)

wc = WordCloud(font_path=r"C:\\Windows\\Fonts\\malgun.ttf",background_color='white', #배경색
                       width=800, height=600, scale=2.0, max_font_size=250)

gen = wc.generate_from_frequencies(c)
gen = wc.recolor(color_func=color_func)
plt.figure()
plt.axis('off') # 눈금을 제거해주는 옵션
plt.imshow(gen)

wc.to_file('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/몬드리안긍정리뷰.png')

with open('coef_neg_index1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

okt = Okt()
nouns = okt.nouns(text) # 명사만 추출


new_text2 = []
new_reviews2 = []
words2 = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외
for i in range(len(lottetext)):
     new_text2+=text_cleaning(lottetext[i])
for a in range(len(new_text)):
    if new_text2[a] in words2:
        new_reviews2.append(new_text[a])
print(new_reviews2)

def color_func2(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(300,350),np.random.randint(95,110),np.random.randint(40,60)))

c = Counter(new_reviews2) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함

wc = WordCloud(font_path=r"C:\\Windows\\Fonts\\malgun.ttf",background_color='white', #배경색
                       width=800, height=600, scale=2.0, max_font_size=250)

gen = wc.generate_from_frequencies(c)
gen = wc.recolor(color_func=color_func2)
plt.figure()
plt.axis('off') # 눈금을 제거해주는 옵션
plt.imshow(gen)

wc.to_file('C:/Users/seong-il/Desktop/대학교/4-1/텍스트마이닝/textmining/routes/몬드리안부정리뷰.png')


newwords = new_reviews+new_reviews2
color_to_words['#FF0C88'] = nouns
# print(color_to_words)

c = Counter(newwords) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함

grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)

wc = WordCloud(font_path=r"C:\\Windows\\Fonts\\malgun.ttf",background_color='white', #배경색
                       width=800, height=600, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
gen = wc.recolor(color_func=grouped_color_func)

plt.figure()
plt.axis('off') # 눈금을 제거해주는 옵션
plt.imshow(gen)


wc.to_file('롯데 합친거.png')


print("true")