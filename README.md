# 🏋️‍♂️ Fitness Booking API (Flask)

A simple **Flask REST API** to view and book fitness classes (Yoga, Zumba, HIIT) with timezone support and SQLite for storage.

---

## 🚀 Features

✅ View all upcoming fitness classes (`GET /classes`)  
✅ Book a spot in a class (`POST /book`)  
✅ View all bookings by email (`GET /bookings?email=<email>`)  
✅ Seed sample classes for testing  
✅ Timezone support (default IST, with `timezone` param)  
✅ SQLite used for lightweight local persistence

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your_repo_url>
cd assignment_flask
```

### 2️⃣ Install Dependencies
```bash
pip install Flask pytz
```

Or if you use `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3️⃣ Seed Sample Data
Run to populate the database with Yoga, Zumba, HIIT classes:
```bash
python seed_data.py
```

### 4️⃣ Run the Flask App
```bash
python app.py
```
Server will start on:
```
http://127.0.0.1:5000/
```

---

## 🧪 **Testing with Postman**

### ✅ **1. View All Classes**
**GET** `http://127.0.0.1:5000/classes`

**Optional:** To get datetimes in UTC timezone:
```
http://127.0.0.1:5000/classes?timezone=UTC
```

---

### ✅ **2. Book a Class**
**POST** `http://127.0.0.1:5000/book`

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
    "class_id": 1,
    "client_name": "Ankit Singh",
    "client_email": "ankit@example.com"
}
```

**Expected Response:**
```json
{
    "message": "Booking successful"
}
```

---

### ✅ **3. View All Bookings by Email**
**GET** `http://127.0.0.1:5000/bookings?email=ankit@example.com`

**Expected Response:**
```json
[
    {
        "booking_id": 1,
        "class_id": 1,
        "class_name": "Yoga",
        "class_datetime": "2025-07-08T10:00:00+05:30",
        "client_name": "Ankit Singh",
        "client_email": "ankit@example.com",
        "booked_at": "2025-07-07T09:15:00+05:30"
    }
]
```

---

## ⚙️ Project Structure

```
.
├── app.py                                     # Flask entry point
├── config/database.py                         # Database configuration
├── models/models.py                           # Models for DB
├── routes/fitness_booking_api_routes.py       # API routes
├── seed_data.py                               # Seeds sample classes
├── tests/test_booking.py                      # API tests
├── fitness_booking.db                         # SQLite DB (created after executing seed_data.py)
└── requirements.txt
```


---

## 🤝 Contact

**Ankit Singh**  
ankitsingh79834@gmail.com

---
