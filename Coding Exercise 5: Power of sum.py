

def power_of_sum(array,power=1):
    sum = 0
    for ele in array:
        if type(ele) == list:
            sum = sum + power_of_sum(ele,power+1)
        else:
            sum = sum + ele
    return sum ** power

print(power_of_sum([1,2,[3,4],[[2]]]))