filenames = ['1.txt', '2.txt', '3.txt']
letters = ['a', 'b', 'c']

for filename, letter in zip(filenames, letters):
    with open(filename, 'w') as file:
        file.write(f"I am {letter}.")


for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)