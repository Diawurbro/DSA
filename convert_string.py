'''main'''
def convert_string_to_tuples(text_in):
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

laongdao_data = convert_string_to_tuples(input())

def swap_tuple_values(data):
    return (data[1], data[0])

result = swap_tuple_values(laongdao_data)
print(result)
