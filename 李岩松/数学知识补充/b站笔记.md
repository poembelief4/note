# 特征值，谱分解，奇异值分解

## 特征值、特征向量

线性映射有两种情况：放缩和旋转。

放缩的线性映射相当于乘以了一个对角矩阵（diagonal matrix）。

旋转的线性映射相当于乘以了一个正交矩阵（orthogonal matrix）：
$$
\begin{aligned}
&<Rv_1,Rv_2>=<v_1,v_2>\\
&\Rightarrow v_1^\top R^\top Rv_2=v_1^\top v_2\\
&\Rightarrow R^\top R=I\\
&\Rightarrow R^{-1}=R^\top
\end{aligned}
$$
直觉可以发现：旋转比放缩复杂。所以我们可以考虑只研究放缩，即：
$$
Av=\lambda v,\lambda\in \mathbb R
$$
那么，$\lambda$ 被称为特征值，$x$ 被称为特征向量。

## 谱分解

==向量是独立于坐标系存在的==，所以坐标系发生改变后，向量是没有发生改变，改变的是坐标。

假设有一个 $n\times n$ 的**对称矩阵** $A$ 有 $n$ 个特征值和特征向量，那么我们可以选择一组 $n$ 个特征向量，满足：

1. $<v_i,v_j>=\delta_{i,j}$，即二者互相垂直（$\delta$ 表示：如果 $i=j$，那么是 $1$，否则是 $0$）。所以这些特征向量张成了 $\R^n$，我们也可以得到：

$$
\begin{aligned}
x&=q_1v_1+q_2v_2+\dots+q_nv_n,q_n\in\R\\
Ax&=q_1Av_1+q_2Av_2+\dots+q_nAv_n\\
&=\lambda_1q_1v_1+\lambda_2q_2v_2+\dots+\lambda_3q_3v_3
\end{aligned}
$$

定义矩阵 $Q$ 由单位特征向量组成，即 $Q\triangleq\set{v_1|v_2|\dots|v_n}$，那么：

- $Q^{-1}x_e$ 表示向量 $x$ 在由单位特征向量组成的坐标系下的新坐标 $S'$。

- $\Lambda Q^{-1}x_e$ 表示经过了放缩后的新坐标 $S'$。
- $Q\Lambda Q^{-1}x_e$ 表示向量 $x$ 先转化得到放缩后的新坐标 $S'$，再由 $S'$ 转化成标准坐标系下的坐标 $S''$。

因为 $Q$ 是正交矩阵，所以 $Q^{-1}=Q^\top$，因此我们可以得到：
$$
A\cdot x_e=Q\Lambda Q^\top\cdot x_e\Rightarrow A=Q\Lambda Q^\top
$$
因此实矩阵 $A$ 都可以被拆分成 $Q\Lambda Q^\top$，这个过程就是谱分解。

## 奇异值分解

考虑非方阵的矩阵的分解。

在方阵中，$Ax=\lambda x$，故向量的空间是没有发生改变的。

而在非方阵中，$Av=\sigma u_i$，$v,u_i$ 所属的空间是不一样的。

# 对矩阵函数求导

单层神经网络的函数可以表示为 $f(x,A):=\phi(Ax)$，而其损失函数是 $\|f(x,A-y)\|^2$，我们需要做的就是求出：$min_{A\in\R^{n\times n}}\sum_{(x,y)\in \mathcal D}\|f(x,A)-y\|^2$。

那么，我们就需要求出：$\frac{\partial f(x,A)}{\partial A}$，因此就需要对矩阵函数求导。

对于函数 $f(x)=a^\top x,f'(x)=a$。

对于函数 $f(x)=Ax,f'(x)=A^\top$。

泰勒展开式：
$$
f(x+\Delta x)\approx f(x)+f'(x)\Delta x+h.o.t\\
f(X+\Delta X)\approx f(X)+Df(X)[\Delta X]+h.o.t
$$
$X\in \mathcal M$ 可以是矩阵、向量等任何东西。

$D$ 表示：$Df:\mathcal M\to \mathcal L(\mathcal M,\R)$。

$\mathcal L(\mathcal M,\R)$ 表示：输入类型为 $\mathcal M$、输出类型为 $\R$ 的函数的集合。 

所以，$X\in \mathcal M$，那么 $Df(X)\in \mathcal L(\mathcal M,\R)$；$\Delta X\in \mathcal M\Rightarrow Df(X)[\Delta X]\in \R$。

对于 $f(x)=Ax$，有：
$$
\begin{aligned}
	f(x+\Delta x)&=A(x+\Delta x)\\
	&=Ax+A\Delta x\\
	&=f(x)+A\Delta x
\end{aligned}
$$
结合泰勒展开式，我们可以知道：$Df(x)[\Delta x]=A\Delta x$。

结合线性变化，我们可以知道：对于函数操作 $\mathcal A\in\mathcal L(\R^n,\R^m)$， 我们总可以找到一个 $m\times n$ 的矩阵 $A$，使得：
$$
\mathcal A(x)=Ax
$$
因此，我们说 $Df(x)$ 是函数的梯度，且 $Df(x)=A$。

# 线性代数的本质

线性变换：把一条直线转换成另一条直线。

- 放缩（scaling），如 $f(x)=2x$。
- 旋转（rotation），这用一维的函数难以描述。

每一个二维空间中的向量都可以被写成基向量 $\set{e_1,e_2}$ 的线性组合：
$$
x\in\R^2\Leftrightarrow x=x_1e_1+x_2e_2=[e_1\mid e_2]\begin{bmatrix}x_1\\x_2\end{bmatrix}\\
x_1,x_2\in\R
$$
在有限维度下，我们可以把线性变换的过程，等价于每个点的坐标值都和一个矩阵相乘；将多个线性变化的结果，等价于多个矩阵相乘后再与坐标相乘。
