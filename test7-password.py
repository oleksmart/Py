password = input("Enter the password: ")
result = []

#Lenght
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

#Digit
digit = False
for i in password:
    i.isdigit()
    digit = True
result.append(digit)

#Upper
upper = False
for i in password:
    i.isupper()
    upper = True
result.append(upper)




if all(result):
    print("Strong password")
else:
    print("Weak password")