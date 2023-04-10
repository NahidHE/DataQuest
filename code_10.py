ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_rating = {}
for rating in ratings:
    if rating in content_rating:
        content_rating[rating] += 1
    else:
        content_rating[rating] = 1

print(content_rating)