<h1 align="center"> Web Diary </h1>

<p align="center">
Diary is a fullstack application to record your memories.<br/>
</p>

<p align="center">
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-deploy">Run Locally</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>


## 🚀 Technologies
- Python
- Django
- HTML
- Pillow
- SQLite3

## 💻 Run Locally

> To run the project locally you must have `PYTHON` and `DJANGO` on your computer


Steps to run it locally:

1. Clone the Repository

```bash
git clone <repository-url>
``` 
2. Set Up a Virtual Environment

- Linux/Mac:
```bash
python3 -m venv env
source env/bin/activate
```

- Windows:
```bash
python -m venv env
.\env\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

5. Apply Migrations
Run the following commands to create the database and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Run the Development Server

```bash
python manage.py runserver
```

8. Access the Application
```bash
http://127.0.0.1:8000
```

9. Start registering your memories!

<br/><br/>

---
### Developed by Vinicius Nascimento with Pythonando.
