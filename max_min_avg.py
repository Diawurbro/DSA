import json

def main():

    input_data = input()
    my_list = json.loads(input_data)

    highest = my_list[0]
    lowest = my_list[0]
    total_sum = 0
    count = 0

    for score in my_list:

        if score > highest:
            highest = score
        
        if score < lowest:
            lowest = score
            
        total_sum += score
        count += 1

    average = total_sum / count
    result = (
        round(highest, 2), 
        round(lowest, 2), 
        round(average, 2)
    )

    print(result)

if __name__ == '__main__':
    main()
