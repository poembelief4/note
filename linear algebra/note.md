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

### multiplication by a number

 **scaling**: the process of stretching or squishing or sometimes reversing the direction of a vector.

**scalar**: a number scaling some vector.

one of the main things that numbers do is scale vectors, so it's common to use the word "scalar" pretty much interchangeably with the word "number".

sample: $2 \times (3,1)=(2\times 3,2\times 1)=(6,2)$ 

# linear combinations, span, and bases