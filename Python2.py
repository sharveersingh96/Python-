#  2. Write a program to calculate the sum of series up to n term.
# For example, if n =5 ,the series will become 2 + 22 + 222 + 2222 + 22222 = 24690



# Answer:

number = int(input('Enter the number'))
number_of_terms = int(input('Enter number of terms'))
number2=int(number)

def sum_of_series(number,number_of_terms,number2):
    sum = 0
    for i in range(0, number_of_terms):
        print(number,'+', end=' ')
        sum += number
        number = (number * 10) + number2
    print('\nSum of a series is =', sum)
        
        
sum_of_series(number,number_of_terms,number2)
