avg_price = None
avg_rating = None

opened_file = open('AppleStore.csv', encoding= 'utf8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list: #BUG: Semicolon needed
        a_sum += float(element) #BUG: element should be converted to float
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column) #BUG: find_sm() should be find_sum() instead

avg_price = mean(apps_data, 5)
avg_rating = mean(apps_data, 8)

print(avg_price)
print(avg_rating)