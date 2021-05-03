from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
def getText():
    txt=open("res.txt","r",encoding='utf-8').read()
    print(txt)
    txt=txt.lower()
    for ch in '|"#$%&()*+,-./:;<>+?@[\\]^_{|}~':
        txt=txt.replace(ch," ")
    return txt
harmTxt=getText()
words=harmTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
#按照第二个元素有大到小排序
items.sort(key=lambda  x:x[1],reverse=True)
words_dict = {}
for i in range(10):
    word, count=items[i]
    words_dict[word] = count
    print(word,end=":")
    print(count)
print(words_dict)
txt=open("res.txt","r",encoding='utf-8').read()
wordcloud = WordCloud().generate(txt)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()


