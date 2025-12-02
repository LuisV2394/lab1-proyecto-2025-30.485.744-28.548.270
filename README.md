# lab1-proyecto-2025-30.485.744-28.548.270
Project developed as part of the Laboratory I course at Universidad Centroccidental Lisandro Alvarado (UCLA). The goal is to implement a RESTful API for managing medical services, including modules for authentication, patients, healthcare professionals, scheduling, and appointments — built with Python (Flask) and MySQL.

**Backend API – Medical Services Platform (Laboratory I – 2025)**

# 🏥 **Healthcare API – Medical Backend in Flask**

A modular medical API built with **Flask**, **SQLAlchemy**, **JWT**, and **Swagger**, following a clean layered architecture (routes → services → repositories → models), with full YAML-based documentation.

Designed to manage:

* Authentication (JWT)
* Users & profiles
* People registry
* Healthcare professionals
* Medical units
* Clinical episodes
* Agenda & appointments
* Consent records

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

---

## 📌 **Key Features**

* 🔐 Secure authentication using **JWT**
* 🧩 Clean modular architecture
* 📚 Swagger documentation using **YAML** files
* 🗂 Database migrations with **Flask-Migrate**
* 🏗 MySQL as the primary database
* 🧪 Ready-to-use testing structure
* 📦 Production-ready project organization

---

# 🚀 **Installation & Setup**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-user/healthcare_api.git
cd healthcare_api
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables (`.env`)

```
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=mysql+pymysql://user:password@localhost/healthcare
SWAGGER_TITLE=Healthcare API
```

### 5️⃣ Run database migrations

```bash
flask db upgrade
```

### 6️⃣ Start the server

```bash
python run.py
```

### ✔ If everything loads correctly:

```
Medical API running
```

---

Default URL:

```
http://127.0.0.1:5000 o http://192.168.0.111:5000

```

---

# 📘 **Swagger API Documentation**

This API uses **Flasgger**, with Swagger definitions stored in modular `.yml` files.

Open the docs at:

👉 **[http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)**

All documentation files are stored in:

```
app/docs/
```

Organized by module:

```
docs/auth/
docs/users/
docs/professionals/
docs/people/
docs/units/
docs/episodes/
docs/agenda/
docs/consent/
docs/common/
```

The main Swagger loader is:

```
app/swagger.py
```

---

# 📂 **Project Structure**

Complete and accurate structure based on your real project:

```
healthcare_api/
│
├── app/
│   ├── __init__.py
│   ├── swagger.py
│   ├── config.py
│   │
│   ├── docs/
│   │   ├── auth/
│   │   ├── users/
│   │   ├── professionals/
│   │   ├── people/
│   │   ├── units/
│   │   ├── episodes/
│   │   ├── agenda/
│   │   ├── consent/
│   │   └── common/
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── professionals.py
│   │   ├── people.py
│   │   ├── units.py
│   │   ├── episodes.py
│   │   ├── agenda.py
│   │   └── consent.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── person.py
│   │   ├── professional.py
│   │   ├── unit.py
│   │   ├── episode.py
│   │   ├── appointment.py
│   │   ├── agenda_block.py
│   │   └── consent.py
│   │
│   ├── repositories/
│   ├── services/
│   ├── middlewares/
│   ├── utils/
│   └── database/
│
├── migrations/
├── scripts/
├── tests/
├── requirements.txt
├── run.py
└── README.md
```

---

# 🔑 **Authentication**

The API uses JWT with **Bearer tokens**.

### Login

```
POST /auth/login
```

### Register

```
POST /auth/register
```

### Protected endpoints require:

```
Authorization: Bearer <token>
```

---

# 🧩 **Available Modules**

## 🔐 Authentication

* Register new user
* Login
* Token handling

## 👤 Users

* Get authenticated profile
* Update user

## 🧍 People

* Create a person
* Update person
* Link person to users or professionals

## 🧑‍⚕️ Professionals

* Create/update professionals
* List all
* Association with medical units

## 🏢 Units

* Full CRUD

## 📅 Agenda & Appointments

* Create agenda blocks
* Create medical appointments
* Update appointment status
* Validate status transitions
* Appointment history tracking

## 🗂 Consent

* Register patient consent
* Audit logs

## 🧾 Clinical Episodes

* Create episodes
* Link to patients/people

---

# 🧪 **Testing**

Tests are stored in:

```
tests/
```

Run them with:

```bash
pytest
```

---

# 🛠 **Useful Scripts**

```
scripts/seed_data.py        # Initial database data
scripts/generate_docs.py    # Build static swagger documentation
```

---

# 📦 **Database Migrations**

Create a migration:

```bash
flask db migrate -m "message"
```

Apply migrations:

```bash
flask db upgrade
```

---

# 📄 License

Academic use only – UCLA Laboratory I 2025.