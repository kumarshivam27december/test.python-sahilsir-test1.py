# find the sum of the series upto n terms

'''write a program to calculate the sum of series upto n terms. 
for example , if n=5 the series will become 2 +22+222+2222+22222=24690'''

number_of_terms = 5
sum1=0
for i in range (1,number_of_terms+1):
    num=eval('2'*i)
    sum1+=num
print(sum1)