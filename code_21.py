
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name, encoding= 'UTF-8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data

apps_data, header = open_dataset()
