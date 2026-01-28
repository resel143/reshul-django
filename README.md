# 📚 Library Management Backend (Django)

A **backend-intensive Library Management System** built on **Django** and **Django REST Framework (DRF)**.  
This repository contains all **REST APIs**, database models, search logic, and backend architecture powering the Library Project.

The frontend for this project is built using **React.js** and is maintained in a separate repository.

---

## 🚀 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- SQLite (default, easily configurable to PostgreSQL)
- RESTful API Architecture


---

## 🖼️ API Demo Screenshot

Below is a snapshot showing API responses in action:

![API Demo](https://github.com/resel143/reshul-django/blob/main/newbackend/assets/api_demo.png)

---

## 🎥 Demo (Backend + API Flow)

![Library Backend Demo](https://github.com/resel143/reshul-django/blob/main/newbackend/assets/Demo-gif.gif)

---

## 🔗 Frontend Repository

👉 **React Frontend Repo:**  
https://github.com/resel143/ReactJS-Mini-Projects/tree/master/Library%20Project

---

## 🎯 Backend Features

- 📘 Book CRUD APIs (Create, Read, Update, Delete)
- 🔍 Search API for books
- 📌 Fetch book by ID
- 🧠 Clean REST API architecture
- 🗂 Modular Django app structure
- 📄 JSON-based API responses
- 🧪 Easy to test via Postman

---

## 🧩 Completed Issues / Work Log

All the following backend tasks are **completed and closed**:

- ✅ Initialize Django Project
- ✅ Django URLs & Routing Concepts
- ✅ Templates Setup
- ✅ Static Files Rendering
- ✅ Template Variable Rendering
- ✅ Backend Folder Structure Setup
- ✅ Book Data Model Creation
- ✅ REST API – GET All Books
- ✅ REST API – POST (Create Book)
- ✅ REST API – UPDATE Book
- ✅ REST API – DELETE Book
- ✅ GET Book by ID API
- ✅ Search API Implementation
- ✅ Backend ↔ Frontend Integration Support
- ✅ Demo Added

---

## 📦 API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/api/books/` | Fetch all books |
| GET | `/api/books/<id>/` | Get book by ID |
| POST | `/api/books/create/` | Create new book |
| PATCH | `/api/books/update/` | Update book |
| DELETE | `/api/books/delete/<id>/` | Delete book |
| GET | `/api/books/search/<query>/` | Search books |

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/resel143/reshul-django.git
cd reshul-django
