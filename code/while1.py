#  to dispaly 10 times name
"""
name=input("Enter the name =")
x=0
while x<10:
    print(name)
    x+=1
    """

# to display 1 to 10
"""

n=1

while n<=10:
    print(n)
    n+=1
"""
# to print the table of user input no.

"""
n=int(input("Enter the no.="))
x=1
while x <= 10:
   
   print(f"{n} * {x} = { n * x}")
   x=x+1

"""
# calculate the sum of n natural no.
"""
x=int(input(" Enter the number="))
n=0
z=1
while z<=x:
    n+=z
    z+=1
    
print(n)
   

# Creating a Countdown Timer

import time
n=int(input("Enter the time start="))
while n>0:
  print(n)
  time.sleep(1)
  n -=1
  
print("Times up !")
"""
"""
# printing even no. up to N

N= int(input(" Enter the number=="))
x=2
while x<=N:
    if x%2 == 0:
        print(x)

    x += 1
    
 
# Generating the Fibonacci Sequence
num=int(input("Enter the value=="))
x=0
y=1

while x<=num:
    print(x)
    z=x+y
    x=y
    y=z
    """