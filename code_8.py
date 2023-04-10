from csv import reader
opened_file = open('AppleStore.csv', encoding = 'utf-8')
read_file = reader(opened_file)
app_data = list(read_file)

rating_count_tot = []
for row in app_data[1:]:
    rating = int(row[6])
    rating_count_tot.append(rating)

max_rating_count = max(rating_count_tot)
min_rating_count = min(rating_count_tot)

print(max_rating_count)
print(min_rating_count)

frequencies = {'0 - 1K': 0, '1K - 1M': 0, 'Above 1M': 0}
for each in rating_count_tot:
    if each < 1000:
        frequencies['0 - 1K'] += 1
    elif each < 1000000:
        frequencies['1K - 1M'] += 1
    else:
        frequencies['Above 1M'] += 1

print(frequencies)


