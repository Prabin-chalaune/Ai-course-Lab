#Name: Prabin Kumar Chalaune
#Roll no.:56
#Group:BCT | c

from collections import deque

def is_valid(state):

    # Checking if the goat and cabbage are left alone or the goat and wolf are left alone
    if (state[1] == state[3] and state[0] != state[1]) or (state[1] == state[2] and state[0] != state[1]):
        return False
    return True

# Function for Breadth-first search
def bfs():
    initial_state = ('west', 'west', 'west', 'west')
    goal_state = ('east', 'east', 'east', 'east')

    queue = deque()
    queue.append((initial_state, []))
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for item in ['G', 'F', 'W', 'C']:
            next_state = list(current_state)
            index = {'G': 1, 'F': 0, 'W': 2, 'C': 3}[item]

            if current_state[0] == 'west':
                next_state[0] = 'east'
            else:
                next_state[0] = 'west'

            next_state[index] = next_state[0]

            if tuple(next_state) not in visited and is_valid(next_state):
                visited.add(tuple(next_state))
                queue.append((tuple(next_state), path + [item]))

    return None

# getting the solution
solution = bfs()

if solution:
    actions = {'G': 'Goat', 'F': 'Farmer', 'W': 'Wolf', 'C': 'Cabbage'}
    print("Solution steps:")
    for i, step in enumerate(solution):
        if i == 0:
            print(f"- Take {actions[step]} across the river")
        elif i == 1:
            print(f"- Return {actions[step]} back")
        elif i == 2:
            print(f"- Take {actions[step]} across the river")
        elif i == 3:
            print(f"- Return {actions[step]} back")
        elif i == 4:
            print(f"- Take {actions[step]} across the river")
        elif i == 5:
            print(f"- Return {actions[step]} back")
        elif i == 6:
            print(f"- Take {actions[step]} across the river")
else:
    print("No solution found.")







