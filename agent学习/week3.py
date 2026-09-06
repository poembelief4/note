import numpy as np

x=np.array([1,2,3,4,5],dtype=float)
y=np.array([52,57,65,73,80],dtype=float)
w=5
b=45

def predict(x,w,b):
    return x*w+b

def mse(y,y_pre):
    return np.mean((y_pre-y)**2)

y_pre=predict(x,w,b)
print("初始参数的训练MSE：",mse(y,y_pre))

ans_b=b
ans_w=w
ans_MSE=mse(y,y_pre)
for b in range(40,51):
    for w in range(4,10):
        y_pre=predict(x,w,b)
        MSE=mse(y,y_pre)
        if MSE<ans_MSE:
            ans_b=b
            ans_w=w
            ans_MSE=MSE
print("最佳参数的训练MSE：",ans_MSE)
print("最佳参数的训练集预测值：",predict(x,ans_w,ans_b))

x_test=np.array([6,7,8],dtype=float)
y_test=np.array([87,94,102],dtype=float)
w=5
b=45

print("初始参数的测试MSE：",mse(y_test,predict(x_test,w,b)))
print("最佳参数的测试MSE：",mse(y_test,predict(x_test,ans_w,ans_b)))
print("最佳参数的测试集预测值：",predict(x_test,ans_w,ans_b))
