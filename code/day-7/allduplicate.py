def Print(list1):

    final_list = []
    for num in range(len(list1)):
        i = num + 1

        for i in range(i, len(list1)):
            if list1[num]== list1[i]:
                final_list.append(list1[num])

    return final_list

# Driver Code
list1 = [2, 4, 10, 20, 5, 2, 20, 4]
print(Print(list1))
