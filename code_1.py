content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = '987' in content_ratings
if '17+' in content_ratings:
    result = "It exists"
print(result) # May cause error when condition is False!

# Custon Code to understand
print('# Custom Output ')
print(is_in_dictionary_1)
print(is_in_dictionary_2)
print(result)