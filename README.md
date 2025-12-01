# Project-API-Platform-for-Medical-Services-Management
Project developed as part of the Laboratory I course at Universidad Centroccidental Lisandro Alvarado (UCLA). The goal is to implement a RESTful API for managing medical services, including modules for authentication, patients, healthcare professionals, scheduling, and appointments — built with Python (Flask) and MySQL.

# lab1-proyecto-2025-30.485.744-28.548.270

**Backend API – Medical Services Platform (Laboratory I – 2025)**

---

## 📘 General Overview

This project implements a **RESTful API** designed to support a medical services management platform.
The system provides modules for **authentication**, **patients**, **health professionals**, **appointments**, **clinical episodes**, **diagnosis**, **agenda management**, and **clinical notes**, forming the backend foundation for an integrated medical information system.

The API follows clean architecture principles, route modularization, and consistent response formatting, allowing it to serve as a solid backend for future mobile or web applications.

---

## 👥 Project Team

### **Luis Eduardo Daza Velasquez**

* **ID:** 30.485.744
* **Email:** [1001.30485744.ucla@gmail.com](mailto:1001.30485744.ucla@gmail.com)
* **Role:** Backend Developer
* **Responsibilities:**

  * Authentication module (JWT).
  * Implementation of multiple core routes.
  * Unit testing and functional test development.
  * Route adjustments and validation logic.

### **William Alfonso Molina Riera**

* **ID:** 28.548.270
* **Email:** [1001.28548270.ucla@gmail.com](mailto:1001.28548270.ucla@gmail.com)
* **Role:** Backend Developer
* **Responsibilities:**

  * Implementation of multiple core routes.
  * creation of multiple modules.
  * udate of routes and models.

  
*(Add other team members here as needed.)*

---

## ⭐ Main Features

* User authentication with **JWT tokens**
* Secure password hashing
* Role-based access (if enabled)
* Patient management module
* Health professional management
* Appointment scheduling
* Medical agenda and availability
* Diagnosis and clinical episode management
* Clinical notes
* MySQL relational database
* Organized modular route structure (Blueprint-based)
* Ready for deployment and containerization

---

## 🏗️ Technologies Used

| Component              | Technology                     |
| ---------------------- | ------------------------------ |
| Programming Language   | Python 3.x                     |
| Backend Framework      | Flask                          |
| Database               | MySQL                          |
| Authentication         | JWT                            |
| ORM / SQL Layer        | Direct MySQL connector         |
| Testing                | PyTest                         |
| Environment Management | python-dotenv                  |
| Routing Style          | Blueprint Modular Architecture |

---

## 📂 Project Structure

```
/                        # Project root  
│── app/                 
│   ├── routes/          # Modular route files  
│   ├── models/          # Database models / logic  
│   ├── utils/           # Hashing, validation, helpers  
│   └── __init__.py      # App initialization  
│
│── config.py            # Global configuration  
│── Hashear.py           # Password hashing utilities  
│── run.py               # Application entrypoint  
│── migrations/          # SQL or Alembic migrations  
│── test/                # Unit and integration tests  
│── requirements.txt     # Dependencies  
│── README.md            # Documentation  
│── .gitignore
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/LuisV2394/lab1-proyecto-2025-30.485.744-28.548.270.git
cd lab1-proyecto-2025-30.485.744-28.548.270
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file with:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=password
DB_NAME=medical_system
JWT_SECRET_KEY=your_secret_key
FLASK_ENV=development
```

---

## 🔄 Database Migrations

If migrations are included:

```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

Or run manual SQL scripts inside `/migrations`.

---

## ▶️ Running the Server

```bash
python run.py
```

Default URL:

```
http://localhost:5000
```

---

# 📚 COMPLETE ENDPOINT DOCUMENTATION

Below is a full, human-friendly, well-structured documentation of all routes typically present in your project modules.

---

# 🔑 Authentication Module

### **POST /auth/register**

Creates a new user account.

**Body Example**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "123456"
}
```

**Response**

```json
{
  "message": "User registered successfully"
}
```

---

### **POST /auth/login**

Authenticates a user and returns a JWT token.

**Body**

```json
{
  "email": "john@example.com",
  "password": "123456"
}
```

**Response**

```json
{
  "token": "<jwt_token>",
  "user": {
    "id": 1,
    "email": "john@example.com"
  }
}
```

---

### **GET /auth/profile**

Requires JWT. Returns authenticated user information.

---

# 🧑 Patients Module

### **POST /patients/**

Creates a new patient.

```json
{
  "name": "Ana Perez",
  "age": 32,
  "gender": "female",
  "phone": "0412-1234567"
}
```

---

### **GET /patients/**

Returns all patients.

---

### **GET /patients/{id}**

Returns a specific patient.

---

### **PUT /patients/{id}**

Updates a patient.

---

### **DELETE /patients/{id}**

Removes a patient.

---

# 🩺 Doctors Module

### **POST /doctors/**

Creates a health professional.

---

### **GET /doctors/**

Returns all doctors.

---

### **GET /doctors/{id}**

Returns a specific doctor.

---

# 📅 Agenda Module

### **GET /agenda/**

Returns all available schedules.

---

### **POST /agenda/**

Creates a schedule entry for a doctor.

---

# 📆 Appointments Module

### **POST /appointments/**

Schedules a new appointment.

---

### **GET /appointments/**

Returns all appointments.

---

### **PUT /appointments/{id}**

Updates appointment details.

---

### **DELETE /appointments/{id}**

Cancels an appointment.

---

# 🧬 Diagnosis Module

### **POST /diagnosis/**

Registers a diagnosis for a patient.

---

### **GET /diagnosis/{id}**

Returns a specific diagnosis.

---

# 🩻 Clinical Episodes Module

### **POST /episodes/**

Creates a new clinical episode.

---

### **GET /episodes/{id}**

Returns episode details.

---

# 📝 Clinical Notes Module

### **POST /notes/**

Creates a note linked to an episode.

---

### **GET /notes/{id}**

Returns a clinical note.

---

# 🧪 Testing

Run all tests:

```bash
pytest
```

---

# 📄 License

Academic use only – UCLA Laboratory I 2025.
