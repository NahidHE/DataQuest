
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_rating_ft = freq_table(apps_data[1:],11)
print(content_rating_ft)
rating_ft = freq_table(data_set=apps_data[1:],index=8)
print(rating_ft)
genre_ft = freq_table(index=12, data_set=apps_data[1:])
print(genre_ft)