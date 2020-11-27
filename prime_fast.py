"""
Created on Fri Nov 27 09:01:05 2020

"""

a = int(input("Enter your number.: "))
if a <= 1:
    print("Not a prime, please input positive integers >1")
elif a==2:
    print("Its the only even prime number.")
else:
    for num in range(2,a):
            if a % num ==0 :                                       #coded by Manish Agrahari
                print(f"Entered {a} is not prime number.")
                break
            elif num == (a//2)+1:                    ## I used // instead of / to get integral values
                print("Entered number is prime.")    ## remeber prime numbers are odd except 2, so to check for odd prime numbers we require to add 1 in a/2 otherwise it will beome a fractional and will never become equal to num
                break
    
