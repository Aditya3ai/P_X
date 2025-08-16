
# Dynamic Invitation Generator

This project is a web application that allows users to create and customize digital invitations. Users can add details such as names, dates, stories, events, and upload media (images, cover photos, etc.). Each invitation is generated dynamically, can be exported as a PDF, and is accessible through a unique URL that can be shared globally.

The application also stores user data in a SQL database, which can be used for insights, analytics, and improvements.



## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Installation and Setup](#installation-and-setup)
* [Deployment](#deployment)
* [Future Enhancements](#future-enhancements)
* [Author](#author)


## Features

* User-friendly interface to customize invitation content
* Upload images and media for personalization
* Slug-based unique URLs for each invitation
* PDF generation for offline sharing and printing
* Global accessibility through hosted links
* Database storage for user details and analytics

---

## Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** PostgreSQL (SQLAlchemy ORM)
* **Deployment:** Render

---

## Project Structure

```
P_X/
│── static/              # CSS, JS, Images
│── templates/           # HTML templates
│── app.py               # Main Flask application
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

---

## Installation and Setup

1. Clone the repository

   ```bash
   git clone https://github.com/Aditya3ai/P_X.git
   cd P_X
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database connection in `app.py` with your PostgreSQL details.

5. Create the database tables

   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   ```

6. Run the application

   ```bash
   flask run
   ```

---

## Deployment

The application is deployed on **Render** and can be accessed globally.

---

## Future Enhancements

* Multiple themes and templates for invitations
* Video/audio-based invitation support
* Advanced analytics dashboard for user engagement
* Admin panel for managing user data

---

## Author

**Aditya Padma**
[GitHub](https://github.com/Aditya3ai)

