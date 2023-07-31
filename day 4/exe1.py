import random

#name_string = input("Give me Everybody's names, separated by a comma:\n")
name_string = "David, onyi, ken, mose,mikal, muricho"
name = name_string.split(",")

len_list_name = len(name)

person_index = random.randint(0, len_list_name-1)

person_to_pay = name[person_index]

print(f"{person_to_pay} will pay the bill")


