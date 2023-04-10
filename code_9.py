a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

# Sum of a_list
sum_manual = 0
for val in a_list:
    sum_manual += val

print(sum_manual)
print(sum(a_list))