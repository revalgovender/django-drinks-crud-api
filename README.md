# Drinks CRUD REST API

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [CRUD Endpoints](#crud-endpoints)
    - [Create a Drink](#create-a-drink)
    - [List All Drinks](#list-all-drinks)
    - [Update a Drink](#update-a-drink)
    - [Delete a Drink](#delete-a-drink)

## About

This project is a simple CRUD REST API built with Django and Django REST Framework. The
API manages a single entity, "drinks," which has properties for name and description.

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

Start the development server:

```bash
python manage.py runserver
```

## CRUD Endpoints

The API provides CRUD (Create, Read, Update, Delete) operations for managing "drinks" entities.

### Create a Drink

**Endpoint**: `POST /api/drinks/`

To create a new drink, send a POST request with a JSON payload:

```json
{
  "name": "Coffee",
  "description": "Hot and energizing"
}
```

### List All Drinks

Endpoint: `GET /api/drinks/`

Retrieve a list of all drinks.

### Retrieve a Drink

Endpoint: `GET /api/drinks/{id}/`

Retrieve details of a specific drink by its ID.

### Update a Drink

Endpoint: `PUT /api/drinks/{id}/`

To update a drink, send a PUT request to the specified endpoint with a JSON payload containing the updated information.

#### Request

```http
PUT /api/drinks/{id}/ HTTP/1.1
Content-Type: application/json

{
  "name": "Iced Coffee",
  "description": "Cold and refreshing"
}
```

### Delete a Drink

**Endpoint:** `DELETE /api/drinks/{id}/`

Deletes a drink by its ID.

#### Request

- **Method:** `DELETE`
- **URL:** `/api/drinks/{id}/`