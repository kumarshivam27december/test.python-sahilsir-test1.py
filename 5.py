# divisible by five 
#  no greater than 150  skip
# no greater than 500,stop the loop

# a=int(input("enter your number: "))
# num = range(0,500)

# if a%=5:
#     print()


# if a>150:
#     pass
# else a<500:
  
# for x in range(0,500):
#     if x<150:break
#     print(x)
# else:
#     print("stop the loop")
x=int(input("enter your number: "))
while x%5==0:
    x+=1
    if x>500:
        continue
    print(x)
else:
    print("the loop is over")
        
       
















  