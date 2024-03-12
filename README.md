## Restaurant Management Backend using Django REST API

### Overview
This project implements the backend part of a restaurant management application using Django REST API. The backend is responsible for managing various aspects of restaurant operations including orders, reservations, accounts, and menu items. It provides a RESTful API that can be consumed by frontend applications to perform CRUD operations on the data.

### Features
Order Management: 
Allows the creation, retrieval, update, and deletion of orders. Each order can contain multiple menu items with their quantities.
Reservation Management: 
Facilitates creating, retrieving, updating, and deleting reservations for tables in the restaurant.
Account Management: 
Manages user accounts including authentication and authorization for accessing the API endpoints.
Menu Management: 
Supports creating, retrieving, updating, and deleting menu items including details like name, description, price, and category.

### Usage
Once the development server is running, you can access the API endpoints using tools like curl or Postman. Alternatively, you can integrate these endpoints into a frontend application.

### API Endpoints
Orders:
GET /api/orders/: Retrieve all orders
POST /api/orders/: Create a new order
GET /api/orders/<id>/: Retrieve a specific order
PUT /api/orders/<id>/: Update a specific order
DELETE /api/orders/<id>/: Delete a specific order
Reservations:
GET /api/reservations/: Retrieve all reservations
POST /api/reservations/: Create a new reservation
GET /api/reservations/<id>/: Retrieve a specific reservation
PUT /api/reservations/<id>/: Update a specific reservation
DELETE /api/reservations/<id>/: Delete a specific reservation
Accounts:
POST /api/accounts/register/: Register a new user
POST /api/accounts/login/: Obtain an authentication token
GET /api/accounts/profile/: Retrieve user profile information
PUT /api/accounts/profile/: Update user profile information
POST /api/accounts/logout/: Logout user
Menus:
GET /api/menus/: Retrieve all menus
POST /api/menus/: Create a new menu
GET /api/menus/<id>/: Retrieve a specific menu
PUT /api/menus/<id>/: Update a specific menu
DELETE /api/menus/<id>/: Delete a specific menu

### Authentication
Authentication is required for certain endpoints such as orders, reservations, and user accounts. You need to obtain an authentication token by registering or logging in before accessing these endpoints.

### Contact
For any inquiries or feedback, please contact Akrem Issaoui.
