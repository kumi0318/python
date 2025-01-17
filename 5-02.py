def sort(input_str):
    numbers = [int(char) for char in input_str]

    odd_numbers = sorted([num for num in numbers if num % 2 == 1], reverse=True)
    even_numbers = sorted([num for num in numbers if num % 2 == 0])

    result = ''.join(map(str, odd_numbers + even_numbers))
    
    return result


input_data = '417324689435'
output_data = sort(input_data)
print(output_data)  
# 輸出應為 '975331244468'