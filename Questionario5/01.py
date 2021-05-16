def check(big, inner):
    for inner_vertex in inner:
        try:
            big_vertex = big[[vertex[0] for vertex in big].index(inner_vertex[0])]
            for value in inner_vertex[2:]:
                if value not in big_vertex[2:]:
                    return False
        except IndexError:
            return False
    return True


size_big = int(input())
big_graph = [[int(value) for value in input().split()] for _ in range(size_big)]
input()
size_inner = int(input())
inner_graph = [[int(value) for value in input().split()] for _ in range(size_inner)]
print('Sub-sub!' if check(big_graph, inner_graph) else 'Ue? Ue? Ue?')
