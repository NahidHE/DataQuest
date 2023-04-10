content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for rating in content_ratings:
    content_ratings[rating] = content_ratings[rating] / total_number_of_apps * 100

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = 100 - content_ratings['17+']

print('%.2f' %percentage_17_plus)
print('%.2f' %percentage_15_allowed)