def update_dictionary(dct, key, value):
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

my_dct = {"name": "Alice","age": 25}
result = update_dictionary(my_dct,"age", 26)
print(result)

#{'name': 'Alice', 'age': 26}