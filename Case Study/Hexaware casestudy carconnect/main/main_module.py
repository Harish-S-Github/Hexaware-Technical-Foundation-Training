from dao.adminservice import AdminService
from dao.customerservice import CustomerService
from dao.vehicleservice import VehicleService
from dao.reservationservice import ReservationService
from report.reportgenerator import ReportGenerator

from entity.admin import Admin
from entity.customer import Customer
from entity.vehicle import Vehicle
from entity.reservation import Reservation

from exception.authentication_exception import AuthenticationException
from exception.reservation_exception import ReservationException
from exception.vehicle_not_found_exception import VehicleNotFoundException


def admin_menu():
    admin_service = AdminService()
    while True:
        print("\n--- Admin Menu ---")
        print("1. Register Admin")
        print("2. Get Admin by Username")
        print("3. Get Admin by ID")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            admin = Admin(
                admin_id=int(input("Admin ID: ")),
                first_name=input("First Name: "),
                last_name=input("Last Name: "),
                email=input("Email: "),
                phone_number=input("Phone Number: "),
                username=input("Username: "),
                password=input("Password: "),
                role=input("Role: "),
                join_date=input("Join Date (YYYY-MM-DD): ")
            )
            admin_service.register_admin(admin)
            print("Admin registered successfully.")

        elif choice == "2":
            username = input("Enter Username: ")
            try:
                admin = admin_service.get_admin_by_username(username)
                print("Admin found:", admin.get_first_name(), admin.get_email())
            except AuthenticationException as e:
                print("Error:", e)

        elif choice == "3":
            admin_id = int(input("Enter Admin ID: "))
            admin = admin_service.get_admin_by_id(admin_id)
            if admin:
                print("Admin found:", admin.get_first_name(), admin.get_email())
            else:
                print("Admin not found.")

        elif choice == "4":
            break


def customer_menu():
    customer_service = CustomerService()
    while True:
        print("\n--- Customer Menu ---")
        print("1. Register Customer")
        print("2. Get Customer by Username")
        print("3. Get Customer by ID")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            customer = Customer(
                customer_id=int(input("Customer ID: ")),
                first_name=input("First Name: "),
                last_name=input("Last Name: "),
                email=input("Email: "),
                phone_number=input("Phone Number: "),
                address=input("Address: "),
                username=input("Username: "),
                password=input("Password: "),
                registration_date=input("Registration Date (YYYY-MM-DD): ")
            )
            customer_service.register_customer(customer)
            print("Customer registered successfully.")

        elif choice == "2":
            username = input("Enter Username: ")
            try:
                customer = customer_service.get_customer_by_username(username)
                print("Customer found:", customer.get_first_name(), customer.get_email())
            except AuthenticationException as e:
                print("Error:", e)

        elif choice == "3":
            customer_id = int(input("Enter Customer ID: "))
            customer = customer_service.get_customer_by_id(customer_id)
            if customer:
                print("Customer found:", customer.get_first_name(), customer.get_email())
            else:
                print("Customer not found.")

        elif choice == "4":
            break


