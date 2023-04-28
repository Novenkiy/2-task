array1 = [1, 4, 7, 21, 19, 5, 6, 11, 9]
sum = 0
sumar = 0
for i in range(len(array1)):
    sum  += alfa[i]
    sumar = sum/len(array1)
print(array1)
print(sumar)



sumi = 0
array2 = array1[::2]
print(beta)
for i in range(len(array2)):
    sumi  += array2[i]
print(sumi)



from functools import reduce
array3 = array1[::4]
print(array3)
print(reduce(lambda x, y: x*y, array3))
