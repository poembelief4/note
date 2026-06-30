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
