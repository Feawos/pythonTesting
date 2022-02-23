values = [1, 2, "Femi", 4, 5]
# List is data type that allows multiple values and data types

print(values[0])  # 1

print(values[3])  # 4
print(values[-1])  # 5
print(values[2])  # Femi
print(values[1:3])  # 2,Femi

# add new value to list
values.insert(3, "Awosanya")
print(values)

# add new value to end of list
values.append("winner")
print(values)

# delete value from list
del values[0]
print(values)

values.insert(0, 1)
print(values)

# Tuple - same as list but immutable
val = (1, 2, "Femi", 4, 5)
print(val[1])

# val[2] = "FEMI"

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello World"}
print(dic[4])
print(dic["c"])

dict = {}

dict["firstname"] = "Femi"
dict["lastname"] = "Awosanya"
dict["gender"] = "Male"

print(dict)
print(dict["lastname"])
