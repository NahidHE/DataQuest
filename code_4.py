from csv import reader
opened_file = open('AppleStore.csv', encoding= 'UTF8')
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}
for row in apps_data[1:]:
    genre = row[12]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
print(genre_counting)

# Extra Work
popular_genre = ''
max_download = 0
for genre in genre_counting:
    if  genre_counting[genre] > max_download:
        popular_genre = genre
        max_download = genre_counting[genre]
print('Most Popular Genre: ', popular_genre,' Downloads: ',max_download)

