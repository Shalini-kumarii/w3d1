# print 0 to 150
for x in range(151):
    print("values are: "+ str(x))
# print multiple of 5
for x in range(5,1000):
    if x % 5 ==0:
        print("multiple of 5 is: "+ str(x))

# print coding divisible by 5 else codingdojo divisible by 10
for x in range(0,100,1):
    if x % 5 ==0 and x % 10 !=0:
        print("Coding")
    elif x % 5 ==0 and x % 10 ==0:
        print("CodingDojo")
    else:
        print(x)

# sum of odd from 0 to 500000 
sum =0
for x in range(0,500000):
    if x % 2 !=0:
        sum = sum + x

print("sum is: "+str(sum))

# countdown by 4
for x in range(2018,0,-4):
    print("numbers countdown by 4: "+ str(x))

#flexible counter
low_num=2
high_num=9
mult= 3
for x in range(low_num,high_num+1):
    if low_num % mult==0:
        print(low_num)
    low_num = low_num+1

b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
