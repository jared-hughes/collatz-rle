from itertools import groupby

# Contract (0) rule
# [...L, a, 0, b, ...S]
# [...L, a+b, ...S]

# Contract (-1) rule in a 1 spot
# [...L, x, -1, y, ...S]
#    x  y
# 1000
#    00001
# 10000001
# [...L, x+y-1, ...S]

# Contract (-1) rule in a 0 spot
# [...L,   x, a, -1, b, ...S]
#  x    a  b
# 0011111
#       11110
# 01000001110
# [...L, x-1, 1,  a, b-1, ...S]
# Same total number of bits


def binary_to_rle(s):
    return [len(list(group)) for _, group in groupby(s)]


def rle_to_binary(rle):
    if -1 in rle: print("warning: rle has -1")
    return "".join(str((i + 1) % 2) * n for (i, n) in enumerate(rle))

def rle_to_num(rle):
    return binary_to_num(rle_to_binary(rle))

def num_to_rle(num):
    return binary_to_rle(num_to_binary(num))


def num_to_binary(n):
    return bin(n)[2:]


def binary_to_num(s):
    return int(s, 2)

def times3(rle):
    L = []
    for i in rle:
        L.extend([1, 1, i-2])
    return L + [1, 1]

# def contract_zeros(rle):
#     I = [rle[0]]
#     for 

r = [1,3,2]
print("manual times 3", num_to_binary(rle_to_num(r)*3))
T = times3(r)
print("rle times 3", T)
print("auto   times 3", rle_to_binary(T))
