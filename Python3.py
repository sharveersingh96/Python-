# 3 Write a program to find out the prime factors of a number

# Answer:

number =int(input('enter the number'))
list=[]
for i in range(2,number+1):
    if number%i==0:
        
        list.append(i)
        
print('\nfactors are ',list)

list2=[]

for i in list:
    count =0
    for j in range (2,i):
        if i%j==0:
            count=count+1
            break
            
    if count==0:
            list2.append(i)   
            
print('\nprime factors are')
print(list2)
