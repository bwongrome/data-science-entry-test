def swap(x, y):
    
    return {"first": y, "second": x}


result = swap ("Apple",10)
x,y = result["first"], result["second"]
print(f"x = {x}, y = {y}")


result = swap (9,17)
x,y = result["first"], result["second"]
print(f"x = {x}, y = {y}")