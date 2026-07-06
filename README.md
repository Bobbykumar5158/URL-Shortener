# URL-Shortener
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Deployment](https://img.shields.io/badge/Deployment-Railway-purple)

A modern Flask-based URL shortener web application that converts long URLs into short, shareable links with real-time click tracking and dashboard analytics.

## Live Demo

[Visit Live Website](url-shortener-production-63e9.up.railway.app)

---

## Features

- Shorten long URLs instantly
- Generate unique short links
- Fast redirection system
- Click tracking support
- Responsive modern UI
- Dashboard to manage links
- REST API endpoint
- JSON-based lightweight storage
- Railway cloud deployment

---

## Tech Stack

* Python
* Flask
* HTML5
* CSS3
* Gunicorn
* Railway
* JSON Storage

---

## Project Structure

```text
URL-Shortner/
│
├── static/
│   └── style/
│       └── base.css
│
├── templates/
│   ├── api.html
│   ├── base.html
│   ├── dashboard.html
│   ├── error.html
│   └── home.html
│
├── .gitignore
├── README.md
├── app.py
├── data.json
├── db.py
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Bobbykumar5158/URL-Shortener.git
cd URL-Shortner
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in your browser:

```text
http://127.0.0.1:5000
```

---

## Deployment

This application is deployed on Railway using Gunicorn.

### Procfile

```text
web: gunicorn app:app
```

---

## How It Works

1. User enters a long URL
2. Flask application generates a unique short code
3. URL mapping gets stored in `data.json`
4. Visiting the short URL redirects to the original website

---

## Example

### Original URL

```text
https://www.google.com
```

### Shortened URL

```text
https://url-shortener-production-63e9.up.railway.app/s/8TCSnz
```

---

## Screenshots

### Home Page

<img width="1536" height="879" alt="image" src="https://github.com/user-attachments/assets/103b9a51-b5a3-4e28-9d0d-c56f2892d01d" />


### Dashboard Page

<img width="1532" height="861" alt="image" src="https://github.com/user-attachments/assets/804b7145-832e-44aa-9963-b2d7ff453481" />

### Error Page
<img width="1526" height="872" alt="image" src="https://github.com/user-attachments/assets/d628458f-1855-4569-a8bd-b120723c3871" />



---
## 🔌 API Documentation Page
Retrieve all stored links:
```
/api/links
```
<img width="1528" height="877" alt="image" src="https://github.com/user-attachments/assets/995c9b52-3ff8-477c-a524-a50b9cdbe02c" />



---
