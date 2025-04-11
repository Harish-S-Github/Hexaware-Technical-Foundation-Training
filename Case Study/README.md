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
- ⚠️ Custom Exceptions- Authentication, Reservation, Not Found, Input Errors
- 🪪 Unit Testing for all services using `unittest`

---

 ▶️ Running the Application

```bash
From project root directory
python -m main.main_module
```

You’ll get a menu like:

```
=== CarConnect Main Menu ===
1. Admin Operations
2. Customer Operations
3. Vehicle Operations
4. Reservation Operations
5. Report Generation
6. Exit
```

---

🪪 Running Tests

```bash
Run all tests
python -m unittest discover test

Or run a specific test
python -m unittest test.test_admin
python -m unittest test.test_customer
```

 All services support `test_mode=True` for mock testing without touching the database.

---

✅ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Minimal `requirements.txt`:

```
pyodbc
```

---
