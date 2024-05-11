# 4.Write a function prodDigits() that inputs a number and returns the product
#  of digits of that number

# Answer:

def prodDigits(number) :
    product =1
    while (number>=1):
        remainder= int(number%10)
        quotient=number//10 
        number=quotient
        product =product*remainder

    return  product
    
    
number =int(input('enter number'))
print('Product is ')
prodDigits(number)
