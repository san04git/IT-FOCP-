student = int(input("How many students?"))
group_size = int(input("required group size?"))

groups = students // group_size
leftover = students % group_size

print(f"There will be 22 with 1 student {'s' if leftover !=1 else ''} left over.")
