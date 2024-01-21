#Write a program to remove duplicates from a given list.
'''
input_list = [1, 2, 3, 2, 6, 3, 5, 3, 7, 8, 3, 4, 2, 1]
output_list = set(input_list)
print("The input list is: ", input_list)
print("The output list after removing duplicates is: ", output_list)
'''

#Create a function that returns the intersection of two lists.
'''
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [4, 5, 6, 7, 8, 9]
print("The first list is: ", lst1)
print("The second list is: ", lst2)
print("The intersection of the two lists is: ", intersection(lst1, lst2))
'''
 
#Generate a list of squares of numbers from 1 to 10
''' 
squares = [i**2 for i in range(1, 11)]
print("The list of squares of numbers from 1 to 10 is: ", squares)
'''

#Create a list of words that have more than 5 characters from a given list of words
'''
l1 = ["indresh", "surya", "sanjay", "arun", "prathap"]
l2 = [word for word in l1 if len(word) > 5]
print("The input list is: ", l1)
print("The output list of words with more than 5 characters is: ", l2)
'''



