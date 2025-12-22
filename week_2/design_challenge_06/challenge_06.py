'''
Design Challenge 6: Marine Company 
A marine company has many ships with them. Ship are either cruise type, or cargo type. Some 
register to a particular ship to travel from one place to another or to send the cargo from one place 
to another. Design the OO model for the above problem statement and implement the  
code to 
• Total amount been collected. 
• List the total amount for every ship 
• List all the customer details for a particular cruise ship
'''

from abc import ABC, abstractmethod


class Ship(ABC):
    def __init__(self, ship_id, name):
        self.ship_id = ship_id
        self.name = name
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def get_total_amount(self):
        return sum(booking.amount for booking in self.bookings)


class CruiseShip(Ship):
    def __init__(self, ship_id, name, route):
        super().__init__(ship_id, name)
        self.route = route

class CargoShip(Ship):
    def __init__(self, ship_id, name, max_capacity):
        super().__init__(ship_id, name)
        self.max_capacity = max_capacity


class Customer:
    def __init__(self, customer_id, name, contact):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"{self.customer_id} - {self.name} ({self.contact})"

class Booking:
    def __init__(self, booking_id, customer, ship, amount):
        self.booking_id = booking_id
        self.customer = customer
        self.ship = ship
        self.amount = amount

        ship.add_booking(self)

class MarineCompany:
    def __init__(self):
        self.ships = []
        self.bookings = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def add_booking(self, booking):
        self.bookings.append(booking)

    # 1. Total amount collected
    def get_total_amount_collected(self):
        return sum(booking.amount for booking in self.bookings)

    # 2. Total amount for every ship
    def get_total_amount_per_ship(self):
        totals = {}
        for ship in self.ships:
            totals[ship.name] = ship.get_total_amount()
        return totals

    # 3. List all customer details for a particular cruise ship
    def get_customers_for_cruise_ship(self, ship_id):
        customers = []
        for ship in self.ships:
            if ship.ship_id == ship_id and isinstance(ship, CruiseShip):
                for booking in ship.bookings:
                    customers.append(booking.customer)
        return customers


if __name__ == "__main__":
    company = MarineCompany()

    # Ships
    cruise_ship = CruiseShip(1, "Ocean Queen", "Mumbai → Goa")
    cargo_ship = CargoShip(2, "Cargo Titan", 15000)

    company.add_ship(cruise_ship)
    company.add_ship(cargo_ship)

    # Customers
    c1 = Customer(101, "Ravi", "9876543210")
    c2 = Customer(102, "Anita", "9123456789")
    c3 = Customer(103, "Logistics Ltd", "cargo@log.com")

    # Bookings
    b1 = Booking(1, c1, cruise_ship, 5000)
    b2 = Booking(2, c2, cruise_ship, 6000)
    b3 = Booking(3, c3, cargo_ship, 20000)

    company.add_booking(b1)
    company.add_booking(b2)
    company.add_booking(b3)

    # Outputs
    print("Total Amount Collected:", company.get_total_amount_collected())

    print("\nTotal Amount per Ship:")
    for ship, amount in company.get_total_amount_per_ship().items():
        print(f"{ship}: {amount}")

    print("\nCustomers for Cruise Ship 'Ocean Queen':")
    for customer in company.get_customers_for_cruise_ship(1):
        print(customer)
