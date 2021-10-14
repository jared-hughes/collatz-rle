from itertools import groupby


def binary_to_rle(s):
    return [len(list(group)) for _, group in groupby(s)]


def rle_to_binary(rle):
    if -1 in rle:
        print("warning: rle has -1")
    return "".join(str((i + 1) % 2) * n for (i, n) in enumerate(rle))


def rle_to_num(rle):
    return binary_to_num(rle_to_binary(rle))


def num_to_rle(num):
    return binary_to_rle(num_to_binary(num))


def num_to_binary(n):
    return bin(n)[2:]


def binary_to_num(s):
    return int(s, 2)


if __name__ == "__main__":
    r = [2, 1, 1, 3, 2]
    print(r)
    print("manual times 3", num_to_binary(rle_to_num(r) * 3))
