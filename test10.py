feet_inches = input("Enter feet and inches: ")
parcers = "modules\parcers10"

#from parsers10  var 1
from modules.parsers10 import parse
from modules.convertors10 import convert

#parsed = parsesrs10.parse(feet_inches) var 1

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed["inches"])


print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

    