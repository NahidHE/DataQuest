content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_rating_percentages = {}

for rating in content_ratings:
    proportion = content_ratings[rating] / total_number_of_apps
    c_rating_percentages[rating] = proportion

print(content_ratings)
print(c_rating_percentages)