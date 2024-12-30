## Analysis

We can approach this problem by trying to understand how $R$ impacts the task. As *R* is increased, it's more likely to have less cows to complete the task. Especially, if $C$ ($C <= K$) cows can complete the task with $R1$, then the same amount of cows can complete the task with $R2$ ($R2 > R1$). This monotonicity is a perfect fit for binary search.

Let's define a function `bool f(int r)` to represent if we can use at most $K$ cows with radius $r$ to complete the task. For the radius sequence $r_1$, $r_2$, ... $r_n$ in ascending order, apply the function, we can get the sequence like $F$, $F$, $F$, $T$, $T$ ..., we would like to know the correponding $r$ of the first $T$.

The challenging part is to implement the function. This is equivalent with if we can place $C$ cows with radius *r* to complete the task, where $C<=K$. We can use a greedy strategy. For a given $r$, we can minimize the cows by minimizing the overlap of areas covered by each cow.


## Code
