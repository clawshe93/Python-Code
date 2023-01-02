# 1) Set the emails variable to an empty dictionary

emails = {}

assert emails == {} 

# 2) Add 'Ashley', 'Craig' and 'Elizabeth' to the emails directory without reassigning the variable

emails['Ashley'] = 'ashley@example.com' 
emails['Craig'] = 'craig@example.com' 
emails['Elizabeth'] = 'elizabeth@example.com'

print (emails)

# 3) Remove 'Craig' from the emails dictionary without reassigning the varialbe

del emails['Craig']

print (emails)

# 4) Add 'Dalton' to the emails dictionary without reassigning the variable

emails['Dalton'] = 'dalton@example.com'

print (emails)

# 5) Return a list of keys from the emails dictionary as 'users'

users = list(emails.keys())
print (users)

# 6) Returna a list of values from the emails dictionary as 'email_list'


email_list = list(emails.values())
print (email_list)

# 7) Return a list of tuples called 'pairs' representing the key/value pairs in 'emails'

pairs = list(emails.items())
print (pairs)
