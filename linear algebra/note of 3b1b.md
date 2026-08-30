# vector basics

the fundamental, root-of-it-all building block for linear algebra.

linear algebra gives the data analyst a nice way to conceptualize many lists of numbers in a visual way, which can seriously clarify patterns in data and give a global view of what certain operations do.

## 3 distinct but related ideas about vectors

### physics student perspective

arrows pointing in space which are defined by its length and direction.

can be moved all around but still not change.

### computer science student perspective

ordered lists of numbers.

### mathematician perspective

vector can be anything where there's a sensible notion of adding two vectors and multiplying a vector by a number.

**vector addition and multiplication by numbers will play an important role throughout linear algebra**

## geometric focus

introduced a new topic involving vectors $\rightarrow$ think about an arrow inside a coordinate system, like the x-y plane, with its tail sitting at the origin.

every pair of numbers represents one and only one vector and every vector is associated with one and only one pair of numbers.

## two fundamental vector operations

### vector addition

To add two vectors, we should move the second one so that its tail sits at the tip of the first one.

Then, their sum is a new vector from the trail of the first one to where the tip of the second one now sits.

#### why do we define it like this?

##### geometric interpretation:

Each vector represents a certain movement, a step with a certain distance and direction in space. If you take a step along the first vector, then take a step in the direction and distance described by the second vector, the overall effect is just the same as if you moved along the sum of those two vectors to start with.

##### mathematic interpretation

We first do all of the rightward motion, then do all of the vertical motion.

sample: $(1,2) + (3,-1)$ means first move $(1+3)$ to the right then move $(2-1)$ up. So the new vector has coordinates $(1+3,2+(-1))=(4,1)$

**In general, vector addition in this "list of numbers" conception looks like matching up their terms and adding each one together.**

### multiplication by a number( or scalar multiplication)

**scaling**: the process of stretching or squishing or sometimes reversing the direction of a vector.

**scalar**: a number scaling some vector.

one of the main things that numbers do is scale vectors, so it's common to use the word "scalar" pretty much interchangeably with the word "number".

sample: $2 \times (3,1)=(2\times 3,2\times 1)=(6,2)$ 

# linear combinations, span, and bases

## basis vector

When you think about coordinates as scalars, the basis vectors are what those scalars scale.

Any time we describe vectors numerically, it depends on an implicit choice of what basis vectors we're using.

## linear combination

Any time that we're scaling two vectors and adding them, it's called a **linear combination** of those two vectors. 

If you fix one scalar and let the other one change its value freely, the tip of the resulting vector draws a straight line.

If you let both scalars range freely and consider every possible vector that you can get, there are three possible results:

1. For most pairs of vectors, you'll able to reach every possible point in the plane.
2. But if your two original vectors happen to line up, the tip of the resulting vector is limited to just a single line passing through the origin.
3. If both your vectors could be zero, you'd just be stuck at the origin.

### span

the set of all possible vectors that you can reach with a linear combination of a given pair of vectors is called the **span** of those two vectors.

the span of some vectors is basically a way of asking what are all the possible vectors you can reach using only these two fundamental operations.

**Note: In general, if you're thinking about a vector on its own, think of it as an arrow. If you're dealing with a collection of vectors, it's convenient to think of them all as points.**

The flat sheet is the span of two vectors which don't line up. The third vector can be seen as something moving around the span sheet of the first two, sweeping it through all of space.

## basis

A basis of a vector space is a set of **linearly independent** vectors that span the full space.

### linearly independent

When at least one of the vectors is redundant, not adding anything to our span, you have multiple vectors and you could remove one without reducing the span. Whenever this happens, the relevant terminology is to say that they are **linearly dependent**.

One of the vectors can be expressed as a linear combination of the others, since it's already in the span of the others.

Each vector really does add another dimension to the span, then they're said to be **linearly independent**

# matrices as linear transformations

## linear transformation

keep grid lines parallel and evenly spaced $\longrightarrow$ vector v is **always a certain linear combination** of $\hat\imath$ and $\hat\jmath$$\longrightarrow$ we can deduce where vector v must go based only on where $\hat\imath$ and $\hat\jmath$ each land.

If after transforming, the vectors are linearly dependent, then the transformation squishes all of 2-D space onto the line where those two vectors sit.

### transformation

transformation $\rightarrow$ function, something that takes in inputs and spits out an output for each one.

a vector $\longrightarrow$ another vector 

**transformation** can visualize this input-output relation and suggests that you think using movement, which function can't.

### linear

A transformation is linear if it has two properties:

1. **all lines** must remain lines, without getting curved.
2. the origin must remain fixed in place.

### how to describe numerically

record where the two basis vectors - $\hat\imath$ and $\hat\jmath$ - each land and everything else will follow from that.

example: 

$\vec v=-1\hat{\imath}+2\hat{\jmath}=-1\begin{bmatrix} 1\\0\end{bmatrix}+2\begin{bmatrix} 0\\1\end{bmatrix}=\begin{bmatrix} 1\\1\end{bmatrix}$

after transformation:

$\hat{\imath}\rightarrow \begin{bmatrix} 1\\-2\end{bmatrix}$

$\hat{\jmath}\rightarrow \begin{bmatrix} 3\\0\end{bmatrix}$

$\vec v=-1\hat{\imath}+2\hat{\jmath}\rightarrow-1\begin{bmatrix} 1\\-2\end{bmatrix}+2\begin{bmatrix} 3\\0\end{bmatrix}=\begin{bmatrix} 5\\2\end{bmatrix}$

## matrices

### matrix-vector multiplication

$\begin{bmatrix} 3\ 2\\-2\ 1\end{bmatrix}$ can be seen like this: $\hat\imath\rightarrow\begin{bmatrix} 3\\-2\end{bmatrix},\ \hat\jmath\rightarrow\begin{bmatrix} 2\\1\end{bmatrix}$

$\begin{bmatrix} 5\\7\end{bmatrix}$ can be seen as $5\hat\imath+7\hat\jmath$

so, $\begin{bmatrix} 3\ 2\\-2\ 1\end{bmatrix}\times\begin{bmatrix} 5\\7\end{bmatrix}=5\begin{bmatrix} 3\\-2\end{bmatrix}+7\begin{bmatrix} 2\\1\end{bmatrix}=\begin{bmatrix} 3\times5+2\times7\\-2\times5+1\times7\end{bmatrix}=\begin{bmatrix} 29\\-3\end{bmatrix}$

thus, $\begin{bmatrix} a\ b\\c\ d\end{bmatrix}\times\begin{bmatrix} x\\y\end{bmatrix}=x\begin{bmatrix} a\\c\end{bmatrix}+y\begin{bmatrix} b\\d\end{bmatrix}=\begin{bmatrix} ax+by\\cx+dy\end{bmatrix}$, and this operation is called **matrix-vector multiplication** 

### shear

$\hat\imath$ remain fixed, but $\hat\jmath$ moves over to the coordinates $(k,1)$, so the matrix is $\begin{bmatrix} 1\ k\\0\ 1\end{bmatrix}$

# Matrix multiplication as composition

shear: $\begin{bmatrix} 1\ 1\\0\ 1\end{bmatrix}$

rotation: $\begin{bmatrix} 0\ -1\\1\ 0\end{bmatrix}$

composition: $\begin{bmatrix} 1\ -1\\1\ 0\end{bmatrix}$

shear $\times$ (rotate $\times \begin{bmatrix} x\\y\end{bmatrix}$) = composition $\times \begin{bmatrix} x\\y \end{bmatrix} \rightarrow $ shear $\times$ rotation = composition

this means: first, rotate. then, shear. We have to read **from right to left** just like read functions.

think about the geometric representation of matrix multiplication, then you can get this:

$\begin{bmatrix} a\ b\\ c\ d \end{bmatrix}\begin{bmatrix} e\ f\\g\ h\end{bmatrix}=\begin{bmatrix} ae+bg\ \ af+bh\\ce+dg\ \ cf+dh\end{bmatrix}$

Change the order of two matrices, the result may be different. So, evidently **order** totally does matter.

that means: $M_1 M_2\neq M_2M_1$

But: $(M_1M_2)M_3=M_1(M_2M_3)$. Think about what this represents geometrically or look at this from right to left, then it's obviously.

# linear transformations in three dimensions

$\begin{bmatrix} 0\ 0\ 1\\0\ 1\ 0 \\-1\ 0\ 0\end{bmatrix}$ represents a linear transformation in three dimensions.

The linear transformations and multiplying two matrices in three dimensions is also similar in two dimensions.

# the determinant

after shearing, the area of the parallelogram doesn't change.

If we know how much the area of one single unit square changes, if can tell us how the area of any possible region in space changes. Any square in the grid has the same change, no matter the size.

This very special scaling factor, the factor by which a linear transformation changes any area, is called **the determinant of that transformation** (not quite right because the full concept of the determinant allows for negative values. the **absolute value** of the determinant tells you the factor by which areas have been scaled.)

examples:

