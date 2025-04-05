# Project: REST API for Online Classifieds

This project implements a REST API (backend) for an online classifieds website.

It provides endpoints for creating, deleting, and editing User and their advertisements.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/Lynatuk666/.git
    cd online-classifieds
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the migrations:
    ```bash
    alembic upgrade head
    ```

4. Run the main.py file

## Endpoints

The API provides the following endpoints:

### Users

-   `GET /api/user/{user_id}`: Return username by ID.
-   `POST /api/user`: Create a new user and return its ID.
-   `PATCH /api/user/{user_id}`: Update name of existing user by ID.
-   `DELETE /api/user/{user_id}`: Delete an existing user by ID.

### Advertisements

-   `GET /api/adv`: Return a list of all advertisements.
-   `GET /api/adv/{adv_id}`: Return an advertisement by ID.

-   `POST /api/user/{user_id}/adv`: Create a new advertisement and return its ID.
-   `DELETE /api/user/{user_id}/adv/{adv_id}`: Delete an existing advertisement by ID.
-   `PATCH /api/user/{user_id}/adv/{adv_id}`: Update title and description of an existing advertisement by ID.
- 
Each user has the following fields:

-   **name:** The name of the user.
-   **id**: The unique identifier of the user.

Each advertisement includes the following fields:

-   **id:** The unique identifier of the advertisement.
-   **title:** The title of the advertisement.
-   **description:** A detailed description of the item or service being advertised.
-   **creation_date:** The date and time the advertisement was created.
-   **owner:** Information about the user who created the advertisement.

The API supports the following HTTP methods:

-   `GET`: Retrieve a list of all advertisements.
-   `POST`: Create a new advertisement.
-   `DELETE`: Delete an existing advertisement.
-   `PATCH`: Update an existing advertisement.

## Technologies Used

-   **Main Framework:** aiohttp
-   **Database:** PostgreSQL
-   **Database Driver:** asyncpg