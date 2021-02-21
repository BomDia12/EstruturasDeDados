import math


total_bytes = int(input())
transferred, tick, latest = 0, 0, []

print(f'Transmitindo {total_bytes} bytes...')

while transferred < total_bytes:
    latest.append(int(input()))
    tick += 1
    transferred += latest[-1]
    if tick % 5 == 0 and not transferred >= total_bytes:
        if sum(latest) / len(latest) > 0:
            time_left = (total_bytes - transferred) / (sum(latest) / len(latest))
            print(f'Tempo restante: {math.ceil(time_left)} segundos.')
        else:
            print('Tempo restante: pendente...')
        latest = []

print(f'Tempo total: {tick} segundos.')
