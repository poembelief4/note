# 标量

仅包含一个数值的量被称为**标量**。标量由只有一个元素的张量表示。

# 向量

向量可以被视为标量值组成的列表，这些标量值被称为向量的**元素**或**分量**。

# 向量的长度、维度和形状

向量是数字数组，而数字数组是有**长度**的。

在数学表示法中，若一个向量 $\mathbf{x}$ 由 $n$ 个实值标量组成，可以将其表示为 $\mathbf{x}\in \mathbb{R}^n$。

向量的长度通常称为向量的**维度**。

**形状**是一个元素组，列出了张量沿每个轴的长度（维度）。

# 点积

给定两个向量 $\mathbf{x},\mathbf{y}$ $\in \mathbb{R}^d$，它们的点积为 $\mathbf{x}^\top\mathbf{y}$（或 $\langle\mathbf x,\mathbf y\rangle$），指相同位置的按元素乘积的和：
$$
\mathbf x ^\top \mathbf y=\sum^d_{i=1} x_iy_i
$$


# $L_2$ 范数

向量的**范数**是表示向量大小（不涉及维度，而是分量的大小）。

向量范数是将向量映射到标量的函数 $f$。

对于向量范数，需要满足一些性质：

- 如果我们按常数因子 $\alpha$ 缩放向量的所有元素，其范数也会按相同常数因子的**绝对值**缩放：$f(\alpha \mathbf x)=|\alpha|f(\mathbf x)$。
- 满足三角不等式：$f(\mathbf x+\mathbf y)\le f(\mathbf x)+f(\mathbf y)$。
- 范数必须是非负的：$f(\mathbf x)\ge 0$，且 $f(\mathbf{x})=0\Longleftrightarrow \mathbf{x}=\mathbf{0}$

假设 $n$ 维向量 $\mathbf x$ 中的元素是 $x_1,\dots,x_n$，其 $L_2$ 范数是向量元素平方和的平方根：
$$
\|\mathbf x\|=\|\mathbf{x}\|_2=\sqrt{\sum^n_{i=1}x_i^2}
$$
与 $L_2$ 范数相比，$L_1$ 范数受异常值的影响较小。

# 余弦相似度

$$
\mathbf a \cdot \mathbf b=\|\mathbf a\|_2\|\mathbf b\|_2\cos\theta
\Longrightarrow \cos\theta=\frac{\mathbf a\cdot\mathbf b}{\|\mathbf a\|_2\|\mathbf b\|_2}
$$

得到的 $\cos\theta$ 就是**余弦相似度**，这样可以消除向量长度的影响，主要比较方向。

余弦相似值通常位于 $[-1,1]$，接近 1 表示方向相近，接近 0 表示近似垂直，近似 -1 表示方向相反。

零向量不能计算余弦相似度，因为 $\|\mathbf 0\|_2=0$，会导致分母为 0。