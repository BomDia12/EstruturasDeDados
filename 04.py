import math


n_holes = int(input())

rabbit = [float(coordinate) for coordinate in input().split()]
fox = [float(coordinate) for coordinate in input().split()]
holes = [[float(coordinate) for coordinate in input().split()] for hole in range(n_holes)]

rabbit_distances = [math.sqrt((rabbit[0] - hole[0])**2 + (rabbit[1] - hole[1])**2) for hole in holes]
fox_distances = [math.sqrt((fox[0] - hole[0])**2 + (fox[1] - hole[1])**2) for hole in holes]

escaped = False
for i in range(n_holes):
    if rabbit_distances[i] < fox_distances[i] / 2:
        print(f'O coelho pode escapar pelo buraco ({holes[i][0]:.3f}, {holes[i][1]:.3f}).')
        escaped = True
        break

if not escaped:
    print('O coelho nao pode escapar.')
