# set
number_set = {1, 2, 3, 3}
print(number_set)

# data manipulation
number_set.add(5)
print(number_set)
number_set.remove(3)
print(number_set)

# union
union_set = number_set.union({1, 2, 100})
print(union_set)

# intersection
intersection_set = number_set.intersection({1, 2, 100})
print(intersection_set)