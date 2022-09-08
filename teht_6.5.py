def running_sum(iterable):
    s = 0
    result = []
    for value in iterable:
         s += value
      result.append(s)
    return result

running_sum([1,2,3,4,5])
[1, 3, 6, 10, 15]