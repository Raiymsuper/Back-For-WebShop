# Project: demoprp

## Overview

demoprp is a Django-based web application that provides an API for managing items and user authentication. The application supports user registration, login, and profile management. It also features item listing with filtering, sorting, and pagination capabilities.

## Project Structure

- **IaUstal**: Main Django app containing models, views, serializers, and filters.
- **demoprp**: Main project directory containing settings, URLs, and WSGI configurations.

## Installation

### Prerequisites

- Python 3.7+
- PostgreSQL 16
  
### Clone the Repository

```bash
git clone https://github.com/Raiymsuper/Back-For-WebShop.git
cd demoprp
```

### Setup Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Configuration

Update the `DATABASES` configuration in `settings.py` with your PostgreSQL database details.

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- **Register**: `POST /api/register/`
- **Login**: `POST /api/login/`
- **User Profile**: `GET /api/profile/`

### Items

- **List Items**: `GET /api/items/`
- **Filter Items**: Add query parameters `name` and `price` to filter items.
- **Sort Items**: Add query parameter `ordering` with values `name`, `-name`, `price`, or `-price` to sort items.

## Usage

### Register

```bash
POST /api/register/
{
    "username": "yourusername",
    "password": "yourpassword",
    "email": "youremail@example.com"
}
```

### Login

```bash
POST /api/login/
{
    "username": "yourusername",
    "password": "yourpassword"
}
```

### User Profile

```bash
GET /api/profile/
```

### List Items

```bash
GET /api/items/
```

### Filter Items

```bash
GET /api/items/?name=&price=140
```

### Sort Items

```bash
GET /api/items/?ordering=price    # Sort by price (low to high)
GET /api/items/?ordering=-price   # Sort by price (high to low)
GET /api/items/?ordering=name     # Sort by name (A to Z)
GET /api/items/?ordering=-name    # Sort by name (Z to A)
```

## Settings

### Allowed Hosts

Update `ALLOWED_HOSTS` in `settings.py` with your domain names.

### CORS

Update `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` in `settings.py` with your frontend URLs.

## Deployment

### Static Files

```bash
python manage.py collectstatic
```

### WSGI

The project uses WSGI for deployment. The configuration is available in `wsgi.py`.

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- React (for frontend, assumed to be deployed separately)
- JWT (for authentication)

## Contact

Telegram: @straw_hat_emae
