date = input("Enter today's date: ")
mood = input("Rate you mood ")
journal = input("How are you today: \n")

with open(f"files/{date}.txt", "w") as file:
    file.write(mood + 2 *"\n")
    file.write(journal)