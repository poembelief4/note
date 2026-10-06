import numpy as np

def generate_matrices(n,seed):
    tmp=np.random.default_rng(seed)

    A=tmp.standard_normal((n,n))
    P=A.T@A

    Z=tmp.standard_normal((n,n))
    U,_=np.linalg.qr(Z)

    eigen_value=tmp.uniform(0.1,0.9,size=n)
    eigen_value[-1]=1.0

    Q=U@np.diag(eigen_value)@U.T

    return P,Q

def f_hat(x,P,c1):
    return 0.5*c1*(x.T@P@x)

def grad_f_hat(x,P,c1):
    return c1*(P@x)

def residual(x,Q,c2,c3):
    tmp=x-c3
    return 0.5*c2*(tmp.T@Q@tmp)

def grad_residual(x,Q,c2,c3):
    return c2*(Q@(x-c3))

def total(x,P,Q,c1,c2,c3):
    return f_hat(x,P,c1)+residual(x,Q,c2,c3)

def grad_total(x,P,Q,c1,c2,c3):
    return grad_f_hat(x,P,c1)+grad_residual(x,Q,c2,c3)

def find(P,Q,c1,c2,c3):
    A=c1*P+c2*Q
    b=c2*(Q@c3)

    return np.linalg.solve(A,b)

if __name__=="__main__":
    n=4
    c1=1.0
    c2=0.1
    c3=np.full(n,0.1)

    P,Q=generate_matrices(n,0)
    x_star=find(P,Q,c1,c2,c3)

    print("P 最小特征值：", np.linalg.eigvalsh(P).min())
    print("Q 最小特征值：", np.linalg.eigvalsh(Q).min())
    print("Q 最大特征值：", np.linalg.eigvalsh(Q).max())
    print("x*：", x_star)
    print(
        "最优点梯度范数：",
        np.linalg.norm(grad_total(x_star, P, Q, c1, c2, c3)),
    )