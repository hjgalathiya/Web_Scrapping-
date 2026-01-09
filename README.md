# Python Web Scraping & Django Display Project

## 📌 Project Overview

This project is a complete Python-based solution that demonstrates **web scraping, data storage, and web application development**.

The application scrapes quotes from **[https://quotes.toscrape.com](https://quotes.toscrape.com)**, stores the data in both **CSV** and **SQLite**, and displays the scraped data using a **Django web application**.

This project was developed as part of a technical assignment to showcase backend and Python skills.

---

## 🛠 Technologies Used

* Python 
* Requests
* BeautifulSoup4
* SQLite
* Django
* HTML & CSS

---


## 🔍 Features

* Scrapes data from **minimum 10 pages** (pagination handled)
* Extracts:

  * Quote text
  * Author name
  * Tags
  * Author profile URL
* Stores data in:

  * CSV file
  * SQLite database
* Prevents duplicate entries in the database
* Displays scraped data using Django web application
* Clean and readable user interface

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd project-root
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Required Libraries

```bash
pip install requests beautifulsoup4 django
```

---

## ▶️ How to Run the Scraper

```bash
python scraper.py
```

This will:

* Scrape quotes from the website
* Create `quotes.csv`
* Create `quotes.db` with all scraped data

---

## 🌐 Running the Django Web Application

### 1️⃣ Navigate to Django Project

```bash
cd quotes_web
```

### 2️⃣ Start Development Server

```bash
python manage.py runserver
```

### 3️⃣ Open Browser

```
http://127.0.0.1:8000/
```

You will see all scraped quotes displayed with author names, tags, and profile links.

---

## 🧠 Database Design

* SQLite database used
* Single table: `quotes`
* Duplicate prevention using **UNIQUE constraint** on quote text
* Django models configured with `managed = False` to use existing database

---

## 📊 CSV Format

```
csv
quote,author,tags,author_profile

```

## 📌 Notes

* UI is kept simple for clarity and readability
* Project focuses on correctness, structure, and functionality
* Can be extended with search, filters, or advanced styling

---

## 👨‍💻 Author

**Harsh Galathiya**
Python Developer

---


