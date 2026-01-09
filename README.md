# Healthcare API — Medical Services Platform (Laboratory I — 2025)

Professional, well-documented RESTful API for managing clinical workflows, built for the Laboratory I course at Universidad Centroccidental Lisandro Alvarado (UCLA).

This repository implements a modular backend for medical services using **Flask**, **SQLAlchemy**, **JWT-based authentication**, **Swagger documentation**, and **email notifications via SendGrid**.

---

## Table of Contents

* Overview
* Key Features
* Technology Stack
* Architecture & Project Layout
* Quickstart (Local)
* Environment Variables
* Database Migrations
* Running with Docker
* API Documentation (Swagger)
* Authentication
* Example Endpoints
* Authors & Roles
* Tests
* Useful Scripts
* Contributing
* Contact
* License

---

## Overview

The Healthcare API provides a complete backend platform for managing medical services. It includes **full support for clinical workflows, appointments, billing, notifications, email communications, and audit trails**, following a layered architecture (routes → controllers → services → repositories → models) for maintainability and testability.

---

## Key Features

* Complete CRUD for patients, professionals, care units, agendas, appointments, clinical episodes, notes, orders, prescriptions, results, insurances, plans, authorizations, services, tariffs, invoices, and payments.
* JWT authentication and role-based access control.
* **Email notifications** for appointment confirmations, reminders, and billing alerts (SendGrid integration).
* Swagger documentation per module (YAML) for interactive API exploration.
* SQLAlchemy models fully integrated with Flask-Migrate for DB migrations.
* Docker-compose support for local development with MySQL.
* Unit and functional tests ready-to-run.
* Audit logs and versioning for clinical notes and results.
* Scripts for seeding database and generating documentation.

---

## Technology Stack

* Python 3.10+
* Flask
* Flask-Migrate / Alembic
* SQLAlchemy
* PyJWT or Flask-JWT-Extended
* MySQL
* Flasgger (Swagger UI)
* SendGrid (email notifications)
* Docker / Docker-compose (optional)

---

## Architecture & Project Layout

```
app/
  __init__.py        # App factory
  swagger.py         # Flasgger loader
  config.py          # Configurations
  controllers/       # Endpoint logic
  docs/              # YAML Swagger docs
  models/            # ORM models
  repositories/      # DB access
  routes/            # Blueprints
  services/          # Business logic
  utils/             # Helpers
docker/              # Docker-compose files & init scripts
migrations/          # Alembic/Flask-Migrate
scripts/             # Seed/generate scripts
tests/               # Unit & functional tests
requirements.txt
run.py
README.md
```

---

## Quickstart (Local)

1. Clone the repository:

```bash
git clone https://github.com/LuisV2394/lab1-proyecto-2025-30.485.744-28.548.270.git
cd lab1-proyecto-2025-30.485.744-28.548.270
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables (`.env`):

### For Docker (`docker-compose`)

```env
FLASK_ENV=development
FLASK_APP=run.py
FLASK_DEBUG=1

# Database
DB_HOST=mysql
DB_PORT=3306
DB_NAME=healthcare_api
DB_USER=healthcare_user
DB_PASSWORD=healthcare_pass
DB_URL=mysql+pymysql://healthcare_user:healthcare_pass@mysql:3306/healthcare_api

# Security
JWT_SECRET_KEY=your_secret_key_here
SECRET_KEY=super_secret_key

# Email notifications (SendGrid)
SENDGRID_API_KEY=
SENDGRID_SENDER_EMAIL=1001.30485744.ucla@gmail.com
```

### For Local Development

```env
DB_URL=mysql+pymysql://root:@localhost:3307/healthcare_api
FLASK_ENV=development
FLASK_APP=manage.py
SECRET_KEY=super_secret_key
JWT_SECRET_KEY=your_jwt_secret_here
SENDGRID_API_KEY=
SENDGRID_SENDER_EMAIL=1001.30485744.ucla@gmail.com
```

---

## Database Migrations

```bash
flask db migrate -m "initial"
flask db upgrade
```

---

## Running with Docker (Enhanced)

Start the API and MySQL using Docker Compose:

```bash
docker-compose up --build
```

This will start:

* **Flask API** — backend server
* **MySQL** — database for the project
* **Optional: Adminer** — web interface for database management

### Useful Docker commands:

```bash
# Rebuild containers if dependencies or Dockerfile change
docker-compose up --build

# Run in detached mode
docker-compose up -d

# Stop containers
docker-compose down

# Remove containers and volumes (reset database)
docker-compose down -v

# View logs
docker-compose logs -f
```

### Database Initialization

The MySQL container automatically runs the script `docker/mysql/init.sql` to create tables and seed initial data. Ensure `DB_URL` matches the container host (`mysql`) when running via Docker.

---

## API Documentation (Swagger)

Open interactive documentation at:

```
http://localhost:5000/apidocs/
```

YAML files are organized per module under `app/docs/`.

---

## Authentication

JWT Bearer tokens:

* `POST /auth/login` — login and receive token
* `Authorization: Bearer <token>` — required for protected routes

---

## Example Endpoints

### Create a Person

**Endpoint:** `POST /people`

**Request Body:**

```json
{
  "document_number": "V12345678",
  "first_name": "Luis",
  "last_name": "Daza",
  "gender": "M",
  "birth_date": "1990-05-20",
  "email": "luis.daza@example.com",
  "phone": "+584123456789",
  "address": "Calle Falsa 123, Caracas, Venezuela",
  "emergency_contact": "+584123987654",
  "active": 1
}
```

**Response 201 (Success):**

```json
{
  "id": 1,
  "document_number": "V12345678",
  "first_name": "Luis",
  "last_name": "Daza",
  "gender": "M",
  "birth_date": "1990-05-20",
  "email": "luis.daza@example.com",
  "phone": "+584123456789",
  "address": "Calle Falsa 123, Caracas, Venezuela",
  "emergency_contact": "+584123987654",
  "active": 1
}
```

**Response 400 (Invalid input)**
**Response 500 (Server error)**

---

## Authors & Roles

### **Luis Eduardo Daza Velasquez**

* **ID:** 30.485.744
* **Email:** [1001.30485744.ucla@gmail.com](mailto:1001.30485744.ucla@gmail.com)
* **Role:** Backend Developer & QA
* **Responsibilities:**

  * Authentication module (JWT)
  * Core routes implementation
  * Unit & functional testing
  * Bug fixing and code corrections
  * Route adjustments and validations
  * **SendGrid email notifications integration and testing**

### **William Alfonso Molina Riera**

* **ID:** 28.548.270
* **Email:** [1001.28548270.ucla@gmail.com](mailto:1001.28548270.ucla@gmail.com)
* **Role:** Backend Developer
* **Responsibilities:**

  * Core routes and modules implementation
  * Database models & migrations
  * Adjustments on routes and business logic
  * Feature development and validation

---

## Tests

Run tests with:

```bash
pytest
```

---

## Useful Scripts

* `scripts/seed_data.py` — Seed database with initial data
* `scripts/generate_docs.py` — Generate/validate Swagger documentation

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new behavior
4. Keep changes small and scoped
5. Submit pull request with clear description

---

## Contact

* Luis Eduardo Daza Velasquez — [1001.30485744.ucla@gmail.com](mailto:1001.30485744.ucla@gmail.com)
* William Alfonso Molina Riera — [1001.28548270.ucla@gmail.com](mailto:1001.28548270.ucla@gmail.com)

---

## License

Academic use only — UCLA Laboratory I 2025

---