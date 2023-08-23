from collections import Counter

my_list = ['A', 'A', 'B', 'C', 'B', 'B']
counter = Counter(my_list)

min_count = min(counter.items())
print("Minimum count:", min_count)
