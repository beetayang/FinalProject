'''
Created on Feb 16, 2018

@author: ITAUser
'''
user_input = int(input('Enter an integer:'))
if user_input > 0: 
    x = 1 
    counter = 0 
    
    while x <= user_input:
        remainder = user_input % x 
        
        if remainder == 0: 
            counter = counter + 1 
            
        x = x + 1 
    if counter == 2:
        print(str(user_input) + " is a prime number")
    else:
        print (str(user_input) + " is not a prime number")
    
else:
    print('Number must be greater than 0')
    
    
    
    
