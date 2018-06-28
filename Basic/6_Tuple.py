tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida');
tup2 = (1, 2, 3, 4, 5, 6, 7);
print(tup1[0])
print(tup2[1:4])
print("LENGTH : ", tup2.__len__())
print("ANY : ", tup2.count())

# Packing & Unpacking
print(" ------ Packing & Unpacking ----")
x = ("Guru99", 20, "Education")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print(company)
print(emp)
print(profile)
print(" ------ Comparing tuples ----")
# Comparison starts with a first element of each tuple
a = (5, 6)
b = (1, 4)
if (a > b):
    print("a is bigger")
else:
    print("b is bigger")

a = (5, 4)
b = (5, 6)
if (a > b):
    print("a is bigger")
else:
    print("b is bigger")

a = {'x': 100, 'y': 200}
b = list(a.items())
print(b)
