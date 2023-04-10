from csv import reader
opened_file = open('AppleStore.csv', encoding= 'UTF-8')
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    data = []
    for row in apps_data[1:]:
        data.append(row[index])
    return data

prime_genre = extract(12)

# print(prime_genre)


## Next Part: Creating Frequency Tables

def freq_table(data):
    frequency_table = {}
    for item in data:
        if item  in frequency_table:
            frequency_table[item] += 1
        else:
            frequency_table[item] = 1
    return frequency_table

genre_ft = (freq_table(extract(12)))
# print(genre_ft)

## Next Part: Writing a Single Function
user_rating = freq_table(extract(8))
# print(user_rating)