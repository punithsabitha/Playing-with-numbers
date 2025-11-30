# Takw input fromm the user
number = int(input("Enter your number: "))

# store original number for comparision later
original_number = number
reversed_number= 0

# reverse the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 +digit
    number //= 10

# check  if reversed number and original number are the same
if original_number == reversed_number:
    print(f"{original_number} is a palinndrome")
else:
     print(f"{reversed_number} is not a palinndrome")
