#1, 11, 13
def ex1(n):
    i = n + 1
    while True:
        is_prime = True

        for j in range (2, i-1): #int i = 2; i <= i-1; i++
            if i % j == 0:
                is_prime = False

        if is_prime:
            print(f"Primul numar prim dupa {n} este {i}")
            break
        else:
            i = i + 1


def ex11(n1, n2):
  a = str(n1)
  b = str(n2)
  for x in a:
    f = 0
    for y in b:
      if x == y:
        f = 1
    if f == 0:
      return False
  for x in b:
    f = 0
    for y in a:
      if x == y:
        f = 1
    if f == 0:
      return False
  return True

#print(ex11(2113, 323121))

def ex13(n):
  k = 0
  c = 0
  while True:
    k += 1
    t = k
    d = 2
    s = []
    if k == 1:
      s = [1]
    while d * d <= t:
      if t % d == 0:
        s.append(d)
        while t % d == 0:
          t //= d
      d += 1
    if t > 1:
      s.append(t)
    for x in s:
      c += 1
      if c == n:
        return x

print(ex13(67))

prin("hello world") 