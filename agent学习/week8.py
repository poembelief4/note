def bayes_update(prior,p_evidence_given_state,p_evidence_given_not_state):
    state=p_evidence_given_state*prior
    not_state=p_evidence_given_not_state*(1-prior)
    p_evidence=state+not_state
    return state/p_evidence

test_cases=[
    (0.5,0.8,0.2),
    (0.2,0.8,0.2),
    (0.3,0.4,0.4),
    (0.1,0.6,0.3),
]

ans=[0.8,0.5,0.3,0.18181818]

import math

for i in range(len(test_cases)):
    tmp=test_cases[i]
    prior=tmp[0]
    state=tmp[1]
    not_state=tmp[2]
    assert math.isclose(bayes_update(prior,state,not_state),ans[i],rel_tol=1e-8)

print("四组测试全部通过。")

probability=0.2

probability=bayes_update(probability,0.8,0.2)
print("第一次更新：",probability)

probability=bayes_update(probability,0.7,0.1)
print("第二次更新：",probability)