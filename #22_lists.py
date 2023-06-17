marks = [45, 66, 99, "sagar", True]
# print(marks)     # or print(marks[:])
# print(marks[0])
# print(marks[1])
# print(marks[3])
# print(marks[4])

print(marks[-3])   # size - 3
print(marks[len(marks) - 3])

if 7 in marks:
    print("Yes")
else:
    print("No")

# if "arry" in "Harry":
#     print("Yes")
# else:
#     print("No")

print(marks[1:4:2])

# List Comprehension

lst = [i for i in range(4)]
print(lst)

lst1 = [i*i for i in range(5)]
print(lst1)

lst2 = [i*i for i in range(10) if i%2==0]
print(lst2)
