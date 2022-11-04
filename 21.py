# list1=[10,20,[300,400,[5000,6000],500],30,40]
# # write a program to add item 7000 after 6000 in the above python list



# list1.insert(3,7000)

# # print(list1,7000)
# # print(list1)
# list1=["Hello","take"]
# list2=["Dear","sir"]

# for x in list1:
#     for y in list2:
#         print
b=[10,20,[300,400,[5000,6000],500],30,40]

m=[7000]

reformed=[]

x=0

while x != len(b):
	
	if  type(b[x]) == list:
		
		for i in b[x]:
			
			if (type(i) == list) and i[-1]==6000:
				
				i.extend(m)
				
				reformed.extend([b[x]])
				
				#used  [b[x]] which is same has list(b[x]) because extend requires a data type list and not any other data type
				
				
	else:
		
		reformed.extend([b[x]])
	
	
	x+=1

print(reformed)
