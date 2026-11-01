#LOOP solvimg assainment

#1/FizzBuzz

num=int(input("chose tha number "))
for i in range(1,101):
    if num/3:
        print("Fizz")
    elif num/5:
        print("Buzz")
    elif num/3 and num/5:
        print("FizzBuzz")
    else:
        ("invalid number")

#3/ Number Reverser

num=int(input())
cnt=0
while num>0:
    ldigit=num%10
    cnt=cnt+ldigit
    num//=10
    print(num)

#4/sum of Digits

num=int(input())
cnt=0
while num>0:
    num//=10
    cnt+=1
print(cnt)

#6/fibonacci sequence

num=int(input())
sum1=0
sum2=1
cnt=0
while cnt<num:
    print(sum1)
    update=sum1+sum2
    sum1=sum2
    sum2=update
    cnt+=1
    
#7/password rety

passw=12345

for i in range(3):
    user=int(input())
    if user==passw:
        print("login succfull")
        break
else:
    print("locate")

#8/ Guss the number game(whil loop)

user=int(input("guss the number 1 to 10: "))
guss=5
while user<=guss:
    if user>guss:
        print("too high")
        break
    elif user<guss:
        print("too low")
        break
    else:
        print("corret")
        break