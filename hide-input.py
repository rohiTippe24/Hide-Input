# HIDE USER INPUT IN PYTHON WITH GETPASS MODULE

#import getpass module
import getpass

# Take normal user input
name = input(" Username :~  ")

# get input with getpass
# in getpass prompt = "string" == input( " string" );
password = getpass.getpass(prompt='Password :~  ')

# Print user inputs
print(" user name is :- " + name )
print(" password is :- " + password )
