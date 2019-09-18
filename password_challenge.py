import random
#import time
#import sys
#sys.setExecutionLimit(60000) # 60 seconds
#Explore the time module - there may be a function that can be used to limit the time the while loop will run.

my_password = "abcd"
guess_num = 0
done = False
while not done:

    guessed_pw = ""
    # your code here

    if guessed_pw == my_password:
        print("found it after ", guess_num, " tries")
        done = True
