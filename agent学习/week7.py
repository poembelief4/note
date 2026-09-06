import numpy as np

def f(x):
    return x**3

def numerical_derivative(x,h):
    return (f(x+h)-f(x-h))/(2*h)

x=2.0
h_value=[1.0,0.1,0.01,0.00001]

for h in h_value:
    result=numerical_derivative(x,h)
    print("h=",h,"数值导数=",result)

analytical_derivative=3*x**2
print("解析导数=",analytical_derivative)

assert np.isclose(
    numerical_derivative(x,0.00001),
    analytical_derivative,
    atol=0.0001
)

from matplotlib import pyplot as plt
x_values=np.linspace(0,3,200)
y_values=f(x_values)

x0=2.0
slope=3*x0**2

tangent_values=f(x0)+slope*(x_values-x0)

plt.plot(x_values,y_values,label="y = x^3")
plt.plot(x_values,tangent_values,label="tangent at x = 2")
plt.scatter([x0],[f(x0)])

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()

def loss(x):
    return (x-3)**2

def gradient(x):
    return 2*(x-3)

w=0.0
learning_rate=0.1

for step in range(1,21):
    grad=gradient(w)
    w-=learning_rate*grad

    print(
        "step=",step,
        "w=",w,
        "loss=",loss(w),
        "used_gradient=",grad
    )

def run_gradient_descent(learning_rate,steps):
    w=0.0
    W=[w]
    Loss=[loss(w)]
    for i in range(steps):
        grad=gradient(w)
        w-=learning_rate*grad
        W.append(w)
        Loss.append(loss(w))
    return W,Loss

learning_rates=[0.01,0.1,0.5,0.9,1.0,1.1]
for i in range(len(learning_rates)):
    x_w,losses=run_gradient_descent(learning_rates[i],30)
    plt.plot(losses,label=f"lr={learning_rates[i]}")

plt.xlabel("step")
plt.ylabel("loss")
plt.yscale("log")
plt.grid()
plt.legend()
plt.show()