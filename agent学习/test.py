import pandas as pd
data = [
    [1, "一元二次方程怎么求解？", 0, 0, 0],
    [2, "北京今天的天气怎么样？", 1, 1, 1],
    [3, "什么是机器学习？", 0, 0, 0],
    [4, "现在黄金价格是多少？", 1, 1, 1],
    [5, "请计算125乘以48", 0, 0, 0],
    [6, "最新的人工智能新闻有哪些？", 1, 1, 1],
    [7, "正态分布是什么意思？", 0, 0, 0],
    [8, "上海明天会下雨吗？", 1, 1, 1],
    [9, "Python中的列表是什么？", 0, 0, 0],
    [10, "目前的世界首富是谁？", 1, 1, 1],
    [11, "三角函数有哪些基本公式？", 0, 0, 0],
    [12, "今天人民币对美元汇率是多少？", 1, 1, 1],
    [13, "过拟合是什么意思？", 0, 0, 0],
    [14, "最近有什么新上映的电影？", 1, 1, 1],
    [15, "如何读取CSV文件？", 0, 0, 0],
    [16, "本周末杭州天气怎么样？", 1, 1, 1],
    [17, "什么是训练集？", 0, 0, 0],
    [18, "查询今天的A股指数", 1, 1, 1],
    [19, "勾股定理是什么？", 0, 0, 0],
    [20, "最新版本的Python是多少？", 1, 1, 1],
]

columns=[
    "id",
    "question",
    "has_latest_word",
    "has_current_info",
    "need_web"
]

df=pd.DataFrame(data,columns=columns)

shuffled=df.sample(frac=1,random_state=42).reset_index(drop=True)

train_df=shuffled.iloc[:16]
test_df=shuffled.iloc[16:]

train_df.to_csv("train.csv",index=False,encoding="utf-8-sig")
test_df.to_csv("test.csv",index=False,encoding="utf-8-sig")

print("训练集数量：",len(train_df))
print("测试集数量：",len(test_df))

overlap=set(train_df["id"])&set(test_df["id"])
print("重复的样本ID：",overlap)