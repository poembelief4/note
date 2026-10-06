import numpy as np

def bt_line_search(x,obj,Dir,alpha,beta,eta_min,eta_max):
    eta=eta_max
    evaluation=0
    now=obj(x)
    dir_norm_2=Dir@Dir

    if(dir_norm_2==0): 
        return 0.0,evaluation
    while True:
        candidate=x-eta*Dir
        candidate_value=obj(candidate)
        evaluation+=1

        armijo=now-alpha*eta*dir_norm_2

        if candidate_value<=armijo:
            return eta,evaluation
        if eta<=eta_min:
            return 0.0,evaluation

        eta=beta*eta

def model_based_descent(x,obj,model_grad,delta,gamma,L_r,e_0,alpha,beta,eta_min,eta_max,max_step=10000):
    x=x.copy()
    e=e_0
    evaluation=0
    step=0
    history=[]

    while step<max_step:
        g=model_grad(x)+delta

        threshold=(1.0-gamma)/gamma*np.linalg.norm(g)

        if e>threshold:
            break

        eta,used=bt_line_search(x,obj,g,alpha,beta,eta_min,eta_max)
        evaluation+=used

        if eta==0.0:
            break

        x_new=x-eta*g
        e+=L_r*np.linalg.norm(x_new-x)

        x=x_new
        step+=1

        history.append((evaluation,x.copy()))

    return x,e,evaluation,step,history

def gc(x,obj,model_grad,exact_grad,x_star,gamma,L_r,alpha,beta,eta_min,eta_max,lim=1e-3,max_outer=1000):
    x=x.copy()
    evaluation=0
    model_step=0

    evaluation_history=[0]
    error_history=[np.linalg.norm(x-x_star)]

    delta=exact_grad(x)-model_grad(x)
    evaluation+=x.size

    e_0=0.0

    for outer_step in range(1,max_outer+1):
        offset=evaluation
        x,_,used,step,inner_history=model_based_descent(x,obj,model_grad,delta,gamma,L_r,e_0,alpha,beta,eta_min,eta_max)

        for local_evaluation,point in inner_history:
            evaluation_history.append(offset+local_evaluation)
            error_history.append(np.linalg.norm(point-x_star))

        evaluation+=used
        model_step+=step

        if np.linalg.norm(x-x_star)<lim:
            break

        true_grad=exact_grad(x)
        delta=true_grad-model_grad(x)
        evaluation+=x.size

        eta,used=bt_line_search(x,obj,true_grad,alpha,beta,0.0,eta_max)
        evaluation+=used

        if(eta==0.0):
            break;
        x_new=x-eta*true_grad

        e_0=L_r*np.linalg.norm(x_new-x)

        x=x_new

        evaluation_history.append(evaluation)
        error_history.append(np.linalg.norm(x-x_star))

        if np.linalg.norm(x-x_star)<lim:
            break
    return (
        x,
        evaluation,
        model_step,
        outer_step,
        np.asarray(evaluation_history),
        np.asarray(error_history),
    )

def model_free_descent(x,obj,exact_grad,x_star,alpha,beta,eta_max,lim=1e-3,max_step=10000):
    x=x.copy()
    evaluation=0
    step=0

    evaluation_history=[0]
    error_history=[np.linalg.norm(x-x_star)]

    while(step<max_step):
        if(np.linalg.norm(x-x_star)<lim):
            break

        true_grad=exact_grad(x)
        evaluation+=x.size

        eta,used=bt_line_search(x,obj,true_grad,alpha,beta,0.0,eta_max)
        evaluation+=used

        if eta==0.0:
            break

        x=x-eta*true_grad
        step+=1

        evaluation_history.append(evaluation)
        error_history.append(np.linalg.norm(x-x_star))

    return (
        x,
        evaluation,
        step,
        np.asarray(evaluation_history),
        np.asarray(error_history),
    )

if __name__ == "__main__":
    from quadratic_problem import (
        generate_matrices,
        total,
        grad_total,
    )

    n = 4
    c1 = 1.0
    c2 = 0.1
    c3 = np.full(n, 0.1)

    P, Q = generate_matrices(n, seed=0)
    x = np.ones(n)

    f = lambda value: total(
        value, P, Q, c1, c2, c3
    )

    exact_gradient = grad_total(
        x, P, Q, c1, c2, c3
    )

    eta, evaluation = bt_line_search(x,f,exact_gradient,0.3,0.5,0.005,1.0)

    print("找到的 eta：", eta)
    print("函数评估次数：", evaluation)
    print("更新前函数值：", f(x))
    print("更新后函数值：", f(x - eta * exact_gradient))
