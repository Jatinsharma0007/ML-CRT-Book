class Product:
    
    discount_rate = 0.10  # 10% default discount
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def calculate_discounted_price(self):
        return self.price * (1 - self.discount_rate)
    
    def display_product_info(self):
        print(f"Product: {self.name}")
        print(f"Original Price: ${self.price:.2f}")
        print(f"Discounted Price: ${self.calculate_discounted_price():.2f}")
        print(f"Discount Rate: {self.discount_rate * 100}%")

def main():
    laptop = Product("Gaming Laptop", 70000)
    smartphone = Product("Smartphone", 30000)
    
    print("Product 1:")
    laptop.display_product_info()
    
    print("\nProduct 2:")
    smartphone.display_product_info()
    
    print("\nChanging Discount Rate:")
    Product.discount_rate = 0.20  # 20% discount
    
    print("Updated Product Prices:")
    print("Product 1:")
    laptop.display_product_info()
    
    print("\nProduct 2:")
    smartphone.display_product_info()

if __name__ == "__main__":
    main()