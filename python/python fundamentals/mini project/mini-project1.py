def suggest_transport():
    try:
        distance = float(input("How far would you like to travel in miles? "))
        
        if distance < 3:
            print("I suggest Bicycle to your destination")
        elif distance < 300:
            print("I suggest Motor-Cycle to your destination")
        else:
            print("I suggest Super-Car to your destination")
            
    except ValueError:
        print("Invalid input. Please enter a valid number for distance.")

if __name__ == "__main__":
    suggest_transport()