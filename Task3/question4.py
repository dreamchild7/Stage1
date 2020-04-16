import re
pass= input("Input your password")
a = True
while a:  
    if (len(pass)<6 or len(pass)>12):
        break
    elif not re.search("[a-z]",pass):
        break
    elif not re.search("[0-9]",pass):
        break
    elif not re.search("[A-Z]",pass):
        break
    elif not re.search("[$#@]",pass):
        break
    elif re.search("\s",pass):
        break
    else:
        print("Valid Password")
        a=False
        break

if a:
    print("Not a Valid Password")