1.  the determinant of a transformation would be 3, if that transformation increase the area of a region by a factor of 3.
2. the determinant of a 2-D transformation is 0, if it squishes all of space on to a line or even onto a single point. Since then, the area of any region would become 0.

So, checking if the determinant of a given matrix is 0 will give a way of computing whether or not the transformation associated with that matrix squishes everything into a smaller dimension.

## how can we scale area by a negative number?

This has to do with the idea of **orientation**. When the orientation of space is inverted, the determinant will be negative. There two ways to understand this inversion:

- Any transformations like giving the sensation of flipping space over are said to invert the orientation of space.
- think about $\hat \imath$ and $\hat\jmath$: In their starting positions, $\hat\jmath$ is to the left of $\hat\imath$. If after transformation, $\hat\jmath$ is now on the right of $\hat\imath$, the orientation of space has been inverted.

## right hand rule

$\hat\imath$: the forefinger.

$\hat\jmath$: the middle finger.

$\hat k$: the thumb.

the determinant in 3 dimensions become a negative number means you can match the corresponding rule only in left hand.

## how to compute the determinant

$det (\begin{bmatrix} a\ b\\ c\ d \end{bmatrix})=ad-bc$ 

$a$ tells you how much $\hat\imath$ is stretched in the x-direction. 

$d$ tells you how much $\hat\jmath$ is stretched in the y-direction.

if neither of $b$ and $c$ is 0, then that $bc$ term tells you how much this parallelogram is stretched or squashed in the diagonal direction.

$det (\begin{bmatrix} a\ b\ c\\ d\ e\ f\\g\ h\ i \end{bmatrix})=a ~det (\begin{bmatrix} e\ f\\ h\ i \end{bmatrix})-b ~det (\begin{bmatrix} d\ f\\ g\ i \end{bmatrix})+c~ det (\begin{bmatrix} d\ e\\ g\ h \end{bmatrix})$

$det (M_1M_2)= det (M_1) det (M_2)$

# inverse matrices, column space and null space

one of the main reasons that linear algebra is more broadly applicable and required for just about any technical discipline is that it lets us solve certain systems of equations.

it's nice to vertically line up the common variables, so you might need to throw in some zero coefficients whenever the variable doesn't show up in one of the equations. 

**linear system equations** consist of many equations like $ax+by+cz=A,abc\neq0$.

we can package all of the equations together into a single vector equation where we have the matrix containing all of the constant coefficients and a vector containing all of the variables, and their matrix-vector product equals some different constant vector.

we often name that constant matrix $A$, denote the vector holding the variables with a $\vec x$, and call the constant vector on the right-hand side $\vec v$.

## inverse matrices

when $det(A)\neq 0$: there will always be one and only one vector that lands on $\vec v$, and you can find it by playing the transformation in reverse.

In general, $A$ inverse is the unique transformation with the property that if you first apply $A$, then follow it with the transformation A inverse, you end up back where you started. Applying one transformation after another is captured algebraically with **matrix multiplication**.

The core property of this transformation $A$ inverse is that $A$ inverse times $A$ equals the matrix that corresponds to "doing nothing". The transformation that "doing nothing" is called the "identity transformation".

==if $det(A)\neq 0$, then $A^{-1}$ exists.==

==if $det(A)= 0$, then $A^{-1}$ doesn't exist, but it's still possible that a solution exists.==

## rank

When the output of a transformation is a line, meaning it's one-dimensional, we say the transformation has **a rank of 1**.

If all the vector land on some two-dimensional plane, we say the transformation has **a rank of 2**.

**Rank** means the number of dimension in the output of a transformation. It's the number of dimensions in the column space.

When the rank is as high as it can be, meaning it equals the number of columns, we call the matrix **full rank**.

## column space

This set of all possible outputs for a matrix, whether it's a line, a plane, 3-D space, whatever, is called the **column space** of the matrix.

==The zero vector will always be included in the column space since linear transformation must keep the origin fixed in place.==

## null space

This set of vector that lands on the origin is called the **null space** or the **kernel** of the matrix.

It's the space of all vectors that become null, in the sense that they land on the zero vector.

In terms of the linear system of equations, when $\vec v$ happens to be the zero vector, the null space gives you all of the possible solutions to the equation.

# non-square matrices

like $\begin{bmatrix} a\ b\\ c\ d\\e~f \end{bmatrix}$. The column space of it has two dimensions, so it's still full rank.

# dot products and duality

## dot products

If you have two vectors of the same dimension, taking their dot product means pairing up all of the coordinates, multiplying those pairs together and adding the results.

example:$\begin{bmatrix} 1\\ 2 \end{bmatrix}\cdot \begin{bmatrix} 3\\ 4 \end{bmatrix}=1\cdot 3+2\cdot 4$

