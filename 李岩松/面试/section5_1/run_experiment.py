from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from algorithms import gc, model_free_descent
from quadratic_problem import (
    find,
    generate_matrices,
    grad_f_hat,
    grad_total,
    total,
)


n = 4
c1 = 1.0
c2 = 0.1
c3 = np.full(n, 0.1)

alpha = 0.3
beta = 0.5
eta_min = 0.005
eta_max = 1.0

P, Q = generate_matrices(n, seed=0)

x_start = np.zeros(n)
x_star = find(P, Q, c1, c2, c3)

# 因为 Q 的最大特征值为 1
L_r = c2 * np.linalg.eigvalsh(Q).max()

objective = lambda x: total(
    x, P, Q, c1, c2, c3
)

model_gradient = lambda x: grad_f_hat(
    x, P, c1
)

exact_gradient = lambda x: grad_total(
    x, P, Q, c1, c2, c3
)

baseline = model_free_descent(
    x_start,
    objective,
    exact_gradient,
    x_star,
    alpha,
    beta,
    eta_max,
)

gc_06 = gc(
    x_start,
    objective,
    model_gradient,
    exact_gradient,
    x_star,
    0.6,
    L_r,
    alpha,
    beta,
    eta_min,
    eta_max,
)

gc_09 = gc(
    x_start,
    objective,
    model_gradient,
    exact_gradient,
    x_star,
    0.9,
    L_r,
    alpha,
    beta,
    eta_min,
    eta_max,
)

print("Model-free evaluations:", baseline[1])
print("GC gamma=0.6 evaluations:", gc_06[1])
print("GC gamma=0.9 evaluations:", gc_09[1])

plt.figure(figsize=(7, 5))

plt.semilogy(
    baseline[3],
    baseline[4],
    label="Model-free",
)

plt.semilogy(
    gc_06[4],
    gc_06[5],
    label="GC, gamma=0.6",
)

plt.semilogy(
    gc_09[4],
    gc_09[5],
    label="GC, gamma=0.9",
)

plt.xlabel("Number of function evaluations")
plt.ylabel("Distance to optimum")
plt.title("Gradient Compensation Experiment")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.tight_layout()

output_path = Path(__file__).with_name(
    "convergence.png"
)
plt.savefig(output_path, dpi=200)
plt.show()

print("Figure saved to:", output_path)