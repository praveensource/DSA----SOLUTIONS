from itertools import permutations

def reorderedPowerOf2(n):
    digits = list(str(n))
    for perm in set(permutations(digits)):
        if perm[0] == '0':
            continue
        num = int("".join(perm))
        if (num & (num - 1)) == 0:  # check power of 2
            return True
    return False
