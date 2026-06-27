def process_purchases():
    filename = input("Enter the file name: ")
    # Ensure it ends with .txt as per problem statement
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    items_purchased = 0
    free_items = 0
    amount_to_pay = 0
    discount_given = 0
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Some samples contain '(blank line)' string instead of an actual blank line
                if line.startswith('(blank line)'):
                    continue
                
                parts = line.split()
                if len(parts) >= 2:
                    name = " ".join(parts[:-1])
                    price_str = parts[-1]
                    
                    if name.lower() == 'discount':
                        try:
                            discount_given = int(price_str)
                        except ValueError:
                            print(f"Error parsing discount: {price_str}")
                    elif price_str.lower() == 'free':
                        free_items += 1
                    else:
                        try:
                            price = int(price_str)
                            amount_to_pay += price
                            items_purchased += 1
                        except ValueError:
                            print(f"Error parsing price for {name}: {price_str}")
                            
        print(f"No of items purchased: {items_purchased}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {amount_to_pay}")
        print(f"Discount given: {discount_given}")
        print(f"Final amount paid: {amount_to_pay - discount_given}")
        
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_purchases()