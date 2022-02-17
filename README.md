# Introduciton to Models of Computation

## Chapter 1

### Intial function

```python
def Z(): return 0

def S(x): return x + 1

# (n : N) -> N -> N^n -> N
# n is the dimension
# i is 1-indexed
def P(n, i):
  def f(*vec):
    assert len(vec) == n
    return vec[i - 1]
  return f
```

### Arithmetic function

```python
def diff(x, y):
  if x <= y:
    return y - x
  else:
    return x - y

def N(x):
  if x != 0:
    return 0
  else:
    return 1

def N2(x):
  if x != 0:
    return 1
  else:
    return 0
```

### Operator

```python
# ( (N^{m} -> N) x (N^n -> N)^m ) -> (N^{n} -> N)
def comp(f, *gs):
  # m = len(gs)
  def h(*x):
    # n = len(y)
    # simple version
    # vec = []
    # for g in gs:
    #   vec.append(g(*x))
    # return f(*vec)
    return f(*map(lambda g: g(*x), gs))
  return h

# (N^{k + 1} -> N) -> (N^{k + 1} -> N)
def sigma(f):
  def g(n, *y):
    sum = 0
    for i in range(n + 1):
      sum += f(i, *y)
    return sum
  return g

# (N^{k + 1} -> N) -> (N^{k + 1} -> N)
def prod(f):
  def g(n, *y):
    mul = 1
    for i in range(n + 1):
      mul *= f(i, *y)
    return mul
  return g

# (N^{k + 1} -> N) -> (N^{k + 1} -> N)
def mu(f):
  h = comp(N2, f)
  g = prod(h)
  return comp(diff, sigma(g), g)

# (N^{k + 1} -> N) -> (N^{k + 1} -> N)
def max(f):
  k = f.__code__.co_argcount - 1
  
  h = comp(f, comp(sub, P(k + 2, 2), P(k + 2, 1)), *map(lambda i: P(k + 2, i), range(3, k + 3)))
  g = prod(comp(N2, h))
  t = comp(sigma(g), P(k + 1, 1), *map(lambda i: P(k + 1, i), range(1, k + 2)))

  return comp(diff, comp(diff, P(k + 1, 1), t), prod(comp(N2, f)))
```

### Examples

Solve a quadratic equation in the range [0, n].

```python
def quadratic(i, a, b, c):
  return a * i * i + b * i + c

solve_l = mu(quadratic)
solve_r = max(quadratic)

print('n, a, b, c = ', end = '')
n, a, b, c = map(int, input().split(' '))

x1 = solve_l(n, a, b, c)
x2 = solve_r(n, a, b, c)

print('{} * x^2 + {} * x + {} = 0'.format(a, b, c))
print('x_1 = {}'.format(x1))
print('x_2 = {}'.format(x2))
```

Arithmetic.

```python
mul = comp(diff, sigma(P(2, 2)), P(2, 2))
# print('3 x 4 =', mul(3, 4)) # 12

add = comp(diff, comp(mul, comp(S, P(2, 1)), comp(S, P(2, 2))), comp(S, mul))
# print('3 + 4 =', add(3, 4)) # 7

sub = comp(
  mul,
  diff,
  comp(N2, comp(diff, comp(add, comp(diff, P(2, 2), P(2, 1)), P(2, 1)), P(2, 2)))
)
# print('3 - 4 =', sub(3, 4)) # 0
# print('4 - 3 =', sub(4, 3)) # 1

def get_div():
  g0 = comp(N, comp(sub, comp(mul, P(3, 3), comp(S, P(3, 1))), P(3, 2)))
  g1 = sigma(g0)
  g2 = comp(g1, P(2, 1), P(2, 1), P(2, 2))
  g3 = comp(N2, P(2, 2))
  return comp(mul, g2, g3)
div = get_div()
# print('1 / 0 =', div(1, 0)) # 0
# print('4 / 3 =', div(4, 3)) # 1
# print('6 / 3 =', div(6, 3)) # 2
# print('7 / 2 =', div(7, 2)) # 3
# print('4 / 1 =', div(4, 1)) # 4

pow = comp(
  add,
  comp(div, comp(prod(P(2, 2)), P(2, 2), P(2, 1)), P(2, 1)),
  comp(mul, comp(N, P(2, 1)), comp(N, P(2, 2)))
)
# print('1 ** 1 = ', pow(1, 1)) # 1
# print('2 ** 2 = ', pow(2, 2)) # 4
# print('3 ** 3 = ', pow(3, 3)) # 27
# print('4 ** 4 = ', pow(4, 4)) # 256
```

Number theory.

```python
tau = comp(
  sigma(comp(N, comp(rs, P(2, 2), P(2, 1)))),
  P(1, 1),
  P(1, 1)
)
# print('tau(1) =', tau(1)) # 1
# print('tau(2) =', tau(2)) # 2
# print('tau(3) =', tau(3)) # 2
# print('tau(4) =', tau(4)) # 3
# print('tau(5) =', tau(5)) # 2
# print('tau(6) =', tau(6)) # 4
# print('tau(7) =', tau(7)) # 2
# print('tau(8) =', tau(8)) # 4
# print('tau(24) =', tau(24)) # 8

prime = comp(N, comp(diff, tau, comp(S, comp(S, comp(Z)))))
# print('prime(1) =', prime(1)) # 0
# print('prime(2) =', prime(2)) # 1
# print('prime(3) =', prime(3)) # 1
# print('prime(4) =', prime(4)) # 0
# print('prime(5) =', prime(5)) # 1
# print('prime(6) =', prime(6)) # 0
# print('prime(7) =', prime(7)) # 1
# print('prime(8) =', prime(8)) # 0
# print('prime(9) =', prime(9)) # 0

pi = sigma(prime)
# print('pi(9) =', pi(9)) # 4

two = comp(S, comp(S, comp(Z)))
pn = comp(
  mu(comp(diff, comp(pi, P(2, 1)), comp(S, P(2, 2)))),
  comp(pow, two, comp(pow, two, P(1, 1))),
  P(1, 1)
)
# print('P_0 =', pn(0)) # 2
# print('P_1 =', pn(1)) # 3
# print('P_2 =', pn(2)) # 5
```