To think about the dot product between two vectors $\vec v$ and $\vec w$, imagine projecting $\vec w$ onto the line that passes through the origin and the tip of $\vec v$ and multiplying the length of this projection by the length of $\vec v$, then you have the dot product $\vec v \cdot \vec w$.

If the projection of $\vec w$ is pointing in the opposite direction from $\vec v$, their dot product will be negative.

when the two vectors are perpendicular, meaning the projection of one onto the other is the zero vector, their dot product is zero.

the dot product is a very useful geometric tool for understanding projections and for testing whether or not two vectors tend to point in the same direction.

### why order doesn't matter

if $\vec v$ and $\vec w$ happened to have the same length, we could leverage some symmetry.

if they don't have the same length, the symmetry is broken, but it can be transformed into the situation that they have the same length.

example: $\vec v$ and $\vec w$ have the same length, and $\vec h=2\vec v$, so $\vec h\cdot \vec w=2(\vec v\cdot \vec w)$

## duality

If output space of a linear transformation is the number line, no matter how it was defined, there is going to be some unique vector $\vec v$ corresponding to that transformation, in the sense that applying the transformation is the same thing as taking a dot product with that vector.

duality refers to situations where you have a natural-but-surprising correspondence between two types of mathematical thing.

example: 

- the dual of a vector is the linear transformation that it encode.
- the dual of a linear transformation from some space to one dimension is a certain vector in that space.

# cross products in the light of linear transformations

## standard introduction

the cross product of $\vec v$ and $\vec w$ ($\vec v \times \vec w$), is the area of the parallelogram consists of $\vec v$ and $\vec w$.

for $\vec v\times\vec w$:

- if $\vec v$ is on the right of $\vec w$, the cross product is positive. 
- if $\vec v$ is on the left of $\vec w$, the cross product is negative.

==This means that order matters: $\vec v\times\vec w=-\vec w\times\vec v$==

if $\vec v=\begin{bmatrix} a\\ c\end{bmatrix}$and $\vec w=\begin{bmatrix} b\\ d \end{bmatrix}$, $\vec v\times\vec w=det(\begin{bmatrix} a\ b\\ c\ d \end{bmatrix})=ad-bc$

in 3-D, $\vec v\times\vec w=\vec p$, and the length of the new vector $\vec p$ will be the area of that parallelogram. the direction of $\vec p$ is going to be perpendicular to the parallelogram.

use the right hand rule to make the direction clear: point the forefinger of your right hand in the direction of $\vec v$, then stick out your middle finger in the direction of $\vec w$, then when you point up your thumb, that's **the direction of the cross product**.

$\begin{bmatrix} v_1\\v_2\\v_3\end{bmatrix}\times\begin{bmatrix} w_1\\w_2\\w_3\end{bmatrix}=\begin{bmatrix} v_2\cdot w_3-w_2\cdot v_3\\v_3\cdot w_1-w_3\cdot v_1\\v_1\cdot w_2-w_1\cdot v_2\end{bmatrix}$

## deeper understanding with linear transformations

$f\left(\begin{bmatrix} x\\y\\z\end{bmatrix}\right)=det\left(\begin{bmatrix} x~v_1~w_1\\y~v_2~w_2\\z~v_3~w_3\end{bmatrix}\right),\vec v=\begin{bmatrix} v_1\\v_2\\v_3\end{bmatrix},\vec w=\begin{bmatrix} w_1\\w_2\\w_3\end{bmatrix}$

This function is linear, so we can transform it:

$\begin{bmatrix} p_1\\p_2\\p_3\end{bmatrix}\cdot \begin{bmatrix} x\\y\\z\end{bmatrix}=det\left(\begin{bmatrix} x~v_1~w_1\\y~v_2~w_2\\z~v_3~w_3\end{bmatrix}\right),\vec p=\begin{bmatrix} p_1\\p_2\\p_3\end{bmatrix}\Longrightarrow \begin{cases}p_1=v_2\cdot w_3-v_3\cdot w_2\\p_2=v_3\cdot w_1-v_1\cdot w_3\\p_3=v_1\cdot w_2-v_2\cdot w_1\end{cases}$

$V=S\times h$, so to calculate the volume of a parallelepiped made by three vectors, we should know the space of two vectors and the height of the parallelepiped. so, it's a good choice to make $\vec p$ a vector that its length is the area of the parallelogram and it's perpendicular to the parallelogram.

# change of basis

anyway to translate between vectors and sets of numbers is called **a coordinate system** and the two special vector, $\hat\imath$ and $\hat\jmath$, are called the **basis vectors** of our standard coordinate system.

