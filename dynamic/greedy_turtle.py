from pprint import pprint


def get_best_way(ways: tuple[tuple[int]]):
    """Находит лучший путь для получения монет."""
    range_ways = len(ways)

    table = [[0 for _ in range(range_ways+1)] for _ in range(range_ways+1)]

    for row in range(range_ways):
        for col in range(range_ways):
            if col == 0:
                table[row+1][col+1] = ways[row][col] + table[row][col+1]
            else:
                count_row = ways[row][col] + table[row+1][col]
                count_col = ways[row][col] + table[row][col+1]
                table[row+1][col+1] = max(count_row, count_col)
    pprint(table)

    return f'Наибольшее число монет: {table[-1][-1]}'


if __name__ == '__main__':

    array = ((19, 8, 3, 12, 5),
             (0, 7, 16, 1, 14),
             (15, 18, 4, 17, 2),
             (3, 11, 6, 20, 13),
             (10, 2, 0, 15, 9))

    print(get_best_way(array))
