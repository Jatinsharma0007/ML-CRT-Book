class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate
        self.is_available = True
    
    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_vehicle(self):
        self.is_available = True
        return True
    
    def get_details(self):
        status = "Available" if self.is_available else "Rented"
        return (
            f"Vehicle ID: {self.vehicle_id}\n"
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Daily Rate: ${self.rental_rate:.2f}\n"
            f"Status: {status}"
        )

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_rate, num_doors, fuel_type):
        super().__init__(vehicle_id, brand, model, rental_rate)
        
        self.num_doors = num_doors
        self.fuel_type = fuel_type
    
    def get_details(self):
        base_details = super().get_details()
        return (
            f"{base_details}\n"
            f"Doors: {self.num_doors}\n"
            f"Fuel Type: {self.fuel_type}"
        )

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_rate, bike_type, frame_size):
        super().__init__(vehicle_id, brand, model, rental_rate)
        
        self.bike_type = bike_type
        self.frame_size = frame_size
    
    def get_details(self):
        base_details = super().get_details()
        return (
            f"{base_details}\n"
            f"Bike Type: {self.bike_type}\n"
            f"Frame Size: {self.frame_size}"
        )

class RentalSystem:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None
    
    def list_available_vehicles(self):
        return [vehicle for vehicle in self.vehicles if vehicle.is_available]

def main():
    rental_system = RentalSystem()
    
    car1 = Car("C001", "Toyota", "Camry", 50.00, 4, "Gasoline")
    car2 = Car("C002", "Tesla", "Model 3", 75.00, 4, "Electric")
    bike1 = Bike("B001", "Giant", "Defy", 25.00, "Road", "Medium")
    bike2 = Bike("B002", "Trek", "Mountain", 30.00, "Mountain", "Large")
    
    rental_system.add_vehicle(car1)
    rental_system.add_vehicle(car2)
    rental_system.add_vehicle(bike1)
    rental_system.add_vehicle(bike2)
    
    print("Initial Vehicle Details:")
    for vehicle in rental_system.vehicles:
        print("\n" + vehicle.get_details())
    
    print("\nRenting a vehicle:")
    car_to_rent = rental_system.find_vehicle("C001")
    if car_to_rent:
        if car_to_rent.rent():
            print(f"Rented: {car_to_rent.brand} {car_to_rent.model}")
    
    print("\nAvailable Vehicles:")
    for vehicle in rental_system.list_available_vehicles():
        print(vehicle.get_details())

if __name__ == "__main__":
    main()
