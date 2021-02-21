def remove_duplicatas(lst):
    result = []
    for item in lst:
        result.append(item) if item not in result else item
    return result

if __name__ == '__main__':
    print(remove_duplicatas([1,1,2]))
