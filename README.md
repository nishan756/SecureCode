# 🔐 SecureCode

**SecureCode** is a Django REST Framework-based URL shortening and access management application. It allows authenticated users to create short URLs, manage their codes, and control access through public and private visibility settings.

Users can also grant access to specific registered users or email addresses.

## ✨ Features

### 🔗 URL Shortening
- Generate unique 6-character short codes.
- Convert long URLs into short codes.
- Retrieve original URLs using generated codes.
- Set expiration dates for short codes.
- Enable or disable individual codes.

### 🔒 Access Management
- Public and private visibility options.
- Grant access to specific registered users.
- Grant access through email addresses.
- Remove previously assigned permissions.
- Owner-based permission management.

### 👤 User Management
- User registration and authentication.
- Login using username or email.
- Custom user model.
- Profile information updates.
- Profile image upload.
- Password updates.
- User search by username.

### ⚙️ Code Management
- View all your generated codes.
- Delete individual codes.
- Delete multiple codes simultaneously.
- UUID-based identifiers for secure code management.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Django | Backend Framework |
| Django REST Framework | REST API Development |
| SQLite | Database |
| Pillow | Image Processing |
| Python Dotenv | Environment Configuration |

## 📁 Project Structure

```text
SecureCode/
│
├── app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── exceptions.py
│   │
│   ├── repositories/
│   └── services/
│
├── session/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── backends.py
│
├── secure_code/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## 🚀 Getting Started

Follow these instructions to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/nishan756/SecureCode.git

cd SecureCode
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Keep your secret key and email credentials private. Never commit your `.env` file to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## 📡 API Endpoints

The application provides two main API modules: `app` and `session`.

### 🔗 SecureCode APIs

Base URL: `/app/`

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/app/get/{code}/` | Retrieve original URL | No |
| POST | `/app/create/` | Create a short code | Required |
| GET | `/app/my-codes/` | Retrieve user's codes | Required |
| DELETE | `/app/delete/{id}/` | Delete a code | Required |
| DELETE | `/app/delete-multiple/` | Delete multiple codes | Required |
| POST | `/app/add-user-permission/{id}` | Grant user access | Required |
| POST | `/app/add-email-permission/{id}/` | Grant email access | Required |
| DELETE | `/app/delete-user-permission/{id}/` | Remove user access | Required |
| DELETE | `/app/delete-email-permission/{id}/` | Remove email access | Required |

### 👤 Authentication APIs

Base URL: `/session/`

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/session/signup/` | Register a new user | No |
| POST | `/session/login/` | Authenticate user | No |
| GET | `/session/logout/` | Logout user | Required |
| PUT | `/session/update-password/` | Update password | Required |
| PUT | `/session/update-info/` | Update profile information | Required |
| GET | `/session/users/` | Search users by username | No |

## 📝 Example API Requests

### 1. User Registration

**POST** `/session/signup/`

```json
{
    "username": "john",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "StrongPassword123",
    "confirm_password": "StrongPassword123"
}
```

### 2. User Login

**POST** `/session/login/`

```json
{
    "username": "john",
    "password": "StrongPassword123"
}
```

You can use either your username or email address as the login identifier.

### 3. Create a Secure Code

**POST** `/app/create/`

```json
{
    "original_url": "https://example.com/some/very/long/url",
    "visibility": "public",
    "expires_at": null
}
```

### 4. Retrieve Original URL

**GET** `/app/get/{code}/`

Example:

```http
GET /app/get/aB12xY/
```

Response:

```json
{
    "original_url": "https://example.com/some/very/long/url"
}
```

### 5. Grant Access to a User

**POST** `/app/add-user-permission/{id}`

```json
{
    "user": 2
}
```

### 6. Grant Access Through Email

**POST** `/app/add-email-permission/{id}/`

```json
{
    "email": "user@example.com"
}
```

*Note: `{id}` represents the UUID of the SecureCode object.*

## 🏗️ Architecture

The project follows a layered architecture to separate responsibilities and improve maintainability.

- **Views:** Handle HTTP requests and responses.
- **Serializers:** Validate and serialize API data.
- **Services:** Handle application-level business logic.
- **Repositories:** Manage database operations.
- **Models:** Define database structures.
- **Custom Exceptions:** Handle application-specific errors.

This separation helps keep business logic independent of HTTP request handling and database access.

## 🔮 Future Improvements

Potential improvements for future development:

- [ ] JWT-based authentication.
- [ ] API documentation using Swagger / OpenAPI.
- [ ] Rate limiting for URL generation.
- [ ] Redis caching.
- [ ] Background task processing with Celery.
- [ ] Comprehensive automated testing.
- [ ] Docker support.
- [ ] Advanced analytics and usage statistics.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

If you have suggestions or want to improve the project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

## 📄 License

This project is currently available for exploration and development. A formal open-source license can be added to define reuse and distribution permissions.

---

**Developed by [Nishan](https://github.com/nishan756)**

GitHub: [github.com/nishan756/SecureCode](https://github.com/nishan756/SecureCode)
