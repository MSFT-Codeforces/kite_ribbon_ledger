Time Limit: **1 second**

Memory Limit: **32 MB**

A merchant sells kites of two types:

- TwinTail kite uses exactly $2$ ribbons.
- QuadTail kite uses exactly $4$ ribbons.

For each test case you are given integers $n, c, d, p$:

- The number of TwinTail kites must be a multiple of $c$ (they come in cartons of $c$).
- The number of QuadTail kites must be a multiple of $d$ (they come in fleets of $d$).
- The total number of ribbons used by all kites must be exactly $n$.
- The total number of kites must be divisible by $p$.

Let $A$ be the number of TwinTail kites and $B$ be the number of QuadTail kites. Then:

- $2A + 4B = n$
- $A \equiv 0 \pmod c$
- $B \equiv 0 \pmod d$
- $(A + B) \equiv 0 \pmod p$
- $A, B \ge 0$ and integers

A *valid shipment* is a pair $(A,B)$ of nonnegative integers satisfying all of the above constraints. For each test case, output the minimum value of $A + B$ over all valid shipments, or $-1$ if there is no valid shipment.

**Input Format:-**

The first line contains an integer $t$ — the number of test cases.  
Each of the next $t$ lines contains four integers $n, c, d, p$.

**Output Format:-**

For each test case, print one integer — the minimum $A+B$ over valid shipments, or $-1$ if there is no valid shipment.

**Constraints:-**

- $1 \le n \le 10^{18}$
- $1 \le c, d \le 10^{9}$
- $1 \le p \le 10^{18}$
**Examples:-**
 - **Input:**
```
1
50 1 1 2
```

 - **Output:**
```
14
```

 - **Input:**
```
4
3 1 1 1
4 2 2 2
24 6 1 5
18 3 3 1
```

 - **Output:**
```
-1
2
-1
6
```

**Note:-**

The **Examples** section above has two example blocks (two separate Input/Output pairs). The first subsection below derives the output for the **first example block** (one test case); the second subsection derives the output for each test case in the **second example block** (four test cases).

**First example block (input: one test case with $n=50$, $c=d=1$, $p=2$; output: $14$):-**  
$n=50$ so $2A+4B=50 \Rightarrow A+2B=25$. With $c=d=1$ there is no restriction on $A,B$, and we need $A+B$ divisible by $p=2$. Minimizing $A+B$ over valid shipments means taking $B$ as large as possible: $B=12$ gives $A=1$, $A+B=13$ (not divisible by $2$); $B=11$ gives $A=3$, $A+B=14$, which is divisible by $2$. So the answer is $14$.

**Second example block (input: four test cases; output: $-1$, $2$, $-1$, $6$):-**  
- Test case 1 ($n=3$, $c=d=p=1$): $n=3$ is odd, so $2A+4B$ can never equal $3$; no valid shipment ⇒ $-1$.
- Test case 2 ($n=4$, $c=d=2$, $p=2$): $A+2B=2$ with $A,B\equiv 0\pmod 2$ ⇒ $A=2$, $B=0$; $A+B=2$ is divisible by $p=2$ ⇒ answer $2$.
- Test case 3 ($n=24$, $c=6$, $d=1$, $p=5$): $A+2B=12$ with $A\equiv 0\pmod 6$ ⇒ $A\in\{0,6,12\}$ give $A+B\in\{6,9,12\}$, none divisible by $5$ ⇒ $-1$.
- Test case 4 ($n=18$, $c=d=3$, $p=1$): $A+2B=9$ with $A,B\equiv 0\pmod 3$ ⇒ $B=3$, $A=3$, $A+B=6$ divisible by $p=1$ ⇒ answer $6$.