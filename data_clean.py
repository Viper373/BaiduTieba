import pandas as pd

# 读取csv文件
df = pd.read_csv('data\百度贴吧——大学吧.csv')

# 尝试将post_reply_count列转换为整数类型，无法转换的转换为NaN
df['post_reply_count'] = pd.to_numeric(df['post_reply_count'], errors='coerce', downcast='integer')
# 删除转换后仍为NaN的行（即转换失败的行）
df = df.dropna(subset=['post_reply_count'])

df['post_reply_count'] = df['post_reply_count'].astype(int, errors='ignore')
# 筛选出post_reply_count大于10的行
filtered_data = df[df['post_reply_count'] > 10]

# 保存到新文件
filtered_data.to_csv('data\百度贴吧——HOT.csv', index=False)