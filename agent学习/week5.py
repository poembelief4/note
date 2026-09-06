import numpy as np
def dot_product(a,b):
    assert a.shape==b.shape,"两个向量的形状必须相同"

    products=a*b
    result=np.sum(products)
    return result

def l2_norm(a):
    squares=a**2
    sum_of_squares=np.sum(squares)
    result=np.sqrt(sum_of_squares)

    return result

def cosine_similarity(a,b):
    assert a.shape==b.shape,"两个向量的形状必须相同"

    norm_a=l2_norm(a)
    norm_b=l2_norm(b)

    if norm_a==0 or norm_b==0:
        raise ValueError("零向量不能计算余弦相似度")

    similarity=dot_product(a,b)/(norm_a*norm_b)

    return similarity

a=np.array([1,2],dtype=float)
b=np.array([3,4],dtype=float)

print("点积：",dot_product(a,b))
print("a的L2范数：",l2_norm(a))
print("b的L2范数：",l2_norm(b))
print("余弦相似度：",cosine_similarity(a,b))

c=np.array([1,0],dtype=float)
d=np.array([0,1],dtype=float)

e=np.array([1,2],dtype=float)
f=np.array([-1,-2],dtype=float)

print("垂直向量：",cosine_similarity(c,d))
print("反向向量：",cosine_similarity(e,f))

texts = [
    "机器 学习 模型",
    "深度 学习 模型",
    "模型 使用 向量",
    "向量 计算 相似度",
    "足球 比赛 进球",
    "球队 赢得 比赛",
    "天气 温度 上升",
    "今天 天气 下雨",
    "Agent 调用 工具",
    "工具 帮助 Agent"
]

vocabulary_set=set()

for text in texts:
    words=text.split()# 根据空格拆分词语
    for word in words:
        vocabulary_set.add(word)

vocabulary=sorted(vocabulary_set)

print("词汇表：",vocabulary)
print("词汇数量：",len(vocabulary))

def text_to_vector(text,vocabulary):
    words=text.split()
    vector=[]

    for word in vocabulary:
        count=words.count(word)
        vector.append(count)

    return np.array(vector,dtype=float)

first_vector=text_to_vector(texts[0],vocabulary)

print("第一条文本：",texts[0])
print("第一条文本的向量：",first_vector)
print("向量维度：",first_vector.shape)

query_vector=text_to_vector(texts[0],vocabulary)
results=[]

for index in range(1,len(texts)):
    current_vector=text_to_vector(
        texts[index],
        vocabulary
    )
    similarity=cosine_similarity(
        query_vector,
        current_vector
    )
    results.append((similarity,index))

results.sort(reverse=True)

for similarity,index in results:
    print(
        texts[index],
        "相似度：",
        round(similarity,3)
    )