
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name, encoding='UTF-8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:]
    else:
        return data

all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]
