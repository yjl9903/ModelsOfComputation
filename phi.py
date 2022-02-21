from chap1 import *

def div(x, y):
  if y != 0:
    return x // y
  else:
    return 0

def mul(x, y): return x * y

def pow(x, y): return x ** y

def rs(x, y):
  if y != 0:
    return x % y
  else:
    return x

def ep(n, x):
  p = pn(n)
  c = 0
  while x % p == 0:
    x = x // p
    c = c + 1
  return c

phi = comp(
  comp(
    mul,
    prod(
      comp(
        add, 
        comp(
          mul,
          comp(
            mul,
            comp(prime, P(2, 1)),
            comp(comp(N2, sub), P(2, 1), comp(S, comp(Z)))
          ),
          comp(
            mul,
            comp(comp(N, rs), P(2, 2), P(2, 1)),
            comp(sub, P(2, 1), comp(S, comp(Z)))
          )
        ),
        comp(
          comp(N, mul),
          comp(
            mul,
            comp(prime, P(2, 1)),
            comp(comp(N2, sub), P(2, 1), comp(S, comp(Z)))
          ),
          comp(comp(N, rs), P(2, 2), P(2, 1))
        )
      )
    ),
    comp(
      div,
      P(2, 2),
      prod(
        comp(
          add, 
          comp(
            mul,
            comp(
              mul,
              comp(prime, P(2, 1)),
              comp(comp(N2, sub), P(2, 1), comp(S, comp(Z)))
            ),
            comp(
              mul,
              comp(comp(N, rs), P(2, 2), P(2, 1)),
              P(2, 1)
            )
          ),
          comp(
            comp(N, mul),
            comp(
              mul,
              comp(prime, P(2, 1)),
              comp(comp(N2, sub), P(2, 1), comp(S, comp(Z)))
            ),
            comp(comp(N, rs), P(2, 2), P(2, 1))
          )
        )
      )
    ),
  ),
  P(1, 1),
  P(1, 1)
)
# print('phi(1) =', phi(1))
# print('phi(2) =', phi(2))
# print('phi(3) =', phi(3))
# print('phi(4) =', phi(4))
# print('phi(5) =', phi(5))
# print('phi(6) =', phi(6))
# print('phi(7) =', phi(7))
# print('phi(8) =', phi(8))
# print('phi(9) =', phi(9))
# print('phi(10) =', phi(10))
# print('phi(11) =', phi(11))
# print('phi(12) =', phi(12))
