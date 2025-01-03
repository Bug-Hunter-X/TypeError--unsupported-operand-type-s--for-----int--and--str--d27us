def function(a, b):
    return str(a) + str(b)

result = function(5, "10")
print(result) # Output: 510

def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Inputs must be integers."

result = function(5, "10")
print(result) # Output: 15
result = function("5", "10")
print(result) # Output: 15
result = function("a", "10")
print(result) # Output: Error: Inputs must be integers.