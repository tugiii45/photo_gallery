#  Photo Gallery Web App

A modern and responsive photo gallery web application built with Django and Tailwind CSS. The application allows authenticated users to browse photos and artworks, filter photos by tags, like or dislike photos, and manage their user profiles.

##  Features

### User Authentication

- User registration with username, email, and password
- Secure user login and logout
- Django password validation
- Secure password change functionality
- Authentication-based access control

### User Profile Management

- Automatic profile creation for registered users
- Dedicated user profile page
- Display of username and email address
- Custom user bio
- Profile picture uploads
- Profile editing functionality
- Secure password updates

### Photo Gallery

- Responsive photo gallery
- Photo titles and descriptions
- Cloud-based image storage using Cloudinary
- Detailed photo view
- Photo uploader information
- Photo creation timestamps

###  Photo Filtering

- Photos can have multiple tags
- Dynamic tag generation
- Filter photos based on tags
- View all photos using the **All** filter

###  User Interactions

- Like and unlike photos
- Dislike and remove dislikes
- Users cannot like and dislike the same photo simultaneously
- Like and dislike counts

### Responsive Design

- Responsive desktop and mobile layouts
- Modern interface built with Tailwind CSS
- Responsive photo grid
- User-friendly navigation

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML5
- Tailwind CSS
- Cloudinary
- Git
- GitHub

## Project Structure

```text
photo_gallery/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── photo_gallery/
│   ├── migrations/
│   ├── templates/
│   │   └── photo_gallery/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── profile.html
│   │       ├── photo_detail.html
│   │       └── change_password.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

##  Getting Started

Follow the instructions below to run the project locally.

### 1. Clone the Repository

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd photo_gallery
```

### 2. Create a Virtual Environment

```bash
python -m venv virtual
```

Activate the virtual environment.

#### Windows PowerShell

```powershell
virtual\Scripts\Activate.ps1
```

#### Git Bash

```bash
source virtual/Scripts/activate
```

#### macOS/Linux

```bash
source virtual/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Database Setup

Create a PostgreSQL database for the project.

Example database name:

```text
photo_gallery_db
```

Configure the PostgreSQL database in the Django settings.



##  Cloudinary Configuration

The project uses Cloudinary for photo and profile image storage.

Create a `.env` file in the root project directory.

Add your Cloudinary configuration:

```env
CLOUDINARY_URL=cloudinary://YOUR_API_KEY:YOUR_API_SECRET@YOUR_CLOUD_NAME
```

Never commit the `.env` file to GitHub.

Ensure `.env` is included in `.gitignore`.

## Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

##  Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the terminal prompts to create an administrator account.

##  Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The Django admin dashboard is available at:

```text
http://127.0.0.1:8000/admin/
```

## How to Use the Application

1. Register for a new account.
2. Log in using your credentials.
3. Browse photos in the gallery.
4. Filter photos using tags.
5. Click a photo to view its details.
6. Like or dislike photos.
7. Open your profile to update your email, bio, or profile picture.
8. Change your account password securely.


## Deployment

The application can be deployed using Render.

Before deployment:

1. Set `DEBUG = False`.
2. Configure `ALLOWED_HOSTS`.
3. Add environment variables to the hosting platform.
4. Configure a production PostgreSQL database.
5. Run Django migrations.
6. Create a production superuser if required.


##  Contributing

Contributions to the Photo Gallery Web App are welcome.

### How to Contribute

1. Fork the repository.

2. Clone your fork:

```bash
git clone <your-fork-repository-url>
```

3. Navigate into the project directory:

```bash
cd photo_gallery
```

4. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

5. Make your changes and test the application.

6. Stage your changes:

```bash
git add .
```

7. Commit your changes:

```bash
git commit -m "feat: add your feature description"
```

8. Push your branch:

```bash
git push origin feature/your-feature-name
```

9. Open a Pull Request and provide a clear description of your changes.


## 👨‍💻 Author

**Conrad Mutugi**

Software Engineering Student

Built as part of a Django web development project.