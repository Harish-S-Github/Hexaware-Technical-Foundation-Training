🚗 CarConnect – Car Rental System

A menu-driven, database-integrated car rental platform implemented in Python using object-oriented programming principles, custom exception handling and MS SQL Server for persistent storage.

---

📁 Project Structure

```
HexawareCasestudyCarConnect/
│
├── dao/                # Service classes for Admin, Customer, Vehicle, Reservation
├── entity/             # Entity/model classes (Admin, Customer, Vehicle, Reservation)
├── exception/          # Custom exception classes
├── main/               # Main menu-driven application
├── report/             # Report generation functionality
├── test/               # Unit test cases for all modules
├── util/               # Database connection utilities
│
├── README.md           # ← You are here
├── requirements.txt    # Python package dependencies
```

---

📍Database Schema (SQL Server)

Create the `car` database and these 4 tables:
1. Customer
2. Reservations
3. Vehicle
4. Admins
```

⚠️ Ensure your SQL Server uses `Trusted_Connection=Yes` and matches the settings in `util/db_conn_util.py`

---

💡 Key Features

- 🔐 Authentication for admin and customers
- 🚘 Vehicle Management (Add, View, Update, Remove, Availability)
- 🗓️ Reservation Handling with date-based conflict checks
- 📊 Reports- Reservation history, vehicle utilization, revenue
