#!/usr/bin/python                                                                                                                                                                                                                
# coding=utf-8

# Describe :定义Word类的结构；定义Tagger类，实现自然语言转为Word对象的方法。

import jieba
import jieba.posseg as psg

class Word:
    def __init__(self, token, pos):
        self.token = token  # 分词
        self.pos = pos  # 词性

class Tagger:
    def __init__(self, dict_paths):
        for p in dict_paths:
            jieba.load_userdict(p)  # 加载外部词典
            # TODO jieba不能正确切分的词语，我们人工调整其频率。
            # jieba.suggest_freq(('喜剧', '电影'), True)
            # jieba.suggest_freq(('恐怖', '电影'), True)
            # jieba.suggest_freq(('科幻', '电影'), True)
            # jieba.suggest_freq(('喜剧', '演员'), True)
            # jieba.suggest_freq(('出生', '日期'), True)
            # jieba.suggest_freq(('英文', '名字'), True)

    def get_word_objects(self, sentence):
        #print([word for word in psg.cut(sentence)])
        return [Word(word, tag) for word, tag in psg.cut(sentence)]  #分词，获取单词与词性