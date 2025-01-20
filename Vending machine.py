print("""
 █████   █████ ██████████ ██████   █████ ██████████   █████ ██████   █████   █████████      
░░███   ░░███ ░░███░░░░░█░░██████ ░░███ ░░███░░░░███ ░░███ ░░██████ ░░███   ███░░░░░███     
 ░███    ░███  ░███  █ ░  ░███░███ ░███  ░███   ░░███ ░███  ░███░███ ░███  ███     ░░░      
 ░███    ░███  ░██████    ░███░░███░███  ░███    ░███ ░███  ░███░░███░███ ░███              
 ░░███   ███   ░███░░█    ░███ ░░██████  ░███    ░███ ░███  ░███ ░░██████ ░███    █████     
  ░░░█████░    ░███ ░   █ ░███  ░░█████  ░███    ███  ░███  ░███  ░░█████ ░░███  ░░███      
    ░░███      ██████████ █████  ░░█████ ██████████   █████ █████  ░░█████ ░░█████████      
     ░░░      ░░░░░░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░       
                                                                                            
                                                                                            
                                                                                            
 ██████   ██████   █████████     █████████  █████   █████ █████ ██████   █████ ██████████   
░░██████ ██████   ███░░░░░███   ███░░░░░███░░███   ░░███ ░░███ ░░██████ ░░███ ░░███░░░░░█   
 ░███░█████░███  ░███    ░███  ███     ░░░  ░███    ░███  ░███  ░███░███ ░███  ░███  █ ░    
 ░███░░███ ░███  ░███████████ ░███          ░███████████  ░███  ░███░░███░███  ░██████      
 ░███ ░░░  ░███  ░███░░░░░███ ░███          ░███░░░░░███  ░███  ░███ ░░██████  ░███░░█      
 ░███      ░███  ░███    ░███ ░░███     ███ ░███    ░███  ░███  ░███  ░░█████  ░███ ░   █   
 █████     █████ █████   █████ ░░█████████  █████   █████ █████ █████  ░░█████ ██████████   
░░░░░     ░░░░░ ░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░    
                                                                                            
                                                                                            
                                                                                            
""")
class VendingMachine:
    def __init__(self):
        self.items = {
            'cola': 3.00,
            'chips': 2.00,'candy': 4.75,'water': 1.50,'sandwich': 6.00,'juice': 2.50,'cookie': 3.25,'gum': 1.00,'mints': 0.75,'fruit custard': 2.25}
        self.balance = 0.0

    def display_items(self):
        print("Available Items:")
        for item, price in self.items.items():
            print(f"{item.capitalize()}: ${price:.2f}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def select_item(self, item):
        item = item.lower()
        if item in self.items:
            price = self.items[item]  
            if self.balance >= price:
                self.balance -= price
                print(f"Dispensing {item.capitalize()}.")
                print(f"Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance. Please insert more money.")
        else:
            print("Invalid item. Please choose a valid item.")

# Example Usage
if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        print("\n1. Display Items")
        print("2. Insert Money")
        print("3. Select Item")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            amount = float(input("Enter the amount to insert: $"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            item = input("Enter the item you want to purchase: ")
            vending_machine.select_item(item)
        elif choice == '4':
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
