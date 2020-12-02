#!/usr/bin/env python
# coding: utf-8

import kss
from gensim.summarization.summarizer import summarize  # textrank


def summarization(txt):
    segment = []
    for sent in kss.split_sentences(txt):  # 품사 분석을 통한 분리
        if "." in sent[0:-1]:  # 문장 내 불필요한 온점은 삭제
            sent = sent.replace(".", "")
        if sent[-1] in [".", "?", "!"]:  # 마침표 유무에 따라 구분
            sent = sent
        else:
            sent = sent + "."  # 분리된 문장 끝에 온점 부여
        segment.append(sent)
    if len(segment) <= 10:
        result = " ".join(segment).replace("\n", "")  # 문장 내 enter 제거
    else:
        # \n 처리
        # 요약된 문장 수 조정
        seg_str = " ".join(segment).replace("\n", "")
        result = summarize(seg_str, ratio=0.15, word_count=80)
    return result
