#!/anaconda3/bin/python

from datetime import datetime, date
# import filename - to import pythin file with functions
# https://docs.python.org - for python library

print("VARIABLES")
is_sunny = False
if not(is_sunny):
    print("its not sunny")

print("LIST - functions >> extend, append, insert, copy, len")
arr = ["08","07","05"]
print(arr[2])
print(arr[1:3])
print(arr[2][1])
for a in arr:
    print(a)
for i in range(len(arr)):
    print(arr[i])

m = min(arr[2], arr[0])
print(m)
print(type(m))

arr.sort()
print(arr)

print("\nTUPLE - its immutable. Functions >> ")
t = (3, 4, 7)
print(t[2])
c = [(9,6),(3,1),(5,7)]
print( c[1][1])

print("\nDICTIONARY - Functions >> ")
months = {
    1: "Jan",
    3: "Mar",
    5: "May",
    12: "Dec"
}
print(months.keys())
print(months.items())
print(months.get(3))

print("\nIF ELSE - ")
is_male = False
is_female = False
if is_male:
    print("it's a male")
elif is_female:
    print("it's a female")
else:
    print("it's undetermined")

print("\nFUNCTION  ")
def add(a, b):
    return a+b
# a = float(input("enter a:"))
# b = float(input("enter a:"))
a=3
b=7
print(add(a,b))

print("\nWHILE - ")
a = 5
b = 7
while a < 10 and b < 10:
    print( add(a,b))
    a += 1
    b += 1
    

print("\nGRID - ")
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in grid:
    print(row)
    print(row[1])
    
    
print("\nTRY Except - ")
try:
#    value = 10/0
    n = int(input("Enter a number:"))
    print(n)
except ZeroDivisionError:
    print("divide by zero")
except ValueError:
    print("value error")
except NameError:
    print("name error")
        
print("\nFile - modes include read/write/append r/w/a")
sample_file = open("sample.txt", "r")
print(sample_file.name)
# every readline call takes the cursor forward
print(sample_file.readline())
print(sample_file.readlines()[1])
sample_file.close()
sample_file = open("sample.txt", "a")
sample_file.write("\nlast line")
sample_file.close()