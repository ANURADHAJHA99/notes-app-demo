
# 📝 Notes Project

This is a Django application that allows users to create and manage personal notes. The application supports user authentication and provides APIs for creating, reading, updating, and deleting notes.

## 🛠️ Setup

### 📂 Clone the Repository

```sh
git clone https://github.com/ANURADHAJHA99/notes-app-demo
cd notes_project
```

### 🔧 Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
DATABASE_NAME=koyebdb
DATABASE_USER=koyeb-adm
DATABASE_PASSWORD=QS2Riwj0gkoC
DATABASE_HOST=ep-autumn-shape-a2fl96f4.eu-central-1.pg.koyeb.app
DATABASE_PORT=5432
```

### 🐳 Build and Run the Docker Containers

```sh
docker-compose up --build
```

### ⚙️ Run Migrations and Create a Superuser

```sh
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

### 🌐 Access the Application

The application will be available at [http://localhost:8000](http://localhost:8000).

## 🔌 API Endpoints

### 🧑‍💻 User Registration

**Endpoint:** POST `/api/users/`

**Description:** Registers a new user.

**Request:**

```sh
curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass123"}'
```

### 🔑 Obtain Authentication Token

**Endpoint:** POST `/api-token-auth/`

**Description:** Obtains an authentication token for a user.

**Request:**

```sh
curl -X POST http://127.0.0.1:8000/api-token-auth/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass123"}'
```

**Response:**

```json
{
    "token": "your_generated_token"
}
```

### 📝 Create a Note

**Endpoint:** POST `/api/notes/`

**Description:** Creates a new note.

**Request:**

```sh
curl -X POST http://127.0.0.1:8000/api/notes/ -H "Content-Type: application/json" -H "Authorization: Token your_generated_token" -d '{"title": "Test Note", "body": "This is a test note."}'
```

### 📋 List Notes

**Endpoint:** GET `/api/notes/`

**Description:** Lists all notes for the authenticated user.

**Request:**

```sh
curl -X GET http://127.0.0.1:8000/api/notes/ -H "Authorization: Token your_generated_token"
```

### 🔍 Retrieve a Note

**Endpoint:** GET `/api/notes/<id>/`

**Description:** Retrieves a specific note by its ID.

**Request:**

```sh
curl -X GET http://127.0.0.1:8000/api/notes/1/ -H "Authorization: Token your_generated_token"
```

### ✏️ Update a Note

**Endpoint:** PUT `/api/notes/<id>/`

**Description:** Updates a specific note by its ID.

**Request:**

```sh
curl -X PUT http://127.0.0.1:8000/api/notes/1/ -H "Content-Type: application/json" -H "Authorization: Token your_generated_token" -d '{"title": "Updated Test Note", "body": "This is an updated test note."}'
```

### 🗑️ Delete a Note

**Endpoint:** DELETE `/api/notes/<id>/`

**Description:** Deletes a specific note by its ID.

**Request:**

```sh
curl -X DELETE http://127.0.0.1:8000/api/notes/1/ -H "Authorization: Token your_generated_token"
```

## 📑 Summary of API Endpoints

- **User Registration:** POST `/api/users/`
- **Obtain Authentication Token:** POST `/api-token-auth/`
- **Create a Note:** POST `/api/notes/`
- **List Notes:** GET `/api/notes/`
- **Retrieve a Note:** GET `/api/notes/<id>/`
- **Update a Note:** PUT `/api/notes/<id>/`
- **Delete a Note:** DELETE `/api/notes/<id>/`

## 🧪 Running Tests

To run the tests for this project, use the following command:

```sh
python manage.py test
```

## 🌐 Postman Collection
You can access the Postman collection for this project here(https://www.postman.com/dark-resonance-874488/workspace/public/request/8821057-e8ee1036-bfd7-436b-a7cb-fcfbf2aa8fb0).

