import math

numbers = [0, 1]
even_numbered_list = []

while numbers[0] < 4000000:
    summation = numbers[0] + numbers[1]
    numbers[0] = numbers[1]
    numbers[1] = summation
    divided_number = numbers[1]/2
    if divided_number - math.trunc(divided_number) == 0:
        even_numbered_list.append(numbers[1])
    print(numbers[1])
#print(even_numbered_list)
total_value = sum(even_numbered_list)
print(total_value)