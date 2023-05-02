def inde(num):
        if len(str(num)) == 8:
            return 0
        for i in range(9):
            x = num % 10
            num = int(num/10)
            if x == 0:
                break
        return 8 - i

def swap(que, a, b):
        tem1 = list(que)
        tem = tem1[a]
        tem1[a]=tem1[b]
        tem1[b]= tem
        return ''.join(tem1)

def make_move(slot):
        tem = slot
        val = inde(slot)
        solution = []
        index = str(slot)
        if len(index) == 8:
            index = '0' + index
        if val == 0:
            end = swap(index, val, 1)
            solution.append([int(end), slot])

            end = swap(index, val, 3)
            solution.append([int(end), slot])
        if val == 1:
            end = swap(index, val, 0)
            solution.append([int(end), slot])

            end = swap(index, val, 2)
            solution.append([int(end), slot])

            end = swap(index, val, 4)
            solution.append([int(end), slot])
        if val == 2:
            end = swap(index, val, 1)
            solution.append([int(end), slot])

            end = swap(index, val, 5)
            solution.append([int(end), slot])

        if val == 3:
            end = swap(index, val, 0)
            solution.append([int(end), slot])

            end = swap(index, val, 4)
            solution.append([int(end), slot])

            end = swap(index, val, 6)
            solution.append([int(end), slot])
        if val == 4:
            end = swap(index, val, 1)
            solution.append([int(end), slot])

            end = swap(index, val, 3)
            solution.append([int(end), slot])

            end = swap(index, val, 5)
            solution.append([int(end), slot])

            end = swap(index, val, 7)
            solution.append([int(end), slot])

        if val == 5:
            end = swap(index, val, 2)
            solution.append([int(end), slot])

            end = swap(index, val, 4)
            solution.append([int(end), slot])

            end = swap(index, val, 8)
            solution.append([int(end), slot])

        if val == 6:
            end = swap(index, val, 3)
            solution.append([int(end), slot])

            end = swap(index, val, 7)
            solution.append([int(end), slot])
        if val == 7:
            end = swap(index, val, 4)
            solution.append([int(end), slot])

            end = swap(index, val, 6)
            solution.append([int(end), slot])

            end = swap(index, val, 8)
            solution.append([int(end), slot])

        if val == 8:
            end = swap(index, val, 5)
            solution.append([int(end), slot])

            end = swap(index, val, 7)
            solution.append([int(end), slot])

        return solution

def displayS(number):
    print("------------")
    tem = str(number)
    tem = [i if i is not '0' else " " for i in tem ]
    board = [tem[0:3], tem[3:6], tem[6:]]
    for row in board:
        row = [str(i) for i in row]
        print (" | ".join(row))
        print("-----------")

from collections import deque
def find(start):
    q = []
    graph = {}
    q += [start]
    searched = []
    level = []
    depth = 0
    all_paths  = {}
    all_paths[start] = [start]
    while q:
        pos = q.pop(0)
        if not pos in searched:
            if  pos == 123456780:
                for state in all_paths[pos]:
                    displayS(state)
                print('depth', depth)
                return True
            else:
                tem = [i[0] for i in make_move(pos)]
                level += tem
                graph[pos] = tem
                for j in tem:
                    all_paths[j] = all_paths[pos] + [j]              

            searched.append(pos)
        if not q:
            q = []
            q +=level
            level = []
            depth += 1
    return False


start = input("시작상태를 입력하세요: ")
start = int(start.replace(" ", ""))
find(start)
