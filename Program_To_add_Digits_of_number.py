# Input a number
num = int(input("Enter a number: "))

# Convert number to string and sum digits
digit_sum = sum(int(digit) for digit in str(num))

print("Sum of digits: %d " %digit_sum)