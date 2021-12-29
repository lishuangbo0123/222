# 李双博
# 学习python
# 开发时间 2021/12/28  23:57


import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from imageio import imread

# 读取数据
text = open('ciyun.txt', 'r', encoding='utf-8').read()
# 读取停用词，创建停用词表
stwlist = [line.strip() for line in open ('stopwords.txt', encoding = 'utf-8').readlines()]
print(stwlist)
# 分词
words = jieba.cut(text, cut_all=False, HMM=True)

# 文本清洗
mytext_list = []
for seg in words:
    if seg not in stwlist and seg != " " and len(seg) != 1:
        mytext_list.append(seg.replace(" ", ""))
cloud_text = ",".join(mytext_list)

# 读取背景图片
jpg = imread('ciyun.jfif')
# 生成词云
wordcloud = WordCloud(
mask = jpg,
background_color = "white",
font_path = 'simhei.ttf',
width = 1500,
height = 960,
margin = 10
).generate(cloud_text)
# font_path='simhei.ttf' 这个参数为指定字体

# 绘制图片
plt.imshow(wordcloud)
# 去除坐标轴
plt.axis("off")
plt.show()