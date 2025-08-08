# Field Target App

## 📌 Description
**Field Target** is a Django-based web application for managing shooting competitions, competitor registrations and sponsors.

### Features
- 🏆 Create, edit, and delete competitions
- 👤 Competitor registration system
- 💼 Sponsor management
- 📅 Competition detail pages with participant lists
- 🔒 Admin-only actions for sensitive operations
- 🌐 Optional REST API for Competitions (read-only for public, POST for admins)

---


## ⚙️ Requirements
- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework** (for API)
- **Bootstrap 5** (for UI styling)
- **Pillow** (for image uploads)
- **PostgreSQL**

---

## 🚀 Installation


### 1️⃣ Clone the repository
```
https://github.com/papazoff06/field_target.git
cd field_targe
```
### 2️⃣ Create & activate a virtual environment for Windows
```
python -m venv .venv
.\.venv\Scripts\activate

```
### 2️⃣ Create & activate a virtual environment for Mac/Linux
```
python3 -m venv .venv
source .venv/bin/activate
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Create a superuser
```
python manage.py createsuperuser
```
### 6️⃣ Run the development server
```
python manage.py runserver
```
```
Access the site at http://127.0.0.1:8000/
```
## 📖 Usage
- Competitions: Create via admin or dedicated forms.

- Registration: Logged-in users can register for competitions.

- Sponsors: Manage via admin; displayed on competition pages.

- API:
  - GET /api/competitions/ → List of competitions (public)

  - GET /api/competitions/{id}/ → competition details (public)

  - POST /api/competitions/ → Create competition (admin only)

### 🔐 Security

- Only authenticated users can register.
- Only admin and staff can edit competitions.
- Only admin can delete competitions.
- API POST/PUT/DELETE actions are admin-only.

### 🖼 Templates
- login.html → Login form
- register → Register form
- profile-delete.html → Delete your profile
- profile-details.html → See details about your profile
- profile-edit.html → Edit data in your profile form
- all-competitions.html → All competitions
- competition-details.html → Competition details, registrations, sponsors
- competition-create.html → Create competition
- competition-delete.html → Fancy delete confirmation
- competition-edit.html → Edit competition
- competition-register.html → Register for competition
- base.html → Site layout
- home.html → Home page

### 📦 Deployment Notes
Before deploying to production:

- Set DEBUG = False
- Configure ALLOWED_HOSTS
- Serve static files properly
- Use a secure database setup
- Enable HTTPS with a valid SSL certificate

### 👤 Author
- Anton Papazov
- 📧 papazov06@gmail.com
- 📅 2025-08-08