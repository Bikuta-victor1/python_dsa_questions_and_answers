import time
#for loop = conditional statement

# for i in range(10):
#     print(i+1)

# for i in "Adekola Victor":
#     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print('Happy New Year!')

# rows = int(input('How many rows?: '))
# columns = int(input('How many columns?:'))
# symbol = input('Enter a symbol to use:')

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end ='')
#     print()
#
# while True:
#     name = input('Enter your name: ')
#     if name != "":
#         break

# phone_number = "123-456-789"
#
# for i in phone_number:
#     if i == '-':
#         continue
#     print(i, end='')

# for i in range(10, 30):
#     if i % 7 == 0:
#         pass
#     else:
#         print(i)

# food = ['pizza', 'hamburger', 'hotdog', 'spag']
#
# food.append('ice-cream')
#
# for x in food:
#     print(x)

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate"}
#
# dinner_table = utensils.union(dishes)

# def hello(**kwargs):
#     # print('hello' + name)
#     print(kwargs.items())
#     # print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")
# hello(title="Mr.", first="Adekola", second="Victor")

# def searchMinimumFromList( L, n ):
#     minValue = L[0]
#     counter = 0
#     while(counter < n):
#         v = L[counter]
#         if (v < minValue):
#             min = v
#             i = counter
#         else:
#           pass
#     print(min+' '+i)
#     return min, i


# def reversewithQueries(arr, operations):
#     for i in range(len(operations)):
#         # for j in range(len(operations[i])):
#             newArr = reverse(arr, operations[i][0], operations[i][1])
#     return newArr
#
#
# def reverse(myarr, x, y):
#     while x <= y:
#         myarr[x], myarr[y] = myarr[y], myarr[x]
#         # print(x)
#         # print(y)
#         x += 1
#         y -= 1
#     print(myarr)
#     return myarr
#
#
# reversewithQueries([5, 2, 5, 1], [[1, 2], [1, 1]])

# reverse([5, 3, 2, 1, 3], 0, 1)

# def searchFromList(L, n):
#     minValue = L[0]
#     counter = 1
#     while counter < n:
#         v = L[counter]
#         if v < minValue:
#             minv = v
#             i = counter
#         else:
#             pass
#     return i, minv


# def sortList(L, n):
#     counter = 0
#     l2 = []
#     while counter < n:
#         print('Printing counter')
#         i, min = searchFromList(L, n)
#         print('Min and i')
#         print(i, min)
#         l2.append(min)
#         del L[i]
#         n = n-1
#         print(L)
#     print(l2)
#     return l2


# sortList([5, 2, 5, 1], 4)
