# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)

# def loop_number(n):
#     numbers = []
#     i = 0

#     while i < n:
#         print(f"At the top i is {i}")
#         numbers.append(i)

#         i += 1
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")

#     print("The numbers: ")
#     for num in numbers:
#         print(num)

# loop_number(6)

def loop_number(n):
    numbers = []

    for i in range(n):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i + 1}")

    print("The numbers: ")
    for num in numbers:
        print(num)

loop_number(6)