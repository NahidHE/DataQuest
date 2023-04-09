from csv import reader
opened_file = open('AppleStore.csv', encoding= 'UTF8')
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}
for row in apps_data[1:]:
    c_rating = row[11]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
print(content_ratings)