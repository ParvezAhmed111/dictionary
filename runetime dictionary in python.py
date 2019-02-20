#program to create a runetime dictionary in python
x=int(input("Enter the size of dictionary: "))
d={}
for i in range(x):
    key=input("Enter the key: ")
    value=input("Enter its value: ")
    d.update({key:value})
print("Dictionary is: ", d)

