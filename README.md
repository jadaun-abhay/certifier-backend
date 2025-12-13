# Certifier Backend

A Django-based backend service for **certificate generation and management**.
The project supports **multiple users**, **authentication**, **certificate templates**, and **custom font selection** to dynamically generate certificates.

---

## ✨ Features

* User authentication & authorization
* Multi-user support
* Certificate template management
* Custom font selection for certificates
* Environment-based configuration
* Dockerized development & production setup

---

## 🏗️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Database**: (Configured via environment variables)
* **Containerization**: Docker & Docker Compose
* **Environment Management**: `.env` files

---

## 📂 Project Structure (Important Paths)

```
certifier-backend/
├── docker/
│   ├── development/
│   │   └── compose.yml
│   └── production/
│       └── compose.yml
├── .env.sample
├── manage.py
└── ...
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/certifier-backend.git
cd certifier-backend
```

---

### 2️⃣ Environment Variables Setup

This project uses environment variables for configuration.

1. Copy the sample environment file:

```bash
cp .env.sample .env
```

2. Open `.env` and update the values according to your setup:

```bash
nano .env
```

> ⚠️ **Important:** Never commit your `.env` file to version control.

---

## 🐳 Docker Setup

You can run the project using **Docker Compose** for both development and production.

---

### 🔧 Development Setup

Navigate to the development docker directory:

```bash
cd docker/development
```

Build and start the containers:

```bash
docker compose up -d --build
```

---

### 🏭 Production Setup

Navigate to the production docker directory:

```bash
cd docker/production
```

Build and start the containers:

```bash
docker compose up -d --build
```

---

## ▶️ Running the Django Server

If you're running the app without Docker or need to manually start the server:

```bash
python manage.py runserver 0.0.0.0:8000
```

The application will be available at:

```
http://localhost:8000
```

---

## 🧪 Common Commands

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Collect static files:

```bash
python manage.py collectstatic
```

---

## 🤝 Contributing

We welcome contributions! 🎉

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes

```bash
git commit -m "Add: your feature description"
```

4. Push to your branch

```bash
git push origin feature/your-feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

For issues, suggestions, or feature requests, please open an issue on GitHub.

---

⭐ If you find this project useful, consider giving it a star!
