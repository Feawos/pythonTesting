greeting = "Good Morning"
a = 4
# if greeting == " Morning":
if a < 2:
    print("condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition completed")

# for loop in python

obj = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in obj:
    print(i*3)

# sum of first natural numbers 1+2+3+4+5=15
# range(i,j) -> i to j-1
summation = 0
for j in range(1, 6):
    print(j)
    summation = summation + j
print(summation)

print("*******************************************************")
for k in range(1, 15, 5):
    print(k)
print("*********SKIPPING FIRST INDEX**********")
for m in range(10):
    print(m)