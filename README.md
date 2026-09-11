# Erdős problem 261: residual-state geometry

This repository records a structural reduction for the finite-representation
part of [Erdős problem 261](https://www.erdosproblems.com/261).

For \(w(k)=k/2^k\), the open question asks whether every positive integer
\(n\) has a finite set \(A\) of at least two distinct positive integers with

\[
w(n)=\sum_{a\in A}w(a).
\]

The result here does **not** settle that question. It shows that exhaustive
non-greedy search has a much smaller state space than it first appears to
have: until a representation terminates, all reachable residuals form either
one state or one complementary pair.

## Residual-pair lemma

Fix \(n\). Before deciding whether to use index \(a\), define the scaled
residual

\[
r_a=2^{a-1}\left(\frac{n}{2^n}-
  \sum_{j\in A\cap\{n+1,\ldots,a-1\}}\frac{j}{2^j}\right).
\]

Only states \(0\le r_a<a+1\) can lead to a finite representation. The strict
upper bound follows from

\[
\sum_{j=a}^{\infty}\frac{j}{2^j}=\frac{a+1}{2^{a-1}};
\]

equality would require selecting the entire infinite tail. Choosing the digit
\(\varepsilon_a\in\{0,1\}\) gives the exact transition

\[
r_{a+1}=2r_a-a\varepsilon_a,
\qquad 0\le r_{a+1}<a+2.
\]

Let \(R_a\) be the set of all admissible residuals reachable before index
\(a\), beginning with \(R_{n+1}=\{n\}\). Then:

> **Residual-pair lemma.** If no zero state has been reached through index
> \(a-1\), then \(|R_a|\le 2\). If \(|R_a|=2\), its two elements add to
> \(a+1\).

Equivalently, before termination the non-greedy reachability problem follows
at most one state together with its reflection \(r\mapsto(a+1)-r\).

## Proof

The claim holds initially because \(R_{n+1}=\{n\}\). Suppose it holds at
index \(a\).

From a singleton \(\{r\}\), both digit choices are admissible exactly when
\(a\le 2r<a+2\). Since \(r\) is integral, there are two possibilities. If
\(a\) is even, then \(r=a/2\), and one child is zero, so the search
terminates. If \(a\) is odd, then \(r=(a+1)/2\), and the two children are
\(1\) and \(a+1\), whose sum is \(a+2\). Otherwise there is at most one
child.

Now suppose \(R_a=\{r,(a+1)-r\}\), ordering the pair so that
\(r\le(a+1)/2\). The only admissible child contributed from the low member,
apart from the just-discussed midpoint case, is \(2r\). The corresponding
admissible child from the high member is

\[
2((a+1)-r)-a=a+2-2r.
\]

The other two prospective children violate one of the admissibility bounds.
Thus the next reachable set again has at most two elements, and when it has
two they sum to \(a+2\). This proves the induction.

The original finite-representation question is therefore exactly whether
zero is eventually reached from \((a,r)=(n+1,n)\) under this one-or-two-state
dynamics.

## Exact computation

[`residual261.py`](residual261.py) implements the recurrence with exact
integers and checks every returned witness with `fractions.Fraction`. It is an
exploration aid, not a proof of the all-\(n\) conjecture.

For example, it finds

\[
\frac{16}{2^{16}}=
\sum_{a\in\{17,18,19,22,23,24,28,32,33,34,35,36,39,42,43,45,46\}}
\frac{a}{2^a}.
\]

This non-greedy path ends at 46; the corresponding greedy path ends at 392.

## Status and provenance

Recovered from an exploratory Codex transcript dated 2026-09-11. Public
sources checked in that investigation included the Erdős Problems page,
Tengely–Ulas–Zygadło (2020), the Erdős Problem a Day report, and the existing
Jig problem graph. Those sources describe greedy or finite-computational
progress; they did not state this complementary-pair formulation. That is a
limited prior-art check, not a claim that no equivalent observation exists.

