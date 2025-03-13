# to25.py

# Accept user input and convert it to an integer
user_input = int(input("Enter a number: "))

# Check if the input number is greater than 25
if user_input > 25:
    print("Error")
else:
    # Loop from the input number to 25 (inclusive)
    for num in range(user_input, 26):
        print(num)
