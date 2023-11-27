# Create a function that receives three numbers and returns the highest of those three numbers.

def max(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > y and z > x:
        return z
    else:
        return x

print(max(100457, 100457, 100457))