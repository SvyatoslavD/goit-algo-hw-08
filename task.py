import heapq


def cables_min_cost(lengths):

    heapq.heapify(lengths)

    sum = 0
    while len(lengths) > 1:
        c_a = heapq.heappop(lengths)
        c_b = heapq.heappop(lengths)

        new_c = c_a + c_b
        heapq.heappush(lengths, new_c)

        sum += new_c

    return sum


cl = [3, 3, 4, 4, 9]
print(cables_min_cost(cl))

cl = [2, 4, 8, 5]
print(cables_min_cost(cl))

cl = [10, 10, 10, 10, 10]
print(cables_min_cost(cl))
