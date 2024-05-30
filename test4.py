waiting_list = ["sen", "ben", "john"]
waiting_list = sorted(waiting_list)
for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

