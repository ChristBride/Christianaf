#python operators
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

c = 20
c += 30
d = 20
d -= 25
e = 10
e *= 3
f = 15
f /= 31
g = 20
g %=10
print(c)
print(d)
print(e)
print(f)
print(g)


h = 25
i = 4
print(h==i)
print(h!=i)
print(h>i)
print(h<i)
print(h>=i)
print(h<=i)

j = 5
k = 8
print ("my result is false", j<4 and k<9)
print ("my results is true", j==5 and k==8)
print ("my result is true", j<4 or k<9)
print ("my result is true", not (j<4 and k<9))
print ("my result is true", k>1 and j>3,
     "\nmy result is", not(k>1 and j>3))

l =  20
m = l
print(l is m)
print(l is not m)

n = 'apple'
print('apple' in n)
print('apple' not in n)
fruits = 'banana'
print('banana' in fruits)
print('banana'not in fruits)
if 'banana' in fruits:
    myfruits = fruits.upper()
    print(myfruits, len(myfruits))




