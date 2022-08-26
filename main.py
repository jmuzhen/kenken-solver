# ken ken solver v1
# made by J Muzhen

import itertools
import math

from datetime import datetime

count = 0

gridsize = int(input("Input grid size > "))

width, height = gridsize, gridsize
grid = [[0 for x in range(width)] for y in range(height)]  # init grid

instructions = {}
while True:
    Continue = False
    # input instructions
    lst = input("Instruction > ").split(" ")
    lst2 = []
    for i in lst[0:-1]:
        x, y = int(i.replace(" ", "").split(",")[0]), int(i.replace(" ", "").split(",")[1])
        lst2.append((x-1, y-1))
        grid[x - 1][y - 1] = 1
    instructions[tuple(lst2)] = (int((lst[-1])[0:-1]), (lst[-1])[-1])  # adds instructions

    # print(grid)
    # print(instructions)
    for row in grid:
        for item in row:
            # print(item)
            if item == 0:
                Continue = True

    if Continue: continue
    else: break

for i in range(gridsize):
    for j in range(gridsize):
        grid[i][j] = j+1

# sorted([i[:2], i[2:]] for i in set(permutations(chain.from_iterable(grid))))


# def generate_base(n):
#     return [list(((i + x) % n) + 1 for x in range(n)) for i in range(n)]
#
#
# def generate(n):
#     return list(itertools.permutations(generate_base(n)))


# gridlist = generate(gridsize)

# ----------------------------
def are_columns_unique(board):
    columns = [set() for _ in range(len(board))]
    for row in board:
        for i, value in enumerate(row):
            column = columns[i]
            if value in column:
                return False
            else:
                column.add(value)
    return True


def generate_boards(n):
    digits = tuple(range(1, n + 1))
    for board in itertools.product(itertools.permutations(digits), repeat=n):
        if are_columns_unique(board):
            yield board


# print(gridlist)
print(f"Solving...\n")
num_tested = 0
starttime = datetime.utcnow()

# for grid in list(gridlist):
for grid in generate_boards(gridsize):
    num_tested += 1
    success = True

    # # check rows & columns
    # for row in grid:
    #     if len(row) != len(set(row)):
    #         success = False
    #
    # if success:
    #     for j in range(gridsize):
    #         column = [i[j] for i in grid]
    #         if len(column) != len(set(column)):
    #             success = False
    #
    # if not success:
    #     continue

    # check against instructions
    for key in instructions.keys():  # key = list(tuple(x,y))
        value = instructions[key]
        num, char = value[0], value[1]

        nums = []
        for tupl in key:
            nums.append(grid[tupl[0]][tupl[1]])

        if char == "+":
            if sum(nums) == num:
                continue
            else:
                success = False
                break
        elif char == "-":
            if abs(nums[0] - nums[1]) == num:
                continue
            else:
                success = False
                break
        elif char == "*" or char == "x":
            if math.prod(nums) == num:
                continue
            else:
                success = False
                break
        elif char == "/":
            if nums[0] / nums[1] == num or nums[0] / nums[1] == 1/num:
                continue
            else:
                success = False
                break

    if success:
        for row in grid:
            print(' '.join([str(elem) for elem in row]))
        endtime = datetime.utcnow()
        print(f"\nTested {num_tested} possibilities; Time taken: {(endtime - starttime).total_seconds()}s")
        exit()

print("\nNo possible answers found.")
endtime = datetime.utcnow()
print(f"Tested {num_tested} possibilities; Time taken: {(endtime - starttime).total_seconds()}s")
