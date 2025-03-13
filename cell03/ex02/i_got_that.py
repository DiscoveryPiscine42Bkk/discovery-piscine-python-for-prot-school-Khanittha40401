# i_got_that.py

# Start the while loop
while True:
    user_input = input("Enter something (or type 'STOP' to quit): ")

    # Check if the user wants to stop
    if user_input == "STOP":
        print("Stopping the program. Goodbye!")
        break
    else:
        print("Got it! You said:", user_input)
