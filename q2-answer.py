def find_and_replace(lst, find_val, replace_val):
    for i in range(len(lst)):
            if lst[i] == find_val:
                lst[i] = replace_val
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

original = [1, 2, 3, 4, 2, 2]
find_and_replace (original,2,5)
print(original)

[1, 5, 3, 4, 5, 5]

original = ["apple", "banana", "apple"]
find_and_replace (original,"apple","orange")
print(original)

['orange', 'banana', 'orange']
