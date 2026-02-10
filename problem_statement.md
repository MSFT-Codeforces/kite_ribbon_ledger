**Kite Ribbon Ledger**

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

For each test case, output the minimum possible value of $A + B$, or $-1$ if it is impossible.

**Input Format:-**

The first line contains an integer $t$ — the number of test cases.  
Each of the next $t$ lines contains four integers $n, c, d, p$.

**Output Format:-**

For each test case, print one integer — the minimum possible total number of kites, or $-1$ if no valid shipment exists.

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
In the first example, $n=50$ so $2A+4B=50 \Rightarrow A+2B=25$. With $c=d=1$ there is no restriction on $A,B$, and we need $A+B$ divisible by $p=2$. Trying to minimize $A+B$ means taking $B$ as large as possible: $B=12$ gives $A=25-2\cdot 12=1$, so $A+B=13$ (not divisible by $2$); the next is $B=11$, $A=3$, giving $A+B=14$, which is divisible by $2$, so the answer is $14$.

In the second example, test case 1: $n=3$ is odd, so $2A+4B$ can never equal $3$; hence no solution exists and the answer is $-1$.

In the second example, test case 2: $n=4$ so $A+2B=2$. Since $A\equiv 0\pmod 2$ and $B\equiv 0\pmod 2$, the only way to satisfy $A+2B=2$ is $A=2, B=0$, and then $A+B=2$ is divisible by $p=2$; the answer is $2$.

In the second example, test case 3: $n=24$ so $A+2B=12$. With $A\equiv 0\pmod 6$, possible values are $A=0,6,12$, giving $(B=6),(B=3),(B=0)$ respectively; however, in all cases $A+B\in\{6,9,12\}$, none of which is divisible by $p=5$, so the answer is $-1$.

In the second example, test case 4: $n=18$ so $A+2B=9$. With $A\equiv 0\pmod 3$ and $B\equiv 0\pmod 3$, $B$ can only be $0$ or $3$; $B=3$ would give $A=3$, so $A+B=6$, which is divisible by $p=1$, and it is also the minimum possible total, so the answer is $6$.