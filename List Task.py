# Write a program 
# Input:
#    list1=[10,20,[30,40,[50,60],80],90,100]
# Output:
#    [10, 20, [30, 40, [50, 60, 70], 80], 90, 100]


list1=[10,20,[30,40,[50,60],80],90,100]
list1[2][2].append(70)
print(list1)

# Input:
#    list2=[1,2,[3,4,5,6,7,8],11,12]
# Output:
#   [1, 2, [3, 4, 5, 6, 7, 8, [15, 20, 30]], 11, 12]


list2=[1,2,[3,4,5,6,7,8],11,12]
list2[2].append([9,10])
print(list2)
