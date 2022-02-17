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
def sub(x, y):
  if x <= y:
    return 0
  else:
    return x - y

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

Multiplication.

```python
mul = comp(sub, sigma(P(2, 2)), P(2, 2))

# print('3 x 4 =', mul(3, 4)) # = 12
```

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
