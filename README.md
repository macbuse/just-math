# Just-math

This is odds and ends of code I wrote for diverse math problems:

##Convex sets in high dimensions

*In mathematics, in the theory of Banach spaces, **Dvoretzky's theorem** is an important structural theorem proved by Aryeh Dvoretzky in the early 1960s.[1] It answered a question of Alexander Grothendieck. A new proof found by Vitali Milman in the 1970s[2] was one of the starting points for the development of asymptotic geometric analysis (also called asymptotic functional analysis or the local theory of Banach spaces).*

[Source: wiki] (https://en.wikipedia.org/wiki/Dvoretzky%27s_theorem)

Basically it says that cross sections of the convex look like ellipses.
This
[code](https://github.com/macbuse/just-math/blob/master/dahmani_median_embedding.py)
represents cross sections of the l1 -norm ball which looks like this

![norm ball](https://github.com/macbuse/just-math/blob/master/one_norm.png)


##Sums of two squares



In additive number theory, Pierre de Fermat's theorem on sums of two squares states that an odd prime p is expressible as
p=x^2 +y^2, p = x^2 + y^2 with x and y integers, if and only if   p \equiv 1 \pmod{4}.

[Source : wiki](https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares)

[hermite-serret.py](https://github.com/macbuse/just-math/blob/master/hermite-serret.py)
calculates x, y so that x^2 + y^2 = p for prime p = 1 mod 4 

Use this for example to see non real primes in the gaussian integers
![gaussian primes](https://github.com/macbuse/just-math/blob/master/gaussian_primes.png)



