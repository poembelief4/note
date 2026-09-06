import numpy as np

X=np.array([
    [2,1],
    [0,3],
    [4,2]
],dtype=float)

w=np.array([2,-1],dtype=float)

print("矩阵的形状为：",X.shape)
print("向量的形状为：",w.shape)

assert X.ndim==2
assert w.ndim==1
assert X.shape[1]==w.shape[0]

predictions=X@w# @表示矩阵乘法，*表示对应元素相乘，np.matmul(X,w)也可以实现矩阵乘法

assert predictions.shape==(X.shape[0],)

print("矩阵乘法结果为：",predictions)
print("矩阵乘法结果的形状为：",predictions.shape)

individual_predictions=np.array([
    X[0]@w,
    X[1]@w,
    X[2]@w
])

print("逐个计算结果：",individual_predictions)

assert np.allclose(predictions,individual_predictions)

W=np.array([
    [2,1],
    [-1,3]
],dtype=float)

multi_prediction=X@W

print("参数矩阵的形状：",W.shape)
print("多输出预测结果：\n",multi_prediction)
print("多输出预测结果的形状：",multi_prediction.shape)

assert W.ndim==2
assert X.shape[1]==W.shape[0]
assert multi_prediction.shape==(X.shape[0],W.shape[1])