#!/usr/bin/env python
# coding: utf-8

import re
from konlpy.tag import Komoran
from collections import Counter
from wordcloud import WordCloud


def get_nouns(txt):
    txt = re.sub('[-=.*#/!?:$}]', '', txt)
    tokenizer = Komoran()
    nouns = tokenizer.nouns(txt)
    result = []
    stop_words = ["이제", "대해", "관련", "다시", "하라", "시오", "대한", "위해",
                  "및", "두기", "저희", "제발", "바로", "동안", "정말", "경우", "제대로", "당장"]
    for w in nouns:
        if w not in stop_words:
            result.append(w)
    for i, v in enumerate(result):
        if len(v) < 2:
            result.pop(i)
    count = Counter(result)
    noun_list = count.most_common(50)  # 빈도수 기준 조정
    return noun_list


def visualize(noun_list, category):
    wc = WordCloud(font_path="./font/A옛날목욕탕L.TTF",
                   background_color='white', width=1000, height=1000, max_words=100, max_font_size=300)
    wc.generate_from_frequencies(dict(noun_list))
    wc.to_file('./static/wordCloud_'+category+'.png')
