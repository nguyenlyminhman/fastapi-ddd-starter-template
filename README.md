# FastAPI DDD Starter Template 🚀

A starter template for building backend APIs with **FastAPI** using **Domain‑Driven Design (DDD)** principles.  
This template gives you a clean and scalable project structure to begin your next Python backend service without reinventing the wheel.

---

## 🌟 Features

- 🧠 **Domain-Driven Design (DDD)** architecture  
  Clean separation of Domain, Application, and Infrastructure layers with clear responsibilities.
- ⚡ Built with **FastAPI** — high performance, async‑ready web framework.
- 🐍 Pythonic code using **Pydantic** for validation and schemas.
- 🐋 Includes **Dockerfile** + local dev script (`dev.sh`).
- 📦 Modular structure — easy to grow for larger applications.
- 🛠 Ready for integration with databases, caching, messaging, testing, etc.

---

## 📁 Project Structure

```
fastapi-ddd-starter-template/
├── src/
│   ├── domain/            # Entities, value objects, domain logic
│   ├── application/       # Use cases, services, business rules
│   ├── infrastructure/    # DB, external services, adapters
│   ├── presentation/      # FastAPI routes, HTTP interfaces
│   └── config/            # Settings and environment config
├── Dockerfile
├── Dockerfile.local
├── dev.sh                 # Dev setup script
├── requirements.txt
├── README.md
└── tests/                 # (optional) unit/integration tests
```

> This layout enforces *one‑way dependency* — inner layers (Domain) don’t depend on outer ones (Infrastructure/Presentation). This is a core DDD & clean architecture principle.

---

## 🛠 Getting Started

### Prerequisites

- Python 3.9+
- pip (or Poetry)
- Docker (optional but recommended)

---

### 🧪 Run Locally

```bash
git clone https://github.com/nguyenlyminhman/fastapi-ddd-starter-template.git
cd fastapi-ddd-starter-template
pip install -r requirements.txt
sh dev.sh
```

Open:
```
http://localhost:8000
```

---

## 🧬 Usage

- `domain/` → business entities & rules
- `application/` → use cases & services
- `infrastructure/` → DB, external services
- `presentation/` → FastAPI routes

---

## 📦 Environment Variables

Example `.env`:

```
APP_ENV=development
DATABASE_URL=postgresql://user:pass@localhost/db
```

---

## 🧪 Testing

```bash
pytest --maxfail=1 --disable-warnings --cov=src
```

---

## 🧩 Contributing

PRs and issues are welcome ❤️

---

## 📝 License

MIT License

---

## 📌 Notes

This is a starter template. Add:
- Auth
- DB migrations
- Background jobs
- CI/CD
as needed.
