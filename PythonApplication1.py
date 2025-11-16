# This program calculates the total cost for multiple line items
# using validated input for price (float) and quantity (integer).

# --- Global Constants for Formatting ---
WIDTH = 50
SEPARATOR = "=" * WIDTH

# --- Part 1: Display Heading ---

def display_heading():
    """
    Displays the program heading.
    """
    print(SEPARATOR)
    print("        LINE ITEM CALCULATOR")
    print(SEPARATOR)

# --- Part 2: Input Functions with Validation ---

def get_valid_price():
    """
    Prompts the user to enter a price and validates that the input is a float.
    Displays an error message on invalid input and prompts again, otherwise returns the price.
    """
    while True:
        try:
            # Price must be a float
            price_input = input("Enter price: ").strip()
            price = float(price_input)
            if price < 0:
                 print("ERROR: Price cannot be negative. Please try again.")
                 continue
            return price
        except ValueError:
            # If a value is entered in an invalid format a message will display
            print("ERROR: Invalid format. Price must be a number (float). Please try again.")

def get_valid_quantity():
    """
    Prompts the user to enter a quantity and validates that the input is an integer.
    Displays an error message on invalid input and prompts again, otherwise returns the quantity.
    """
    while True:
        try:
            # Quantity must be an integer
            quantity_input = input("Enter quantity: ").strip()
            quantity = int(quantity_input)
            if quantity < 1:
                print("ERROR: Quantity must be a positive whole number. Please try again.")
                continue
            return quantity
        except ValueError:
            # If a value is entered in an invalid format a message will display
            print("ERROR: Invalid format. Quantity must be a whole number (integer). Please try again.")

# --- Main Program Logic ---

def main():
    """
    Runs the main program loop, handling input, calculation, and user continuation prompt.
    """
    # Part 1: Display the heading
    display_heading()
    
    # Part 2: Write a while loop
    continue_program = 'y'
    
    while continue_program.lower() == 'y':
        
        # Call function to get valid price
        price = get_valid_price()
        
        # Call function to get valid quantity
        quantity = get_valid_quantity()
        
        # Compute the total by multiplying quantity times price
        total = quantity * price
        
        # Display the totals in the format shown in the sample screenshot.
        print(SEPARATOR)
        print(f"{'Price:':<15} ${price:,.2f}")
        print(f"{'Quantity:':<15} {quantity}")
        print(f"{'TOTAL:':<15} ${total:,.2f}")
        print(SEPARATOR)
        
        # Prompt the user to enter another line item.
        # If the user enters a 'y' continue, if the user enters an 'n' end the program
        while True:
            prompt = input("Enter another line item? (y/n): ").strip().lower()
            if prompt in ['y', 'n']:
                continue_program = prompt
                break
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    print("\nProgram ended. Goodbye!")

if __name__ == "__main__":
    main()