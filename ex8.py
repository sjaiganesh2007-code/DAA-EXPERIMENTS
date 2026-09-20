from itertools import permutations

INF = float('inf')

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF],
]
cities = ['A', 'B', 'C', 'D', 'E']
n = 5

best_cost = INF
best_path = None
for perm in permutations(range(1, n)):
    path = [0] + list(perm) + [0]
    c = sum(cost[path[i]][path[i + 1]] for i in range(n))
    if c < best_cost:
        best_cost = c
        best_path = path

print('5-City TSP - Cost Matrix:')
print(f'{"":>4}', ' '.join(f'{c:>5}' for c in cities))
for i, row in enumerate(cost):
    r = ['INF' if x == INF else str(x) for x in row]
    print(f'{cities[i]:>4}', ' '.join(f'{v:>5}' for v in r))

path_names = [cities[i] for i in best_path]
print(f'\nOptimal Tour: {" -> ".join(path_names)}')
print(f'Minimum Cost: {best_cost}')

print('\nPath verification:')
for i in range(len(best_path) - 1):
    u, v = best_path[i], best_path[i + 1]
    print(f'  {cities[u]} -> {cities[v]}: cost = {cost[u][v]}')
