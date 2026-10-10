count = 1
total = 0

# BUG: the while line was missing a colon at the end, so Python raised a SyntaxError. I added the ':' at the end of the line.
# BUG: the condition count < 5 stopped the loop before adding 5, so the sum was 10 with no error. I changed < to <= so 5 is included.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer and "Sum of 1 to 5 is: " is a string, so + raised a TypeError. I converted total with str(total).
print("Sum of 1 to 5 is: " + str(total))