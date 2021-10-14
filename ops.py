from conversions import *


def contract_mutate(rle):
    if -1 in rle:
        """
        Contract (-1) rule in a 1 spot
        [...L, a, b, -1, c, ...S]
        a  b   c
        111000
            00001
        1101110001
        [...L, a-1, 1, b, c-1, ...S]

        Contract (-1) rule in a 0 spot
        [...L,   a, b, -1, c, ...S]
        a    b  c
        0011111
            11110
        01000001110
        [...L, a-1, 1, b, c-1, ...S]
        Same rule
        """
        i = rle.index(-1)
        a, b, _, c = rle[i - 2 : i + 2]
        rle[i - 2 : i + 2] = [a - 1, 1, b, c - 1]
        contract_mutate(rle)
    elif 0 in rle:
        i = rle.index(0)
        if i == 0:
            # remove leading zeros
            rle[:2] = []
        elif i == len(rle) - 1:
            # remove trailing zeros
            rle[-2:] = []
        else:
            """
            Contract (0) rule
            [...L, a, 0, b, ...S]
            [...L, a+b, ...S]
            """
            a, _, b = rle[i - 1 : i + 2]
            rle[i - 1 : i + 2] = [a + b]
        contract_mutate(rle)


def contracted(rle):
    rle_copy = rle.copy()
    contract_mutate(rle_copy)
    return rle_copy


def collatz_step(rle):
    """
    Given the RLE `rle` in standard form representing x, compute (3*x+1)/2,
    then keep divide by 2 to remove trailing zeros, and contract to
    obtain standard form again.

    For reference, standard form is an RLE of odd length with positive entries
    """
    assert min(rle) >= 1, "RLE must have positive integers"
    assert len(rle) % 2 == 1, "RLE must have odd length"

    L = []
    for i in rle:
        L.extend([1, 1, i - 2])
    """
    let L = [...S, x]
    Then 3*rle = [...L, 1, 1]
    (3*rle+1/2)
        = ([...S, x, 1, 1] + 1)/2
        = [...S, x+1, 1, 0]/2
        = [...S, x+1]
    """
    L[-1] += 1
    """
    if rle[-1] == 1 to begin with, then
        L[-1] == 0 now
        L = [...T, k, 0]
    Keep dividing by 2, so
        L/2^k = [...T]
    """
    return contracted(L)


def print_rle(rle):
    num = rle_to_num(rle)
    print(num, bin(num), rle, sep="\t")


def collatz_rle_print(rle):
    print_rle(rle)
    while rle_to_num(rle) > 1:
        rle = collatz_step(rle)
        print_rle(rle)


if __name__ == "__main__":
    for start in range(1, 20, 2):
        collatz_rle_print(num_to_rle(start))
        print()
