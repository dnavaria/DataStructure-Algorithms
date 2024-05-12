def check_values(x, y, z):
    return x >= 0 and y >= 0 and z >= 0


def get_permutations(x, y, z, hash_map):
    if not check_values(x, y, z):
        return
    if check_values(x, y, z) and hash_map.get((x, y, z)) is None:
        hash_map[(x, y, z)] = 1
    get_permutations(x - 1, y, z, hash_map)
    get_permutations(x, y - 1, z, hash_map)
    get_permutations(x, y, z - 1, hash_map)
    return


def permute_inorder(x, y, z):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(1 + z) if i + j + k != n]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # hash_map = {}
    # get_permutations(x, y, z, hash_map)
    # result = []
    # for arr in hash_map.keys():
    #     if sum(arr) != n:
    #         result.append(list(arr))
    # print(result)
    print(permute_inorder(x, y, z))