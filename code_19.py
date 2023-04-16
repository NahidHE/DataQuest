def pythagorean(a, b):
    a_square = a ** 2
    b_square = b ** 2
    c_square = a_square + b_square
    return a_square, b_square, c_square

pythagorean(5, 12)

# Check output:
data = pythagorean(5, 12)
print(data) # tuples type

