for i in range(1, 101):
    print(i)


# 1-100 even number
for i in range(2 , 101, 2):
    print(i)

# 1-100 odd number
for i in range(1 , 101, 2):
    print(i)


#triangle

num_rows = 10

for i in range(num_rows):
    for i in range(i + 1):
        print("*", end="")

    print()