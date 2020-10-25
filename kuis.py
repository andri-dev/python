# a = 6
# b = 4

# c = "Hasilnya " + str (a + b) + "6" * 3

# print(c)

# a = True ** 6
# # b = "Hello" + 3" --> error
# c = "Hello" * 3
# d = "Ini adalah " + str(5) +  " dalam bentuk string."

# print(c)

# list_a = range(1,10,2)
# x = [ [a**2, a**3] for a in list_a]
# print(x)

a = 5.5
print(a, "is of type", type(a))

a=3; print(float(a))

d = "Dicoding"
print(d[3])

x = [10,15,20,25,30]
print(x[-3:])

y = 300
print(str(y).zfill(5))


for letter in 'Python':
    if letter.isupper():
        pass  
    else:
        print('Output: {}'.format(letter))