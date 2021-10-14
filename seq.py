def collatz_print(n):
  print(n, bin(n), sep="\t")
  if n == 1:
    return
  elif n%2 == 1:
    n = 3*n+1
    collatz_print(n)
  else:
    while n%2 == 0:
      n //= 2
    collatz_print(n)

collatz_print(7)
