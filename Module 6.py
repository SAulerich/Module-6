import datetime

class ItemToPurchase:
    def __init__(self, name = "none", price = 0, quantity = 0, description = "none"):
        self.item_Name = name
        self.item_Price = price
        self.item_Quantity = quantity
        self.item_Description = description

class Cart:
    def __init__(self, customer_Name = "none"):
        self.customer_Name = customer_Name
        self.current_Date = datetime.datetime.now().strftime("%B %d, %Y")
        self.cart_Items = []
    def add_Item(self, item):
        self.cart_Items.append(item)
        print(f"{item.item_Name} has been added to your cart")
    def remove_Item(self, item_Name):
        for item in self.cart_Items:
            if item.item_Name == item_Name:
                self.cart_Items.remove(item)
                print(f"{item_Name} has been removed from your cart")
                return
        print("Item can not be found in your cart, so nothing has been removed")
    def modify_Item(self, item_Name, new_Quantity):
        for item in self.cart_Items:
            if item.item_Name == item_Name:
                item.item_Quantity = new_Quantity
                print(f"Update: {item_Name} now has {new_Quantity} in your cart")
                return
        print("This item was not found in your cart, so nothing has been modified")
    def get_Num_Items_In_Cart(self):
        return sum(item.item_Quantity for item in self.cart_Items)
    def get_Cost_Of_Cart(self):
        return sum(item.item_Price * item.item_Quantity for item in self.cart_Items)
    def print_Total(self):
        if not self.cart_Items:
            print("Your Shopping cart is now empty")
            return
        print(f"{self.customer_Name}'s Shopping Cart ({self.current_Date})")
        print("Number of Items:", self.get_Num_Items_In_Cart())
        for item in self.cart_Items:
            print(f"{item.item_Quantity} of the {item.item_Name} for ${item.item_Price} each = ${item.item_Quantity * item.item_Price}")
        print("Total: $", self.get_Cost_Of_Cart())
    def print_Descriptions(self):
        if not self.cart_Items:
            print("Your shopping cart is now empty")
            return
        print(f"{self.customer_Name}'s Shopping Cart ({self.current_Date})")
        print("Item Descriptions:")
        for item in self.cart_Items:
            print(f"{item.item_Name}: {item.item_Description}")

def print_Menu(shopping_Cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

def main():
    customer_Name = input("Enter your name: ")
    shopping_Cart = Cart(customer_Name)
    print_Menu(shopping_Cart)
    while True:
        choice = input("\nPlease, choose an option: ")
        if choice == "a":
            item_Name = input("Item name: ")
            item_Description = input("Item description: ")
            item_Price = float(input("Item price: "))
            item_Quantity = int(input("Item quantity: "))
            item = ItemToPurchase(item_Name, item_Price, item_Quantity, item_Description)
            shopping_Cart.add_Item(item)
        elif choice == "r":
            item_Name = input("Enter the name of the item to remove: ")
            shopping_Cart.remove_Item(item_Name)
        elif choice == "c":
            item_Name = input("Enter the name of the item to modify: ")
            new_Quantity = int(input("Enter the new quantity of the item to modify: "))
            shopping_Cart.modify_Item(item_Name, new_Quantity)
        elif choice == "i":
            shopping_Cart.print_Descriptions()
        elif choice == "o":
            shopping_Cart.print_Total()
        elif choice == "q":
            print("Program Completed")
            break
        else:
            print("Invalid choice. Please, choose another.")

if __name__ == "__main__":
    main()