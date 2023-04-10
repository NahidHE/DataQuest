opened_file = open('AppleStore.csv', encoding='utf-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(index):
    frequency_table = {}
    
    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

# FUNCTION
def freq_table(dataset, index):
    frequency_table = {}
    
    for row in dataset:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

user_rating = freq_table(apps_data[1:], 8)
print(user_rating)