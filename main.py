nums = {"a": 1, "b": 2, "c": 3, "d": 4}

even = {k: v for k, v in nums.items() if v % 2 == 0}
print(even)


d = {"a": 1, "b": 2, "c": 3}

rev = {v: k for k, v in d.items()}
print(rev)
