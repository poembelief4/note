# 导数和微分

对于每个参数，如果我们把这个参数增加或减少一个**尽可能小**的量，就可以知道损失会以多快的速度增加或减少。

对于一个定义域和值域都是 $\mathbb R$ 且输入和输出都是标量的函数 $f$，如果其导数存在，则这个极限被定义为：
$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}
$$
如果 $f'(a)$ 存在，则称 $f$ 在 $a$ 处是可微的。如果 $f$ 在一个区间内的每个数上都是可微的，则此函数在此区间中是可微的。
$$
f'(x)=y'=\frac{dy}{dx}=\frac{df}{dx}=\frac{d}{dx}f(x)=Df(x)=D_xf(x)
$$
其中 $\frac{d}{dx}$ 和 $D$ 是微分运算符，表示微分操作。有以下规则对常见函数求微分：

- $DC=0$（$C$ 是一个常数）。
- $Dx^n=nx^{n-1}$（幂律，$n$ 是任意实数）。
- $De^x=e^x$。
- $D\ln(x)=\frac{1}{x}$。

为了微分一些复合函数，假设函数 $f,g$ 都是可微的，$C$ 是一个常数，有以下法则：

- 常数相乘法则：$\frac{d}{dx}[Cf(x)]=C\frac{d}{dx}f(x)$。

- 加法法则：$\frac{d}{dx}[f(x)+g(x)]=\frac{d}{dx}f(x)+\frac{d}{dx}g(x)$。
- 乘法法则：$\frac{d}{dx}[(f(x)g(x))]=f(x)\frac{d}{dx}[g(x)]+g(x)\frac{d}{dx}[f(x)]$。
- 除法法则：$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]=\frac{g(x)\frac{d}{dx}[f(x)]-f(x)\frac{d}{dx}[g(x)]}{[g(x)]^2}$。

# 偏导数

设 $y=f(x_1,x_2,\dots,x_n)$ 是一个具有 $n$ 个变量的函数，$y$ 关于第 $i$ 个参数 $x_i$ 的偏导数为：
$$
\frac{\partial y}{\partial x_i}=\lim_{h\to 0}\frac{f(x_1,\dots,x_{i-1},x_i+h,x_{i+1},\dots,x_n)-f(x_1,\dots,x_i,\dots,x_n)}{h}
$$
为了计算 $\frac{\partial y}{\partial x_i}$，可以把其他变量看作常数，然后计算 $y$ 关于 $x_i$ 的导数。对于偏导数的表示，以下是等价的：
$$
\frac{\partial y}{\partial x_i}=\frac{\partial f}{\partial x_i}=f_{x_i}=f_i=D_if=D_{x_i}f
$$

# 梯度

把一个多元函数对其各个变量的偏导数按顺序排列，就得到了该函数的**梯度**向量。

令 $f$ 为输入是 $n$ 维向量 $\mathbf x=[x_1,x_2,\dots,x_n]^\top$、输出是标量的函数，则其相对于 $\mathbf x$ 的梯度是一个包含 $n$ 个偏导数的向量：
$$
\nabla_{\mathbf x}f(\mathbf x)=\left[\frac{\partial f(\mathbf x)}{\partial x_1},\frac{\partial f(\mathbf x)}{\partial x_2},\dots,\frac{\partial f(\mathbf x)}{\partial x_n}\right]^\top
$$
在没有歧义时，通常用 $\nabla f(\mathbf x)$ 表示。

假设 $\mathbf x$ 为 $n$ 维向量，在微分多元函数时通常会使用以下规则：

- 对于所有 $\mathbf A\in\mathbb R^{m\times n}$，都有 $\nabla_{\mathbf x}\mathbf{Ax}=\mathbf{A^\top}$
- 对于所有 $\mathbf A\in \mathbb R^{n\times m}$，都有 $\nabla_{\mathbf x}\mathbf{x^\top A}=\mathbf A$
- 对于所有 $\mathbf A\in\mathbb R^{n\times n}$，都有 $\nabla_{\mathbf x}\mathbf{x^\top Ax}=(\mathbf{A}+\mathbf{A^\top})\mathbf x$
- $\nabla_\mathbf x \|\mathbf{x}\|^2=\nabla_{\mathbf x}\mathbf {x^\top x}=2\mathbf x$

对于任意矩阵 $\mathbf X$，都有 $\nabla_{\mathbf X}\|\mathbf X\|^2_F=2\mathbf X$。

# 链式法则

链式法则可以用于微分复合多元函数。

对于单变量函数：假设 $y=f(u)$ 和 $u=g(x)$ 都是可微的，根据链式法则：
$$
\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}
$$
当函数具有任意数量的变量时：假设可微分函数 $y$ 有变量 $u_1,u_2,\dots,u_m$，其中每个可微分的函数 $u_i$ 都有变量 $x_1,x_2,\dots,x_n$（注意，$y$ 是 $x_1,x_2,\dots,x_n$ 的函数），对于任意 $i=1,2,\dots,n$，由链式法则可知：
$$
\frac{\partial y}{\partial x_i}=\frac{\partial y}{\partial u_1}\frac{\partial u_1}{\partial x_i}+\frac{\partial y}{\partial u_2}\frac{\partial u_2}{\partial x_i}+\dots+\frac{\partial y}{\partial u_m}\frac{\partial u_m}{\partial x_i}
$$