def vehicle_menu():
    vehicle_service = VehicleService()
    while True:
        print("\n--- Vehicle Menu ---")
        print("1. Add Vehicle")
        print("2. Get Vehicle by ID")
        print("3. Get Available Vehicles")
        print("4. Update Vehicle")
        print("5. Remove Vehicle")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            vehicle = Vehicle(
                vehicle_id=int(input("Vehicle ID: ")),
                model=input("Model: "),
                make=input("Make: "),
                year=int(input("Year: ")),
                color=input("Color: "),
                registration_number=input("Registration Number: "),
                availability=bool(int(input("Available (1-Yes, 0-No): "))),
                daily_rate=float(input("Daily Rate: "))
            )
            vehicle_service.add_vehicle(vehicle)
            print("Vehicle added successfully.")

        elif choice == "2":
            try:
                vehicle_id = int(input("Enter Vehicle ID: "))
                vehicle = vehicle_service.get_vehicle_by_id(vehicle_id)
                print("Vehicle found:", vehicle.get_model(), vehicle.get_registration_number())
            except VehicleNotFoundException as e:
                print("Error:", e)

        elif choice == "3":
            available = vehicle_service.get_available_vehicles()
            for v in available:
                print(v.get_vehicle_id(), v.get_model(), v.get_daily_rate())

        elif choice == "4":
            vehicle_id = int(input("Enter Vehicle ID to update: "))
            vehicle = Vehicle(
                vehicle_id=vehicle_id,
                model=input("Model: "),
                make=input("Make: "),
                year=int(input("Year: ")),
                color=input("Color: "),
                registration_number=input("Registration Number: "),
                availability=bool(int(input("Available (1-Yes, 0-No): "))),
                daily_rate=float(input("Daily Rate: "))
            )
            vehicle_service.update_vehicle(vehicle)
            print("Vehicle updated successfully.")

        elif choice == "5":
            vehicle_id = int(input("Enter Vehicle ID to remove: "))
            vehicle_service.remove_vehicle(vehicle_id)
            print("Vehicle removed successfully.")

        elif choice == "6":
            break


def reservation_menu():
    reservation_service = ReservationService()
    while True:
        print("\n--- Reservation Menu ---")
        print("1. Create Reservation")
        print("2. Get Reservation by ID")
        print("3. Get Reservations by Customer ID")
        print("4. Update Reservation")
        print("5. Cancel Reservation")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            reservation = Reservation(
                reservation_id=int(input("Reservation ID: ")),
                customer_id=int(input("Customer ID: ")),
                vehicle_id=int(input("Vehicle ID: ")),
                start_date=input("Start Date (YYYY-MM-DD): "),
                end_date=input("End Date (YYYY-MM-DD): "),
                total_cost=0.0,
                status="pending"
            )
            daily_rate = float(input("Enter Daily Rate: "))
            reservation.calculate_total_cost(daily_rate)
            reservation_service.create_reservation(reservation)
            print("Reservation created with total cost:", reservation.get_total_cost())

        elif choice == "2":
            try:
                reservation_id = int(input("Enter Reservation ID: "))
                r = reservation_service.get_reservation_by_id(reservation_id)
                print("Reservation:", r.get_customer_id(), r.get_status())
            except ReservationException as e:
                print("Error:", e)

        elif choice == "3":
            customer_id = int(input("Enter Customer ID: "))
            reservations = reservation_service.get_reservations_by_customer_id(customer_id)
            for r in reservations:
                print(r.get_reservation_id(), r.get_status(), r.get_total_cost())

        elif choice == "4":
            reservation_id = int(input("Reservation ID to update: "))
            new_status = input("New Status: ")
            new_end_date = input("New End Date (YYYY-MM-DD): ")
            daily_rate = float(input("New Daily Rate: "))

            r = reservation_service.get_reservation_by_id(reservation_id)
            r.set_status(new_status)
            r.set_end_date(new_end_date)
            r.calculate_total_cost(daily_rate)
            reservation_service.update_reservation(r)
            print("Reservation updated.")

        elif choice == "5":
            reservation_id = int(input("Enter Reservation ID to cancel: "))
            reservation_service.cancel_reservation(reservation_id)
            print("Reservation canceled.")

        elif choice == "6":
            break


def report_menu():
    while True:
        print("\n--- Report Menu ---")
        print("1. Reservation History")
        print("2. Vehicle Utilization")
        print("3. Revenue Report")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            ReportGenerator.generate_reservation_history()
        elif choice == "2":
            ReportGenerator.generate_vehicle_utilization()
        elif choice == "3":
            ReportGenerator.generate_revenue_report()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n=== CarConnect Main Menu ===")
        print("1. Admin Operations")
        print("2. Customer Operations")
        print("3. Vehicle Operations")
        print("4. Reservation Operations")
        print("5. Report Generation")  # ✅ Report menu added
        print("6. Exit")
        choice = input("Select option: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            vehicle_menu()
        elif choice == "4":
            reservation_menu()
        elif choice == "5":
            report_menu()
        elif choice == "6":
            print("Exiting CarConnect. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
