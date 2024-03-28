#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''1- Pretend that you have just opened a new savings account that earns 4 percent interest per year. The
interest that you earn is paid at the end of the year, and is added to the balance of the savings account.
Write a program that begins by reading the amount of money deposited into the account from the user.
Then your program should compute and display the amount in the savings account after 1, 2, and 3
years. Display each amount so that it is rounded to 2 decimal places.'''


# In[9]:


dep_amt = int(input("Welcome to your SenecaBank savings account. \n \nHow much would you like to deposit? : "))

interest_rate = 0.04
one_year_principal = (dep_amt * interest_rate)+dep_amt
one_year_principal_dep = "${:.2f}".format(one_year_principal)
one_year_principal_rounded = "${:.2f}".format(one_year_principal)
two_year_principal = (one_year_principal * interest_rate)+one_year_principal
two_year_principal_rounded = "${:.2f}".format(two_year_principal)
three_year_principal = (two_year_principal * interest_rate)+two_year_principal
three_year_principal_rounded = "${:.2f}".format(three_year_principal)

if dep_amt <= 0:
    print("Please deposit an amount greater than 0.")
else: 
    print(f'''Deposit successful. Your account has a 4% annual interest rate. Your projected savings growth is: \t \n
    Your current balance: {one_year_principal_dep} 
    After 1 year: {one_year_principal_rounded} 
    After 2 years: {two_year_principal_rounded}
    After 3 years: {three_year_principal_rounded}
    
Thank you for choosing SenecaBank. Have a nice day!''')


# In[10]:


'''2- Consider the software that runs on a self-checkout machine.
One task that it must be able to perform is to determine how much change 
to provide when the shopper pays for a purchase with cash. Write a program 
that begins by reading a number of cents from the user as an integer. 
Then your program should compute and display the denominations of the coins 
that should be used to give that amount of change to the shopper. 
The change should be given using as few coins as possible. 
Assume that the machine is loaded with pennies, nickels, 
dimes, quarters, loonies and toonies.'''


# In[11]:


cents = int(input(f'''Thank you for shopping at Seneca Mart.

How much change is required? Please input an amount 
in cents: '''))

num_toonies = cents // 200
num_loonies = (cents % 200) // 100
num_quarters = (cents % 200 % 100) // 25
num_dimes = (cents % 200 % 100 % 25) // 10
num_nickels = (cents % 200 % 100 % 25 % 10) // 5
num_pennies = (cents % 200 % 100 % 25 % 10 % 5)
coincount = num_toonies + num_loonies + num_quarters + num_dimes + num_nickels + num_pennies

"If change equals 0 then, exit"

if cents <= 0:
    print("Please deposit an amount greater than 0.")
    exit()
elif cents == 1:
    print("\nThe following coins will be dispensed:")
    print(f"Toonies: {num_toonies}")
    print(f"Loonies: {num_loonies}")
    print(f"Quarters: {num_quarters}")
    print(f"Dimes: {num_dimes}")
    print(f"Nickels: {num_nickels}")
    print(f"Pennies: {num_pennies}")  
    print(f"\nYou will receive {coincount} coin in total. Have a nice day!")
elif cents > 1:
    print("\nThe following coins will be dispensed:")
    print(f"Toonies: {num_toonies}")
    print(f"Loonies: {num_loonies}")
    print(f"Quarters: {num_quarters}")
    print(f"Dimes: {num_dimes}")
    print(f"Nickels: {num_nickels}")
    print(f"Pennies: {num_pennies}")  
    print(f"\nYou will receive {coincount} coins in total. Have a nice day!")


# In[12]:


'''Develop a program that begins by reading a number of seconds from the user. 
Then your program should display the equivalent amount of time in the form D:HH:MM:SS, 
where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. 
The hours, minutes and seconds should all be 
formatted so that they occupy exactly two digits, 
with a leading 0 displayed if necessary.'''


# In[13]:


time = int(input(
    f'''Welcome to the seconds calculator.\n 
Please enter a number of seconds you would like to 
convert to D:HH:MM:SS format: '''))
if time <= 0:
    print("Please enter more than 0 seconds.") 
    exit()

day     = time // (24 * 3600) 
hour    = (time // 3600) % 24
minutes = (time // 60) % 60
seconds = time % 60

print(f"\n{time} seconds is %d:%02d:%02d:%02d" % (day, hour, minutes, seconds))

if time > 3155695200:
    print("\nThat's over a century!")
elif time > 315569520:
    print("\nThat's over a decade!")
elif time > 31556952:
    print("\nThat's over a year!")
elif time > 2629746:
    print("\nThat's over a month!")
elif time > 604800:
    print("\nThat's over a week!")
elif time > 1800:
    print("\nThat's over half an hour!")
elif time < 300:
    print("\nThat's a few minutes!")


# In[ ]:




