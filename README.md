# Simple Shop 🛒

A beginner-friendly Python project that uses Streamlit, FastAPI, SQLAlchemy, SQLite, and Telegram Bot.

## 🚀 Technologies Used

- **Python** — Main programming language
- **Streamlit** — Shop management dashboard
- **FastAPI** — Provides an API for products
- **SQLAlchemy** — Communicates with the database
- **SQLite** — Stores product information
- **Telegram Bot** — Displays products through Telegram
- **Requests** — Sends HTTP requests to FastAPI

## ✨ Features

- Add new products
- View all products
- Delete products
- Get products through FastAPI
- View products using a Telegram bot

## ⚙️ How It Works

The project has four main parts:

1. **Streamlit:** The user can add, view, and delete products through a simple web interface.
2. **SQLAlchemy and SQLite:** Product information is stored in a database named `shop.db`.
3. **FastAPI:** The API retrieves products from the database and returns them as JSON.
4. **Telegram Bot:** The user sends `/products` to the bot. The bot requests product information from FastAPI and displays the results in Telegram.

### Project Workflow

```text
User
 |
 v
Streamlit Dashboard
 |
 v
SQLAlchemy
 |
 v
SQLite Database
 ^
 |
FastAPI API
 ^
 |
Telegram Bot
```

## 📁 Project Structure

```text
simple_shop/
│
├── app.py
├── api.py
├── bot.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📦 Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Go to the project directory:

```bash
cd simple_shop
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

### 1. Run FastAPI

```bash
uvicorn api:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

### 2. Run Streamlit

Open another terminal and run:

```bash
streamlit run app.py
```

### 3. Run Telegram Bot

Create a bot using [@BotFather](https://t.me/BotFather).

Add your bot token to `bot.py`, then run:

```bash
python bot.py
```

**Important:** Never publish your real Telegram bot token on GitHub.

## 📱 Telegram Commands

- `/start` — Start the bot
- `/products` — Display the product list

## 🎯 Project Goal

This project was created for learning Python, databases, APIs, and Telegram bot development. It is designed for beginners who want to understand how these technologies work together.

## 👨‍💻 Author

Created as a beginner Python learning project.
