n = int(input("Please enter the number of row: "))
# Print half Pyramid
for i in range(n+1):
    print(i * "* ")

print()

# Print Inverted half pyramid
for i in range(n, 0, -1):
    print(i * "* ")

print()

# Print hollow inverted half pyramid
print(n * "* ")
for i in range(n-3, -1, -1):
    print("* " + i * "  " + "*")
print("*")

# Print full pyramid
for i in range(n+1):
    print((n-i) * " " + i * "* ")