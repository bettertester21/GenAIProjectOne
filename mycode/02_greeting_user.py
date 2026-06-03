# Simple greeting program

def main():
    # Ask the user to enter their name
    name = input("Please enter your name: ").strip()
    
    # Check if the user actually entered a name
    if not name:
        print("You didn't enter a name. Please try again.")
        return
    
    # Capitalize the first letter for a cleaner look
    formatted_name = name.capitalize()
    
    # Print the greeting message
    print(f"Hello, {formatted_name}! Welcome to the Python + LLM")

if __name__ == "__main__":
    main()