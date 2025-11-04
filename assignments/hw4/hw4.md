---
geometry: margin=0.75in

---

# Introduction to Artificial Intelligence
## Homework 4 Resolution by Dino Meng [SM3201466]

---

# Q1. Logic

## Exercise a)

**i.)** The assertion is valid. Without loss of generality, if we assume that $\alpha \models \gamma$ then $(a \land \beta) \models \gamma$ must be also true since that by assuming that $(a \land \beta)$ are true we have that $\alpha$ is true, which entails $a \models \gamma$.

**ii.)** Not generally valid, we have a counterexample for $\alpha = A, \beta = B, \gamma= A \land B$. It's certain that $(A \land B) \models (A \land B)$, but not that $A \models (A \land B)$.

**iii.)** Not generally valid, we have a counterexample for $\alpha = A,\beta = \neg A, \gamma=A$. In fact, assuming that $\alpha \models (A \vee \neg A)$ (the RHS is a tautology so it's always true) it's certain that $\alpha \models \neg \alpha$ is false.

## Exercise b)

**i.)** True, clearly a taulogy.

**ii.)** Neither, it can be satisfiable. For example, when Smoke and Fire are both true.

**iii.)** By using some known equivalencies, we have that the formula is equivalent to Smoke $\vee \neg$ Fire which is not valid but satisfiable.

**iv.)** Valid, since that Fire $\vee \neg$ Fire is clearly a tautology.

**v.)** Valid, by transforming the LHS and the RHS with known rules we have a formula of type
$$
(\neg A \vee \neg B \vee C) \iff (\neg A \vee \neg B \vee C)
$$
(where A is Smoke, B is heat and C is fire) Which is obviously valid.

**vi.)** Likewise, by transforming the implications we have a form of type
$$
(A \vee \neg A \vee \neg B \vee C) \land (\neg C \vee C \vee \neg A \vee \neg B)
$$
which is valid, as both of the clauses are trivial (i.e. contain tautologies).

**vii.)** Valid, by transforming the implications we get the form Big $\vee$ Dumb $\vee \neg$ Big $\vee$ Dumb which contains a tautology.

## Exercise c)

**i.** 
$$
S^{t+1} \iff \big((S^t \land a^t) \lor (\lnot S^t \land b^t)\big) \land \big((a^t \land \lnot b^t) \lor (b^t \land \lnot a^t)\big)
$$

The LHS (with respect to the central $\land$ operator) models the transition towards $S^{t+1}$ according to the action taken, the RHS models the fact that the agent must take only one action at the time step $t$

We can simplify the second part by assuming that $a^t \equiv \neg b^t$, giving us the form
$$
S^{t+1} \iff (S^t \land a^t) \lor (\lnot S^t \land b^t)
$$

**ii.** Using distributive and De Morgan's laws, we have the form

$$
S^{t+1}\iff(S^t \vee b^t)\land(a^t \vee \neg S^t) 
$$

By doing further transformations, we obtain the final CNF composed of four clauses:

1. $\neg S^{t+1}, S^t \neg a^t$
2. $\neg S^{t+1}, \neg S^t, a^t$
3. $S^{t+1}, \neg S^t, \neg a^t$ 
4. $S^{t+1}, S^t, a^t$ 

# Q2. FOL

**iii.)** (Occupation(SURGEON, EMILY) $\land \neg$ (Occupation(LAWYER, EMILY)) $\vee$ (Occupation(LAWYER, EMILY) $\land$ $\neg$ Occupation(LAWYER, EMILY)

**iv.)** OCCUPATION(ACTOR, JOE) $\land$ ($\exists$ O, O $\neq$ ACTOR $\land$ OCCUPATION(P, JOE))

**v.)** $\forall$ P, OCCUPATION(SURGEON, P) $\implies$ OCCUPATION(DOCTOR, P)

**vi.)** $\neg \exists$ P, OCCUPATION(LAWYER, P) $\land$ CUSTOMER(P, JOE)

**vii.** $\exists$ P, OCCUPATION(LAWYER, P) $\land$ BOSS(P, EMILY)

**viii.** $\exists$ P, OCCUPATION(LAWYER, P) $\land$ ($\forall$ P', CUSTOMER(P', P) $\implies$ OCCUPATION(P', DOCTOR))

**ix.** $\forall$ P, OCCUPATION(P, SURGEON), ($\exists$ P' OCCUPATION(P', LAWYER) $\land$ CUSTOMER(P, P'))

# Q3. LOCAL SEARCH

## a) HC

**i.** False, it can get stuck on local minimas which might not represent effective solutions at all

**ii.** False, It cannot if it's not complete then it cannot be optimal

## b) SA

**i.** True, by the properties of the function $\exp(\Delta E / T)$ where $\Delta E$ is negative.

**ii.** If A or B were to be picked they would have 1.0 probability of being chosen as they have positive energy difference. C has a probability of 0.5 of being the successor if they were randomly chosen. Normalizing all of the probabilities, we obtain that A, B have probabilities of 0.4 each in being the successor, while C has the probability 0.2.

Summary: p(A)=p(B)=0.4, p(C)=0.2

**iii.** True, it's proven that simulated annealing is optimal

## c) LBS

States A and B will be expanded before C and D, since the initial "beams" will greedily pick A,B first

## d) GA

Both are true by definition of genetic algorithm.

## e) GD

**i.** False, it can get stuck on plateaus or local minimas (unless the objective function is convex)

**ii.** $x_{k+1} = x_k - \alpha f'(x_k)$ 

