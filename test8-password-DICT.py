password = input("Enter the password: ")
result = {}

#Lenght
if len(password) >= 8:
    result["lenght"] = True
else:
    result["lenght"] = False

#Digit
digit = False
for i in password:
    i.isdigit()
    digit = True
result["digit"] = digit

#Upper
upper = False
for i in password:
    i.isupper()
    upper = True
result["upper"] = upper


if all(result):
    print("Strong password")
else:
    print("Weak password")