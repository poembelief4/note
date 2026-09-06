# 矩阵

$\mathbf{A}\in\mathbb{R}^{m\times n}$ 表示矩阵 $\mathbf{A}$ 由 $m$ 行和 $n$ 列的实值标量构成，即形状是 $(m,n)$ 或 $m\times n$。若 $n=m$，则其被称为**方阵**。

若交换矩阵的行和列，则其结果被称为矩阵的**转置**，通常用 $\mathbf{A}^\top$ 来表示。若 $\mathbf B =\mathbf A^\top$，则有：$b_{ij}=a_{ji}$。

若 $\mathbf A=\mathbf A^\top$​，则该矩阵为**对称矩阵**。

# 矩阵-向量积

假定 $\mathbf A\in\mathbb R^{m\times n},\mathbf x\in\mathbb R^n$，我们用行向量来表示矩阵 $\mathbf A$：
$$
\mathbf A=
\begin{bmatrix}
	\mathbf a_1^\top\\
	\mathbf a_2^\top\\
	\vdots\\
	\mathbf a_m^\top
\end{bmatrix}
$$
其中，$\mathbf{a_i^\top}\in\mathbb R^n$ 都是行向量，表示矩阵的第 $i$ 行。

矩阵向量积 $\mathbf{Ax}$ 是一个长度为 $m$ 的列向量，其第 $i$ 个元素是点积 $\mathbf{a_i^\top x}$：
$$
\mathbf{Ax}=
\begin{bmatrix}
	\mathbf a_1^\top\\
	\mathbf a_2^\top\\
	\vdots\\
	\mathbf a_m^\top
\end{bmatrix}
\mathbf{x}=
\begin{bmatrix}
	\mathbf{a_1^\top x}\\
	\mathbf{a_2^\top x}\\
	\vdots\\
	\mathbf{a_m^\top x}\\
\end{bmatrix}
$$
可以通过一个矩阵 $\mathbf A\in\mathbb R^{m\times n}$ 来实现从 $\mathbb R^n$ 到 $\mathbb R^m$ 向量的转换。

# 矩阵-矩阵乘法

假设有两个矩阵 $\mathbf A\in \mathbb R^{n\times k},\mathbf B\in \mathbb R^{k\times m}$：
$$
\mathbf A=
\begin{bmatrix}
	a_{11}&a_{12}&\dots&a_{1k}\\
	a_{21}&a_{22}&\dots&a_{2k}\\
	\vdots&\vdots&\ddots&\vdots\\
	a_{n1}&a_{n2}&\dots&a_{nk}\\
\end{bmatrix}
,\qquad
\mathbf B=
\begin{bmatrix}
	b_{11}&b_{12}&\dots&b_{1m}\\
	b_{21}&b_{22}&\dots&b_{2m}\\
	\vdots&\vdots&\ddots&\vdots\\
	b_{k1}&b_{k2}&\dots&b_{km}\\
\end{bmatrix}
$$
行向量 $\mathbf a_i^\top\in\mathbb R^k$ 表示矩阵 $\mathbf A$ 的第 $i$ 行，列向量 $b_j\in\mathbb R^k$ 表示矩阵 $\mathbf B$ 的第 $j$ 列。

对于矩阵积 $\mathbf C=\mathbf{AB}$，考虑前者的行向量和后者的列向量，即每个元素 $c_{ij}$ 的值为点积 $\mathbf a_i^\top\mathbf b_j$：
$$
\mathbf C=\mathbf{AB}=
\begin{bmatrix}
	\mathbf a_1^\top\\
	\mathbf a_2^\top\\
	\vdots\\
	\mathbf a_n^\top\\
\end{bmatrix}
\begin{bmatrix}
	\mathbf b_1&\mathbf b_2&\dots&\mathbf b_m
\end{bmatrix}
=
\begin{bmatrix}
	\mathbf a_1^\top \mathbf b_1&\mathbf a_1^\top \mathbf b_2&\dots&\mathbf a_1^\top \mathbf b_m\\
	\mathbf a_2^\top \mathbf b_1&\mathbf a_2^\top \mathbf b_2&\dots&\mathbf a_2^\top \mathbf b_m\\
	\vdots&\vdots&\ddots&\vdots\\
	\mathbf a_n^\top \mathbf b_1&\mathbf a_n^\top \mathbf b_2&\dots&\mathbf a_n^\top \mathbf b_m\\
\end{bmatrix}
$$
可以把矩阵-矩阵乘法看作执行 $m$ 次矩阵-向量积，并把结果拼接在一起，形成一个 $n\times m$ 矩阵。

矩阵-矩阵乘法可以简单地称为**矩阵乘法**。

# 张量

张量是描述具有任意数量轴的数组的通用方式，标量是零阶张量，向量是一阶张量，矩阵是二阶张量。

# 张量算法的基本性质

任何按元素的一元运算都不会改变其操作数的形状；对于两个形状相同的张量，按元素二元运算的结果也是相同形状的张量。

两个矩阵的按元素乘法称为 Hadamard 积，用 $\odot$ 表示。

例如：矩阵 $\mathbf A$ 和 $\mathbf B$ 的 Hadamard 积为：
$$
\mathbf A \odot \mathbf B=\begin{bmatrix}
	a_{11}b_{11}&a_{12}b_{12}&\cdots&a_{1n}b_{1n}\\
	a_{21}b_{21}&a_{22}b_{22}&\cdots&a_{2n}b_{2n}\\
	\vdots&\vdots&\ddots&\vdots\\
	a_{m1}b_{m1}&a_{m2}b_{m2}&\cdots&a_{mn}b_{mn}
\end{bmatrix}
$$
将张量乘以或加上一个标量不会改变张量的形状，其中张量的每个元素都会和标量相加或相乘。