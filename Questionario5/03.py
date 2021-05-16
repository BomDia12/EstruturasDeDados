def process_command(graph, command):
    if command[0] == 'IV':
        graph[command[1]] = []
        return graph

    if command[0] == 'RV':
        if command[1] in graph.keys():
            graph.pop(command[1])
        for key in graph.keys():
            if command[1] in graph[key]:
                graph[key] = list(filter(lambda x: x != command[1], graph[key]))
        return graph

    if command[1] in graph.keys() and command[2] in graph.keys():
        if command[0] == 'IA':
            graph[command[1]].append(command[2] if command[2] not in graph[command[1]] else None)
            graph[command[2]].append(command[1] if command[1] not in graph[command[2]] else None)
            return graph

        if command[2] in graph[command[1]]:
            graph[command[1]].pop(graph[command[1]].index(command[2]))
            graph[command[2]].pop(graph[command[2]].index(command[1]))
    return graph


n = int(input())
commands = [input().split() for _ in range(n)]
graph = {}
for command in commands:
    graph = process_command(graph, command)

print(max([len(graph[vertex]) for vertex in graph]) if graph else 0)
