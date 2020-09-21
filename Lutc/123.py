a = 4
print(a, id(a))
a = 10.2
print(a, id(a))
b = 10.2
print(b, id(b), "\n")


a = [1, 2]
print(id(a))
print(id(a[0]), id(a[1]), "\n")

a[1] = 3
print(id(a))
print(id(a[0]), id(a[1]), "\n")

for el in a:
    print(id(el), el)
    el += 100
    print(id(el), el, "\n")
print("\n")
# for i in range(0, 2):
#    print(id(a[i]))

print(a)



