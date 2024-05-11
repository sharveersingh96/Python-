# A number is called perfect if the sum of proper divisors of that number is equal to the number. 
# For example 28 is perfect number, since 1+2+4+7+14=28.
# Write a program to print all the perfect numbers in a given range:

# answer:

def perfect_number(low_range,High_range):
     print('perfect numbers are')
     for number in range (low_range,High_range):
          sum=0

          for j in range(1,(number//2)+1):
               if number%j==0:
                    sum=sum+j
                    
          if sum==number:
               print(number,end=" ")

low_range=int(input('enter min range'))
High_range=int(input('enter max range'))

perfect_number(low_range,High_range)
