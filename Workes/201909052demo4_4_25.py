import jieba
import numpy as np
from PIL import Image
import wordcloud
# 获取文本函数
from matplotlib import pyplot as plt
from wordcloud import WordCloud


def getText():
    txt = open("res.txt", "r", encoding='utf-8').read()
    txt = txt.lower()
    for ch in '|"#$%&()*+,-./:;<>+?@[\\]^_{|}~':
        txt = txt.replace(ch, " ")
    return txt
# 打印关键词
def printKeyWord(res):
    res = getText()
    words = res.split()
    # print(words)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
def printKeyWordPlus(res):
    excludes = {"the","and","of","you","a","i","my","in"}
    res = getText()
    words = res.split()
    # print(words)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    for word in excludes:
        del (counts[word])
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))

def calThreeKingdom():
    txt = open("三国演义.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(15):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))

def fun2(txt):
    # 生成对象

    # mask = np.array(Image.open("1.jfif"))
    wc = WordCloud( font_path='FRSCRIPT.TTF', mode='RGBA', background_color=None).generate(str(txt))

    # 显示词云
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('2.jpg')
    plt.show()

    # 保存到文件

    # wc.to_file('2.jpg')
if __name__ == '__main__':
    res = getText()
    fun2(res)
    printKeyWord(res)
    print('*'*20)
    printKeyWordPlus(res)
    calThreeKingdom()