an expression like $A^{-1}MA$ suggests a mathematical sort of empathy. $M$ represents a transformation of some kind as you see it, and the outer two matrices represent the empathy, the shift in perspective. the full matrix product represents that same transformation, but as someone else sees it.

# Eigenvectors and eigenvalues

the special vectors with the special property of **staying on their span** are called the **eigenvectors** of the transformation, and each eigenvector has associated with a value, what's called an **eigenvalue**, which is just the factor by which it stretched or squashed during the transformation.

eigenvalue can be negative. the important part is that the vector stays on the line that it spans out without getting rotated off of it.

if we can find an eigenvector for the rotation, a vector that remains on its own span, what you have found is the axis of rotation. **But** the corresponding eigenvalue would have to be 1.

often, **a better way** to get at the heart of what the linear transformation actually does, less dependent on your particular coordinate system, is to find the eigenvectors and eigenvalues.

$A\vec v=\lambda\vec v$ : $A$ means the transformation matrix. $\vec v$ means the eigenvector. $\lambda$ is a number, namely the corresponding eigenvalue. The expression is saying that the matrix-vector product - A times $\vec v$ - gives the same result as just scaling the eigenvector $\vec v$ by some value $\lambda$.

$A\vec v=(\lambda I)\vec v\Rightarrow (A-\lambda I)\vec v=\vec 0 $: $I$ is the identity matrix with 1's down the diagonal.

we have a new matrix and we're looking for a vector $\vec v$, such that this new matrix times $\vec v$ gives the zero vector. we want a non-zero vector $\vec v$, so the determinant of the matrix is zero.

==a 2-D transformation doesn't have to have eigenvectors.==

==a single eigenvalue can have more that a line full of eigenvector.==

## eigenbasis

**diagonal matrix** means anytime the matrix has 0's everywhere other than diagonal. in it, all the basis vectors are eigenvectors, with the diagonal entries of this matrix being their eigenvalues.

it is difficult to have a matrix that the basis vectors in it is just the eigenvectors. but if our transformation has a lot of eigenvectors and we can choose a set that spans the full space, then we could change our coordinate system so that these eigenvectors are our basis vectors. and the set of basis vectors is called **eigenbasis**.

# abstract vector spaces

a transformation is linear if it satisfies two following properties, commonly called "additivity" and "scaling".

additivity: $L(\vec v+\vec w)=L(\vec v)+L(\vec w)$

scaling: $L(c\vec v)=cL(\vec v)$

# Cramer's rule

Cramer's rule is not actually the best way for computing solutions to linear systems of equations.
$$
\begin{cases}3x+2y=-4\\-1x+2y=-2\end{cases}\Longrightarrow\begin{bmatrix}~~~3~2\\-1~2\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}-4\\-2\end{bmatrix}
$$
if the determinant of the matrix **isn't zero**:

the dot product usually change after the transformation.

transformations which preserve dot products have their own name: **Orthonormal transformations**. after the transformation, all the basis vectors are still perpendicular to each other and still with unit lengths.

as for orthonormal transformation, there is a super specific case, for example:
$$
\begin{bmatrix}
	\cos(30^\circ)~-\sin(30^\circ)\\
	\sin(30^\circ)~~~~~\cos(30^\circ)
\end{bmatrix}
\begin{bmatrix}
	x\\
	y
\end{bmatrix}
=
\begin{bmatrix}
	1\\
	2
\end{bmatrix}
\Longrightarrow 
\begin{cases}
	x=
	\begin{bmatrix}
		1\\2
	\end{bmatrix}
	\cdot
	\begin{bmatrix}
		~~~\cos(30^\circ)\\
		~~~\sin(30^\circ)
	\end{bmatrix}\\
	y=
	\begin{bmatrix}
		1\\
		2
	\end{bmatrix}
	\cdot
	\begin{bmatrix}
	-\sin(30^\circ)\\
	~~~\cos(30^\circ)
	\end{bmatrix}
\end{cases}
$$
for general transformation:
$$
\begin{bmatrix}
	2~-1\\
	0~~~~~~1
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\begin{bmatrix}
4\\
2
\end{bmatrix}
$$

$$
Area=det(A)y\Longrightarrow y=\frac{Area}{det(A)}=
\frac{
	det\left(
	\begin{bmatrix}
		2~~~~~~4\\
		0~~~~~~2
	\end{bmatrix}\right)
}{
	det\left(
	\begin{bmatrix}
		2~-1\\
		0~~~~~~1
	\end{bmatrix}
	\right)
}
$$
