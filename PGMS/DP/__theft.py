def solution(N, number):
    num_set = []

    num_set.append({N})
    for i in range(2, 9):
        lst = []

        string = ''
        for q in range(i):
            string += str(N)
        lst.append(int(string))

        max_num = int(i / 2)

        for X_index in range(0, max_num):
            Y_index = i - X_index - 2

            X = num_set[X_index]
            Y = num_set[Y_index]

            for x in X:
                for y in Y:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)

                    if x != 0:
                        lst.append(int(y / x))
                    if y != 0:
                        lst.append(int(x / y))

        lst = set(lst)

        if number in lst:
            return i

        num_set.append(lst)

    return -1


print(solution(5, 88))
