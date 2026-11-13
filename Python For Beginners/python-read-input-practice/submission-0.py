def add_two_numbers() -> int:
    user_input = input()
    sum = 0
    my_list = [int(x) for x in user_input.split(",")]
    for i in range(len(my_list)):
        sum += my_list[i]
    return sum
    
   
    





# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
