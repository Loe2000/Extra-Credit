def sumFinder(array, target_sum):
    i = len(array)
    x = 0
    y = 0
    while x < i:
        while y < i:
            if ( x != y and array[x] + array[y] == target_sum ):
                return [array[x], array[y]]
            y += 1
        x += 1
        y = 0
    return 0
