n_vertices, n_connections, graph_type = input().split()
n_vertices, n_connections = int(n_vertices), int(n_connections)
matrix = [[0 for j in range(n_vertices)] for i in range(n_vertices)]
for i in range(n_connections):
    x, y, value = map(int, input().split())
    if graph_type == 'D':
        matrix[x - 1][y - 1] = value
    else:
        matrix[x - 1][y - 1], matrix[y - 1][x - 1] = value, value

output = [''.join([f'{value:4}' for value in vertex]) for vertex in matrix]
[print(line) for line in output]
