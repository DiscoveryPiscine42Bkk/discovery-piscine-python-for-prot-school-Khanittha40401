
def print_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Display multiplication tables from 1 to 10
def display_tables():
    for number in range(1, 11):
        print_table(number)

# Start the program
if __name__ == "__main__":
    display_tables()
