import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

z=np.array([-2,-1,0,1,2],dtype=float)

probabilities=sigmoid(z)

print("线性得分：",z)
print("预测概率：",probabilities)

y_true=np.array([1,0,1,1,0,0,1,0,1,0],dtype=int)
y_prob=np.array(
    [0.95, 0.85, 0.75, 0.65, 0.55, 
     0.45, 0.35, 0.25, 0.15, 0.05],
     dtype=float
     )

def predict_class(y_prob,threshold):
    return (y_prob>=threshold).astype(int)

y_pred=predict_class(y_prob,0.5)
print(y_pred)

def confusion_counts(y_true,y_pred):
    tp=np.sum((y_true==1)&(y_pred==1))
    fp=np.sum((y_true==0)&(y_pred==1))
    fn=np.sum((y_true==1)&(y_pred==0))
    tn=np.sum((y_true==0)&(y_pred==0))
    assert tp+fp+tn+fn==len(y_true)
    return tp,fp,fn,tn

def calculate_metrics(tp,fp,fn,tn):
    total=tp+fp+fn+tn
    accuracy=(tp+tn)/total
    precision=(
        tp/(tp+fp)
        if tp+fp>0
        else 0
    )
    recall=(
        tp/(tp+fn)
        if tp+fn>0
        else 0
    )
    return accuracy,precision,recall

thresholds=[0.3,0.5,0.7]
for threshold in thresholds:
    y_pred=predict_class(y_prob,threshold)
    tp,fp,fn,tn=confusion_counts(y_true,y_pred)
    accuracy,precision,recall=calculate_metrics(tp,fp,fn,tn)

    print("阈值：",threshold)
    print("预测类别：",y_pred)
    print("TP、FP、FN、TN：",tp,fp,fn,tn)
    print("准确率：",accuracy)
    print("精确率",precision)
    print("召回率",recall)