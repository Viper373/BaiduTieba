import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# 假设你的CSV文件名为data.csv，并且包含post_title和post_content两列
csv_file = './data/百度贴吧——HOT.csv'

# 停用词列表，这里只给出一个简单的例子，实际应用中可能需要更全面的停用词库
# 读取停用词
with open('./data/chinese.txt', 'r', encoding='utf-8') as f:
    stopwords = [line.strip() for line in f]


def process_text(text):
    """分词并过滤停用词"""
    words = jieba.lcut(text)
    return ' '.join(word for word in words if word not in stopwords)


def read_and_process_csv(file_path):
    """多线程读取CSV并处理文本"""
    df = pd.read_csv(file_path)
    text_list = []

    def update_progress(current, total, pbar):
        pbar.update(1)

    with ThreadPoolExecutor() as executor, tqdm(total=len(df), desc="Processing CSV") as pbar:
        futures = {executor.submit(process_text, str(df.loc[i, 'post_title'])
                                   + ' '
                                   + str(df.loc[i, 'post_content'])): i for i in range(len(df))}
        for future in futures:
            result = future.result()
            text_list.append(result)
            update_progress(futures[future], len(df), pbar)

    return ' '.join(text_list)


# 读取并处理CSV
combined_text = read_and_process_csv(csv_file)

# 生成词云
wordcloud = (WordCloud(font_path='simhei.ttf', background_color='white', width=1366, height=768)
             .generate(combined_text))
# 保存词云到本地文件
wordcloud.to_file('./data/wordcloud.png')
# 显示词云
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
