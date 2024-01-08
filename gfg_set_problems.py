#*********************************************** Set *********************************************************


# Python – Maximum and Minimum in a Set

# Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
# Output : max is 65

set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
set1={8, 16, 24, 1, 25, 3, 10, 65, 55}
print(max(set))
print(min(set1))





# Python – Remove items from Set


# Input : set([12, 10, 13, 15, 8, 9])
# Output :
# {9, 10, 12, 13, 15}
# {10, 12, 13, 15}
# {12, 13, 15}
# {13, 15}
# {15}

set={12, 10, 13, 15, 8, 9}
print(set.pop())




# Python – Check if two lists have at-least one element common

# Input : a = [1, 2, 3, 4, 5]
#         b = [5, 6, 7, 8, 9]
# Output : True

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
for i in a:
    if i in b:
        print(f"Yes atleast one element is common that element is {i}")



# Python program to find common elements in three lists using sets

#
# Input : ar1 = [1, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# Output : [80, 20]

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

# Calculates intersection of
# sets on s1 and s2
set1 = s1.intersection(s2)  # [80, 20, 100]

# Calculates intersection of sets
# on set1 and s3
result_set = set1.intersection(s3)

# Converts resulting set to list
final_list = list(result_set)
print(final_list)






# Python – Find missing and additional values in two lists

#
# Input : list1 = [1, 2, 3, 4, 5, 6]
#         list2 = [4, 5, 6, 7, 8]
# Output : Missing values in list1 = [8, 7]
#          Additional values in list1 = [1, 2, 3]
#          Missing values in list2 = [1, 2, 3]
#          Additional values in list2 = [7, 8]

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
s1=(set(list1))
s2=(set(list2))
print(f"Additional values in list1 {list(s1.difference(s2))} ")


for i in list2:
    if i not in list1:
        print(i)




