class Customer:
    def __init__(self, name: str):
        self.name = name

class Table:
    def __init__(self, id: int, capacity: int):
        self.id = id
        self.capacity = capacity

class Reservation:
    def __init__(self, customer: Customer, table: Table, start_time_slot: int, 
                 end_time_slot: int):
        self.customer = customer
        self.table = table
        self.start_time_slot = start_time_slot
        self.end_time_slot = end_time_slot

class Restaurant:
    def __init__(self):
        self.tables = []  #List of tables in the restaurant
        self.reservations = []  #List of reservations

    def add_table(self, table: Table):
        self.tables.append(table)

    def is_table_available(self, table: Table, start_time_slot: int, 
                           end_time_slot: int):
        #Check if the table is available for the given time slot
        for reservation in self.reservations:
            if reservation.table.id == table.id and (
                (start_time_slot >= reservation.start_time_slot 
                 and start_time_slot < reservation.end_time_slot) or
                (end_time_slot > reservation.start_time_slot 
                 and end_time_slot <= reservation.end_time_slot) or
                (start_time_slot <= reservation.start_time_slot 
                 and end_time_slot >= reservation.end_time_slot)
            ):
                return False
        return True

    def find_available_tables(self, capacity: int, start_time_slot: int, 
                              end_time_slot: int) :
        #Find tables that are available and have the required capacity
        available_tables = [
            table for table in self.tables
            if table.capacity >= capacity 
            and self.is_table_available(table, start_time_slot, end_time_slot)
        ]
        #Sort available tables by capacity
        available_tables.sort(key=lambda table: table.capacity)
        return available_tables

    def add_reservation(self, name: str, capacity: int, start_slot: int, 
                        end_slot: int):
        #Try to find available tables for the given capacity and time slot
        available_tables = self.find_available_tables(capacity, start_slot, end_slot)
        if available_tables:
            #If available, add a new reservation
            self.reservations.append(Reservation(
                Customer(name), available_tables[0], start_slot, end_slot))
            print("Reservation successfully added.")
        else:
            print("No available tables for the requested time slot.")

    def print_reservations(self):
        print("All reservations:")
        for reservation in self.reservations:
            print(f"Customer: {reservation.customer.name}, "
                f"Table Capacity: {reservation.table.capacity}, "
                f"Start Time Slot: {reservation.start_time_slot}, "
                f"End Time Slot: {reservation.end_time_slot}")

def main():
    restaurant = Restaurant()

    #Add tables to the restaurant
    restaurant.add_table(Table(1, 6))
    restaurant.add_table(Table(2, 4))
    restaurant.add_table(Table(3, 2))

    #Try to add reservations
    restaurant.add_reservation("Customer 1", 4, 1, 3)
    restaurant.add_reservation("Customer 2", 6, 2, 4)
    restaurant.add_reservation("Customer 3", 4, 3, 5)
    restaurant.add_reservation("Customer 4", 4, 1, 3)

    #Print all reservations
    restaurant.print_reservations()

if __name__ == "__main__":
    main()
